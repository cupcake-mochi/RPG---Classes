"""Sensibilidade de Não Cede, mantendo a regra original.

Não estima uma distribuição real de encontros: compara hipóteses explícitas.
Todas as saídas ficam na pasta autorizada. Apenas biblioteca padrão.
"""
from itertools import product
from pathlib import Path
import json

SLICE = 5.08
FAIL = .35
POOL = 4  # maestria no nível 30
ROOT = Path(__file__).resolve().parent


def encounter_pattern(lengths, mode, frequency):
    result = []
    for encounter, length in enumerate(lengths):
        for turn in range(length):
            occurrence = float(turn == 0) if mode == 'one_per_combat' else frequency
            result.append((encounter, occurrence))
    return result


def expected_rerolls(lengths, mode='frequency', frequency=.5,
                     fail=FAIL, pool=POOL, rests=True, tests_per_event=1):
    # Com efeitos idênticos, usar no primeiro fracasso elegível é ótimo.
    # Mais de um teste na rodada continua permitindo só uma rerrolagem.
    state = {pool: 1.}
    used = 0.
    previous = -1
    for encounter, occurrence in encounter_pattern(lengths, mode, frequency):
        if rests and encounter != previous:
            state = {pool: 1.}
        previous = encounter
        trigger = occurrence * (1 - (1 - fail)**tests_per_event)
        following = {}
        for remaining, probability in state.items():
            spent = probability * trigger if remaining else 0.
            if spent:
                following[remaining-1] = following.get(remaining-1, 0.) + spent
            following[remaining] = following.get(remaining, 0.) + probability-spent
            used += spent
        state = following
    assert abs(sum(state.values())-1.) < 1e-10
    return used


def evaluate(difference, **kwargs):
    # 3 combates de 3 ou 4 rodadas com igual peso: 10,5 rodadas esperadas.
    schedules = tuple(product((3,4), repeat=3))
    uses = sum(expected_rerolls(lengths, **kwargs) for lengths in schedules)/len(schedules)
    fail = kwargs.get('fail', FAIL)
    success = 1-fail
    # O +1 abaixo supõe faixa linear do d20, sem vantagem ou desvantagem.
    success_plus = min(1., success+.05)
    recovered = uses*success
    total = recovered*difference
    original = total/10.5/SLICE
    plus_one = uses*success_plus*difference/10.5/SLICE
    # Alternativa não adotada: mover 3 m após passar NA RERROLAGEM.
    movement = recovered*3*.6/10.5/SLICE
    return {'rerolls_per_day': uses, 'successful_rerolls_per_day': recovered,
            'avoided_equivalents_per_day': total, 'original_slices': original,
            'with_plus_one_slices': plus_one, 'plus_one_increment': plus_one-original,
            'move_3m_increment': movement}


output = {'status': 'Sensibilidade; frequências hipotéticas, não média de mesa.',
          'rules': 'Qualquer TR falhado, segundo resultado, maestria usos/descanso curto, no máximo um/rodada.',
          'constants': {'slice': SLICE, 'failure_probability': FAIL,
                        'mastery_at_30': POOL, 'rounds_per_day': 10.5},
          'scenarios': {}}

specs = [
    ('73_dano_um_TR_por_combate', 73/2, {'mode':'one_per_combat'}),
    ('73_dano_TR_em_metade_das_rodadas', 73/2, {}),
    ('73_dano_um_TR_por_rodada', 73/2, {'frequency':1.}),
    ('73_dano_dois_TR_por_rodada', 73/2, {'frequency':1., 'tests_per_event':2}),
    ('73_dano_metade_rodadas_sem_descanso_curto', 73/2, {'rests':False}),
    ('67_dano_metade_rodadas', 67/2, {}),
    ('167_dano_metade_rodadas', 167/2, {}),
    ('182_5_dano_metade_rodadas', 182.5/2, {}),
    ('perda_hipotetica_78_75_metade_rodadas', 78.75, {}),
]
for name, difference, options in specs:
    output['scenarios'][name] = {'difference_success_failure': difference,
                                 'options': options, **evaluate(difference, **options)}

reference = output['scenarios']['73_dano_TR_em_metade_das_rodadas']
assert abs(reference['original_slices'] - .5*.35*.65*(73/2)/SLICE) < 1e-12
assert abs(expected_rerolls((4,), frequency=1.) - 4*FAIL) < 1e-12
assert expected_rerolls((4,4,4), frequency=1., rests=False) <= 4
assert evaluate(0)['original_slices'] == 0
assert evaluate(73/2, fail=0)['original_slices'] == 0
assert evaluate(73/2, fail=1)['original_slices'] == 0
assert evaluate(73/2, pool=0)['original_slices'] == 0
assert evaluate(73/2, frequency=1., tests_per_event=2)['original_slices'] < 2*evaluate(73/2, frequency=1.)['original_slices']
output['checks'] = 'Gatilho de falha, limite por rodada, reserva de usos e diferença entre sucesso/falha: OK.'
output['proposed_budget'] = {'base_approved':2.75, 'nao_cede_proposed':1.,
                             'combined_if_accepted':3.75, 'remaining_if_accepted':1.25}
(ROOT/'vanguarda-nao-cede-contas.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
for name, row in output['scenarios'].items():
    print(name, 'original=',round(row['original_slices'],4),
          'com +1=',round(row['with_plus_one_slices'],4),
          'incremento=',round(row['plus_one_increment'],4),
          'usos/dia=',round(row['rerolls_per_day'],4))
print(output['checks'])
