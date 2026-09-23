#!/usr/bin/env python3
"""Controles negativos dos novos Caminhos, sempre em cópias temporárias.

Uso: python3 validacao/contrateses.py [documentos.md ...]
Não modifica os documentos de trabalho nem publica resultados neles.
"""
from pathlib import Path
import json
import re
import sys
import tempfile

from caminhos import (
    PARAM_START, PARAM_END, RESULT_START, RESULT_END,
    ValidationError, block, render, validate_document,
)


def rejeitar(path, label):
    try:
        validate_document(path)
    except ValidationError as error:
        if "Tabela ausente ou desatualizada" not in str(error):
            raise AssertionError(f"{label}: rejeição inesperada: {error}") from error
        return
    raise AssertionError(f"{label}: alteração não detectada")


def conferir(source, folder):
    original = source.read_text(encoding="utf-8")
    target = folder / source.name
    target.write_text(original, encoding="utf-8")
    validate_document(target)  # A própria cópia precisa passar primeiro.

    begin, end, raw = block(original, PARAM_START, PARAM_END)
    data = json.loads(re.fullmatch(r"\s*```json\s*\n(.*?)\n```\s*", raw, re.S).group(1))
    before, _ = render(data)
    data["params"]["fatia"] += 0.1
    after, _ = render(data)
    assert before != after, "A premissa perturbada não alterou o cálculo."

    # Atualiza também as células vinculadas: uma divergência de binding não
    # pode se passar pela prova de que a conta consome o parâmetro.
    changed = original[:begin] + "\n```json\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n```\n" + original[end:]
    bindings = [entry for entry in data["bindings"] if entry["key"] == "fatia"]
    assert bindings, "Fatia sem ligação com o texto."
    for binding in bindings:
        matches = list(re.finditer(binding["pattern"], changed))
        assert matches, "Ligação não encontrou o parâmetro no texto."
        for match in reversed(matches):
            value = str(data["params"]["fatia"])
            if "," in match.group(1):
                value = value.replace(".", ",")
            changed = changed[:match.start(1)] + value + changed[match.end(1):]
    target.write_text(changed, encoding="utf-8")
    rejeitar(target, "Premissa consumida")
    target.write_text(original, encoding="utf-8")
    validate_document(target)

    begin, end, table = block(original, RESULT_START, RESULT_END)
    match = re.search(r"\| [^|\n]+ \| ([0-9]+,[0-9]+) \|", table)
    assert match, "Nenhuma célula de resultado encontrada."
    value = float(match.group(1).replace(",", ".")) + 0.0001
    table = table[:match.start(1)] + f"{value:.4f}".replace(".", ",") + table[match.end(1):]
    target.write_text(original[:begin] + table + original[end:], encoding="utf-8")
    rejeitar(target, "Célula publicada")
    target.write_text(original, encoding="utf-8")
    validate_document(target)
    assert source.read_text(encoding="utf-8") == original
    print(f"OK — {source.name}: base, premissa consumida, tabela e restauração; dono intacto.")


def main():
    root = Path(__file__).resolve().parent.parent
    sources = [Path(name) for name in sys.argv[1:]] or [root / "guia-completo.md", root / "emanador-completo.md"]
    with tempfile.TemporaryDirectory(prefix="contrateses-caminhos-") as folder:
        for source in sources:
            conferir(source, Path(folder))
    print("TUDO OK — contraprovas executadas somente em cópias isoladas.")


if __name__ == "__main__":
    main()
