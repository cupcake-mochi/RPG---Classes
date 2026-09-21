"""Parcela de PE máximo acrescentada ao Compasso, não preço da habilidade inteira.

Convenções herdadas: 1 PE = 5,14 equivalentes, uma fatia = 5,08 por rodada,
dia de referência com 10,5 rodadas. O cenário com descansos supõe recuperação
de 25%, arredondada para baixo, e espaço no reservatório para aproveitá-la.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
PE_RATE, SLICE, ROUNDS = 5.14, 5.08, 10.5


def compare(level, attribute, short_rests):
    base = 5 * level
    modified = base + attribute
    recovered_before = max(1, base // 4)
    recovered_after = max(1, modified // 4)
    extra_recovery = recovered_after - recovered_before
    extra_available = attribute + short_rests * extra_recovery
    return {
        'nivel': level, 'atributo_escolhido': attribute,
        'descansos_curto_25_porcento': short_rests,
        'pe_maximo_antes': base, 'pe_maximo_depois': modified,
        'recuperacao_antes': recovered_before,
        'recuperacao_depois': recovered_after,
        'recuperacao_extra_por_descanso': extra_recovery,
        'pe_extra_disponivel': extra_available,
        'fatias_nominais': extra_available * PE_RATE / ROUNDS / SLICE,
    }


result = {
    'status': 'Regra de aumento de PE aprovada; precificação apenas desta parcela.',
    'regra': 'Escolha Essência ou Inteligência para Compasso; o mesmo atributo aumenta uma única vez o PE máximo.',
    'premissas': {
        'pe_por_nivel_vanguarda': 5, 'pe_equivalente': PE_RATE,
        'fatia_por_rodada': SLICE, 'rodadas_no_dia': ROUNDS,
        'descanso_curto': '25% do máximo, arredondado para baixo; sem redução por exaustão.',
        'aproveitamento': 'Começa com PE cheio; todo incremento inicial e de recuperação pode ser gasto. Capacidade e recuperação não garantem gasto real.',
        'limite': 'Não mede Compasso inteiro, atributo de ataque, ação bônus, Sequência ou dano das outras entregas.',
    },
    'exemplos': [compare(2, 3, 0), compare(30, 6, 0)],
    'orcamento_nivel_30': [compare(30, 6, n) for n in (0, 1, 2)],
}
(ROOT/'estocada-compasso-pe-contas.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
for row in result['orcamento_nivel_30']:
    print(f"{row['descansos_curto_25_porcento']} descansos: +{row['pe_extra_disponivel']} PE disponíveis, {row['fatias_nominais']:.6f} fatias nominais.")
for row in result['exemplos']:
    print(f"Nível {row['nivel']}, atributo {row['atributo_escolhido']}: {row['pe_maximo_antes']} → {row['pe_maximo_depois']} PE máximos.")
