#!/usr/bin/env python3
"""Contas proporcionais cujo contrato e parâmetros ficam no documento dono.

Uso: python3 validacao/caminhos.py [documentos.md ...] [--publicar]

Cada documento contém um JSON cercado por ``<!-- parametros-caminho -->`` e
``<!-- /parametros-caminho -->``. O contrato usa ``params`` (números),
``bindings`` ({pattern, key}), ``checks`` opcionais ({label, expr}) e ``groups``.
Cada grupo tem ``name``, ``cap``, ``items`` ({name, expr, reserve}) e, opcionalmente,
``sensitivity`` (substituições de params). As expressões de item já retornam
fatias. ``reserve`` é uma reserva de projeto, não benefício demonstrado.

O relatório fica entre ``<!-- contas-caminho -->`` e ``<!-- /contas-caminho -->``.
Sem --publicar, o arquivo é somente lido e o relatório publicado é conferido.
O teto vale para a referência; a sensibilidade é informativa e nunca substitui
a referência silenciosamente. Este programa não inventa hipóteses ou preços.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import json
import keyword
import math
from pathlib import Path
import re
import sys


PARAM_START = "<!-- parametros-caminho -->"
PARAM_END = "<!-- /parametros-caminho -->"
RESULT_START = "<!-- contas-caminho -->"
RESULT_END = "<!-- /contas-caminho -->"
FUNCTIONS = {"min": min, "max": max, "ceil": math.ceil, "floor": math.floor}
LIMIT = 1e12


class ValidationError(ValueError):
    """Documento, expressão ou conta inconsistente."""


def number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError(f"{label}: deve ser número, sem valor booleano.")
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValidationError(f"{label}: número fora do limite.") from exc
    if not math.isfinite(result) or abs(result) > LIMIT:
        raise ValidationError(f"{label}: número não finito ou fora do limite.")
    return result


def expression(source: object, params: dict[str, float]) -> float | bool:
    """Interpreta uma pequena árvore; nunca executa eval, atributos ou imports."""
    if not isinstance(source, str) or not source.strip() or len(source) > 4000:
        raise ValidationError("Expressão ausente ou extensa demais.")
    try:
        tree = ast.parse(source, mode="eval")
    except (SyntaxError, ValueError, RecursionError) as exc:
        raise ValidationError(f"Expressão inválida: {source!r}.") from exc
    if sum(1 for _ in ast.walk(tree)) > 400:
        raise ValidationError("Expressão complexa demais.")

    def numeric(node: ast.AST) -> float:
        return number(visit(node), source)

    def visit(node: ast.AST) -> float | bool:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant):
            return number(node.value, source)
        if isinstance(node, ast.Name):
            if node.id not in params:
                raise ValidationError(f"Parâmetro desconhecido: {node.id}.")
            return params[node.id]
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                operand = visit(node.operand)
                if not isinstance(operand, bool):
                    raise ValidationError("not exige uma comparação booleana.")
                return not operand
            value = numeric(node.operand)
            if isinstance(node.op, ast.UAdd):
                return value
            if isinstance(node.op, ast.USub):
                return -value
        if isinstance(node, ast.BinOp):
            left, right = numeric(node.left), numeric(node.right)
            try:
                if isinstance(node.op, ast.Add):
                    result = left + right
                elif isinstance(node.op, ast.Sub):
                    result = left - right
                elif isinstance(node.op, ast.Mult):
                    result = left * right
                elif isinstance(node.op, ast.Div):
                    result = left / right
                elif isinstance(node.op, ast.Pow) and abs(right) <= 16:
                    result = left ** right
                else:
                    raise ValidationError("Operador não permitido ou expoente fora do limite.")
            except (ZeroDivisionError, OverflowError, ValueError) as exc:
                raise ValidationError(f"Operação indefinida: {source!r}.") from exc
            return number(result, source)
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in FUNCTIONS:
                raise ValidationError("Somente min, max, ceil e floor são permitidos.")
            if node.keywords or not 1 <= len(node.args) <= 16:
                raise ValidationError("Quantidade de argumentos inválida.")
            name = node.func.id
            if name in ("ceil", "floor") and len(node.args) != 1:
                raise ValidationError(f"{name} exige um argumento.")
            if name in ("min", "max") and len(node.args) < 2:
                raise ValidationError(f"{name} exige ao menos dois argumentos numéricos.")
            args = [numeric(arg) for arg in node.args]
            return number(FUNCTIONS[name](*args), source)
        if isinstance(node, ast.Compare):
            left = numeric(node.left)
            results = []
            for operator, right_node in zip(node.ops, node.comparators):
                right = numeric(right_node)
                if isinstance(operator, ast.Lt):
                    results.append(left < right)
                elif isinstance(operator, ast.LtE):
                    results.append(left <= right)
                elif isinstance(operator, ast.Gt):
                    results.append(left > right)
                elif isinstance(operator, ast.GtE):
                    results.append(left >= right)
                elif isinstance(operator, ast.Eq):
                    results.append(left == right)
                elif isinstance(operator, ast.NotEq):
                    results.append(left != right)
                else:
                    raise ValidationError("Comparação não permitida.")
                left = right
            return all(results)
        if isinstance(node, ast.BoolOp) and isinstance(node.op, (ast.And, ast.Or)):
            values = [visit(value) for value in node.values]
            if any(not isinstance(value, bool) for value in values):
                raise ValidationError("and/or exigem comparações booleanas.")
            return all(values) if isinstance(node.op, ast.And) else any(values)
        raise ValidationError(f"Construção não permitida: {type(node).__name__}.")

    try:
        return visit(tree)
    except RecursionError as exc:
        raise ValidationError("Expressão profunda demais.") from exc


def mapping(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        raise ValidationError(f"{label}: deve ser objeto JSON.")
    return value


def records(value: object, label: str, *, allow_empty: bool = True) -> list[dict]:
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValidationError(f"{label}: deve ser uma lista{' não vazia' if not allow_empty else ''}.")
    return [mapping(item, label) for item in value]


def name(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(c in value for c in "\n\r|"):
        raise ValidationError(f"{label}: nome vazio ou incompatível com a tabela.")
    return value.strip()


def block(text: str, start: str, end: str) -> tuple[int, int, str]:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValidationError(f"Exige exatamente um par {start} / {end}.")
    begin, finish = text.index(start) + len(start), text.index(end)
    if finish < begin:
        raise ValidationError(f"Ordem incorreta dos marcadores {start}.")
    return begin, finish, text[begin:finish]


def params_from(value: object, label: str) -> dict[str, float]:
    result = {}
    for key, value in mapping(value, label).items():
        if not isinstance(key, str) or not key.isidentifier() or keyword.iskeyword(key) or key in FUNCTIONS:
            raise ValidationError(f"Nome de parâmetro inválido: {key!r}.")
        result[key] = number(value, f"{label}.{key}")
    return result


def check_rules(checks: list[dict], params: dict[str, float], scenario: str) -> None:
    for check in checks:
        label = name(check.get("label"), "check.label")
        result = expression(check.get("expr"), params)
        if result is not True:
            raise ValidationError(f"Invariante falhou em {scenario}: {label}.")


def check_bindings(bindings: list[dict], prose: str, params: dict[str, float]) -> None:
    for binding in bindings:
        key, pattern = binding.get("key"), binding.get("pattern")
        if not isinstance(key, str) or key not in params or not isinstance(pattern, str):
            raise ValidationError("Binding exige key existente e pattern textual.")
        try:
            regex = re.compile(pattern, flags=re.MULTILINE)
        except re.error as exc:
            raise ValidationError(f"Binding {key}: regex inválida.") from exc
        if regex.groups != 1:
            raise ValidationError(f"Binding {key}: regex deve ter exatamente um grupo numérico.")
        matches = list(regex.finditer(prose))
        if not matches:
            raise ValidationError(f"Binding {key}: número não encontrado no texto de regra.")
        for match in matches:
            try:
                actual = float(match.group(1).strip().replace(",", "."))
            except (AttributeError, ValueError) as exc:
                raise ValidationError(f"Binding {key}: captura não é número decimal.") from exc
            if not math.isfinite(actual) or not math.isclose(actual, params[key], rel_tol=0, abs_tol=1e-10):
                raise ValidationError(f"Binding {key}: texto {match.group(1)!r} diverge do parâmetro {params[key]:g}.")


@dataclass(frozen=True)
class ItemResult:
    name: str
    calculated: float
    reserved: float

    @property
    def total(self) -> float:
        return self.calculated + self.reserved


def item_results(items: list[dict], params: dict[str, float]) -> list[ItemResult]:
    result = []
    seen = set()
    for item in items:
        label = name(item.get("name"), "item.name")
        if label in seen:
            raise ValidationError(f"Item repetido dentro do grupo: {label}.")
        seen.add(label)
        calculated = number(expression(item.get("expr"), params), label)
        reserve = item.get("reserve", 0)
        if isinstance(reserve, str):
            reserve = expression(reserve, params)
        reserve = number(reserve, f"Reserva de {label}")
        if calculated < 0 or reserve < 0:
            raise ValidationError(f"{label}: conta e reserva precisam ser não negativas.")
        result.append(ItemResult(label, calculated, reserve))
    return result


def fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def totals(items: list[ItemResult]) -> tuple[float, float, float]:
    calculated = math.fsum(item.calculated for item in items)
    reserved = math.fsum(item.reserved for item in items)
    return calculated, reserved, calculated + reserved


def render(data: dict) -> tuple[str, list[str]]:
    params = params_from(data.get("params"), "params")
    checks = records(data.get("checks", []), "checks")
    check_rules(checks, params, "referência")
    lines = [
        "Valores em fatias, calculados apenas nas hipóteses declaradas neste documento. "
        "Reserva é margem de projeto explícita; não é benefício comprovado pela conta. "
        "O total composto soma conta e reserva sem transformar a reserva em medição.",
        "",
    ]
    summaries, seen = [], set()
    for group in records(data.get("groups"), "groups", allow_empty=False):
        label = name(group.get("name"), "group.name")
        if label in seen:
            raise ValidationError(f"Grupo repetido: {label}.")
        seen.add(label)
        cap = number(group.get("cap"), f"Teto de {label}")
        if cap <= 0:
            raise ValidationError(f"Teto de {label}: deve ser positivo.")
        items = records(group.get("items"), "items", allow_empty=False)
        baseline = item_results(items, params)
        calculated, reserved, total = totals(baseline)
        if total > cap + 1e-10:
            raise ValidationError(f"{label}: total de referência {fmt(total)} supera teto {fmt(cap)}.")
        sensitivity = None
        if "sensitivity" in group:
            changes = params_from(group["sensitivity"], "sensitivity")
            if not changes or any(key not in params for key in changes):
                raise ValidationError(f"{label}: sensibilidade precisa substituir parâmetros existentes.")
            alternate = {**params, **changes}
            check_rules(checks, alternate, f"sensibilidade de {label}")
            sensitivity = item_results(items, alternate)
        lines.extend([
            f"**{label}** — teto da referência: {fmt(cap, 2)}.",
            "",
            "| Habilidade | Calculado | Reserva | Total composto |" + (" Total na sensibilidade |" if sensitivity else ""),
            "|---|---:|---:|---:|" + ("---:|" if sensitivity else ""),
        ])
        for index, item in enumerate(baseline):
            row = f"| {item.name} | {fmt(item.calculated)} | {fmt(item.reserved)} | {fmt(item.total)} |"
            if sensitivity:
                row += f" {fmt(sensitivity[index].total)} |"
            lines.append(row)
        row = f"| **Total** | **{fmt(calculated)}** | **{fmt(reserved)}** | **{fmt(total)}** |"
        if sensitivity:
            row += f" **{fmt(totals(sensitivity)[2])}** |"
        lines.extend([row, ""])
        summary = f"{label}: {fmt(calculated)} calculadas + {fmt(reserved)} reservadas = {fmt(total)} / {fmt(cap, 2)}"
        if sensitivity:
            alternative_calculated, alternative_reserved, alternative_total = totals(sensitivity)
            changes_text = ", ".join(f"`{key}` = {fmt(value)}" for key, value in changes.items())
            status = "acima" if alternative_total > cap + 1e-10 else "dentro"
            lines.extend([
                f"Sensibilidade ({changes_text}): {fmt(alternative_calculated)} calculadas + "
                f"{fmt(alternative_reserved)} reservadas = {fmt(alternative_total)}; "
                f"{status} do teto da referência. Este cenário é informativo.",
                "",
            ])
            summary += f"; sensibilidade {fmt(alternative_total)} ({status} do teto)"
        summaries.append(summary)
    return "\n" + "\n".join(lines).rstrip() + "\n", summaries


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"Chave JSON duplicada: {key}.")
        result[key] = value
    return result


def validate_document(path: Path, *, publish: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    param_begin, param_end, raw = block(text, PARAM_START, PARAM_END)
    result_begin, result_end, published = block(text, RESULT_START, RESULT_END)
    if max(param_begin, result_begin) < min(param_end, result_end):
        raise ValidationError("Blocos de parâmetros e resultados não podem se sobrepor.")
    match = re.fullmatch(r"\s*```json\s*\n(.*?)\n```\s*", raw, flags=re.DOTALL)
    if not match:
        raise ValidationError("Bloco de parâmetros exige uma única cerca ```json.")
    try:
        data = mapping(json.loads(match.group(1), object_pairs_hook=unique_object), "raiz")
    except json.JSONDecodeError as exc:
        raise ValidationError(f"JSON inválido: {exc}.") from exc
    params = params_from(data.get("params"), "params")
    prose = text
    for begin, end in sorted(((param_begin, param_end), (result_begin, result_end)), reverse=True):
        prose = prose[:begin] + prose[end:]
    check_bindings(records(data.get("bindings", []), "bindings"), prose, params)
    expected, summaries = render(data)
    if publish:
        if published != expected:
            path.write_text(text[:result_begin] + expected + text[result_end:], encoding="utf-8")
    elif published != expected:
        raise ValidationError("Tabela ausente ou desatualizada; revise premissas e use --publicar.")
    return summaries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("documents", metavar="documento.md", nargs="*", type=Path)
    parser.add_argument("--publicar", action="store_true", help="Atualiza somente o bloco de contas, após validar as premissas.")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    paths = args.documents or [root / "guia-completo.md", root / "emanador-completo.md"]
    failed = False
    for path in paths:
        try:
            summaries = validate_document(path, publish=args.publicar)
        except (OSError, ValidationError) as exc:
            print(f"FALHOU — {path}: {exc}", file=sys.stderr)
            failed = True
            continue
        print(f"OK — {path.name}: {'publicado e conferido' if args.publicar else 'contas e tabela conferidas'}")
        for summary in summaries:
            print(f"  {summary}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
