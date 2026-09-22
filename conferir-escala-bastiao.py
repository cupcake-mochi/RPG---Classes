"""Decisão de 21/09: escala com acerto, pra Fagulha, Trocação Franca e Retaliação.

Fagulha (correção histórica, conferir-fagulha.py) e Retaliação (Combatente
Amaldiçoado, nível 2) já usavam 50% de acerto no Classe 0. Trocação Franca
(Punho, nível 2) usava dano cru (11,50 x 0,75, sem acerto) — a mesma reforma,
duas escalas. Critério do Mizuki: qual escala fecha melhor a fatia de 5:00
nas DUAS Trilhas que a tensão toca. Fonte dos outros degraus:
bastiao-reforma/reforma-caminhos-continuidade.md (livro-caixa do Punho e da
Brasa/Combatente Amaldiçoado).
"""
from fractions import Fraction as F

FATIA = F(508, 100)
DANO_SOCO = F(1150, 100)      # d10 + Força 6, nível 30
GATILHO = F(75, 100)          # >=1 de 2 ataques acerta
ACERTO = F(1, 2)
SOCO_REACAO = F(65, 100)      # não muda com a escala
PUNHO_11, PUNHO_19 = F(91, 100), F(51, 100)
PUNHO_27_BAIXO, PUNHO_27_ALTO = F(68, 100), F(135, 100)

DIA, USOS_DIA, FORCA, PE_DANO, DANO_C0 = F(21, 2), F(6), F(6), F(514, 100), F(27)
COMB_11, COMB_19, COMB_27 = F(118, 100), F(173, 100), F(50, 100)


def trocacao_franca(cru):
    return DANO_SOCO * GATILHO * (1 if cru else ACERTO) / FATIA


def retaliacao(cru):
    base = DANO_C0 * (1 if cru else ACERTO) * USOS_DIA / DIA
    pe_max = FORCA * PE_DANO / DIA
    return (base + pe_max) / FATIA


def punho_total(cru):
    nv2 = trocacao_franca(cru) + SOCO_REACAO
    return nv2, (nv2 + PUNHO_11 + PUNHO_19 + PUNHO_27_BAIXO,
                 nv2 + PUNHO_11 + PUNHO_19 + PUNHO_27_ALTO)


def combatente_total(cru):
    nv2 = retaliacao(cru)
    tres = nv2 + COMB_11 + COMB_19
    return nv2, tres, tres + COMB_27


output = {'decisao': 'com acerto, adotada para as tres', 'punho': {}, 'combatente_amaldicoado': {}}
print('Punho (Trocação Franca):')
for cru in (True, False):
    nv2, (baixo, alto) = punho_total(cru)
    output['punho']['cru' if cru else 'com_acerto'] = {
        'trocacao_franca': float(trocacao_franca(cru)), 'nv2_total': float(nv2),
        'caminho_baixo': float(baixo), 'caminho_alto': float(alto)}
    print(f"  {'cru' if cru else 'com acerto':10s} Trocação Franca {float(trocacao_franca(cru)):.2f}  "
          f"nv2 {float(nv2):.2f}  total {float(baixo):.2f}-{float(alto):.2f} de 5,00")

print('\nCombatente Amaldiçoado (Retaliação):')
for cru in (True, False):
    nv2, tres, total = combatente_total(cru)
    output['combatente_amaldicoado']['cru' if cru else 'com_acerto'] = {
        'retaliacao': float(nv2), 'tres_primeiros_degraus': float(tres), 'total': float(total)}
    print(f"  {'cru' if cru else 'com acerto':10s} Retaliação {float(nv2):.2f}  "
          f"3 primeiros degraus {float(tres):.2f}  total {float(total):.2f} de 5,00")

# Contra-teste: prova que a alternativa rejeitada (cru) faz o Combatente
# Amaldiçoado estourar mais que qualquer peça já aceita no projeto (o pior
# aceito hoje é a própria Brasa em 5,51; cru levaria a mais de 7).
_, _, cru_total = combatente_total(True)
_, _, aceito_total = combatente_total(False)
assert cru_total > F(7)
assert aceito_total < cru_total - F(1)
# E prova que com acerto no Punho não quebra a Trilha: fica com margem, não estoura.
_, (baixo_ca, alto_ca) = punho_total(False)
assert alto_ca < F(5)
assert baixo_ca > F(3)

output['checks'] = ('Cru faz o Combatente Amaldiçoado passar de 7,00 (pior estouro do projeto); '
                     'com acerto no Punho fica com margem, sem quebrar a Trilha: OK.')
print(output['checks'])

from pathlib import Path
import json
(Path(__file__).resolve().parent / 'escala-bastiao-contas.json').write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + '\n')
