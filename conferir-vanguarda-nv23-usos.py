"""Compara contadores de Persistência sem alterar a auditoria histórica de 1/cena.

Cada combate começa com todos os usos. Para uma recarga por descanso curto,
isso é um cenário generoso: combates sem descanso compartilham o contador.
"""
from pathlib import Path
from dataclasses import replace
import json

ROOT = Path(__file__).resolve().parent
loader = (ROOT / 'conferir-vanguarda-nv23.py').read_text().split("result={'status':")[0]
old = "'    slow_from_turn:int=1\\n    recovery:bool=False'"
new = "'    slow_from_turn:int=1\\n    recovery:bool=False\\n    recovery_uses:int=1'"
assert loader.count(old) == 1
loader = loader.replace(old, new)
assert loader.count('cfg.recovery and not recovery_spent and cfg.break_on_miss') == 1
loader = loader.replace('cfg.recovery and not recovery_spent and cfg.break_on_miss',
                        'cfg.recovery and recovery_spent < cfg.recovery_uses and cfg.break_on_miss')
assert loader.count('be=be,rs=True') == 1
loader = loader.replace('be=be,rs=True', 'be=be,rs=recovery_spent+1')
ns = {'__file__': str(ROOT / 'conferir-vanguarda-nv23.py')}
exec(compile(loader, '<auditoria nv23 com contador>', 'exec'), ns)
day, solve, reference, melee = [ns[k] for k in ('day', 'solve', 'reference', 'melee')]


def inspect(cfg, duration=None, **kwargs):
    def measure(uses, cap):
        adjusted = replace(cfg, recovery=uses > 0, recovery_uses=uses, capstone=cap)
        row = day(adjusted, **kwargs) if duration is None else solve(adjusted, duration, **kwargs)
        assert row['recoveries'] <= uses * (3 if duration is None else 1) + 1e-8
        assert abs(row['pe'] - row['conduct_attempts'] * ((cfg.mastery+1)//2+1)) < 1e-8
        return row
    rows = {str(u): {str(cap): measure(u, cap) for cap in (False, True)} for u in (0, 1, 2, 3)}
    result = {}
    for u in (1, 2, 3):
        before = rows['0']['False']['net_slices']
        with23 = rows[str(u)]['False']['net_slices']
        with30 = rows['0']['True']['net_slices']
        both = rows[str(u)]['True']['net_slices']
        result[str(u)] = {
            'marginal_23_sem_30': with23-before,
            'marginal_23_com_30': both-with30,
            'marginal_30_apos_23': both-with23,
            'incremento_conjunto_23_30': both-before,
            'usos_esperados_com_30': rows[str(u)]['True']['recoveries'],
        }
        for cap in (False, True):
            assert rows[str(u)][str(cap)]['net_slices'] >= rows[str(u-1)][str(cap)]['net_slices']-1e-9
    return {'marginais': result, 'dados': rows}


output = {
    'regra': 'Cada erro preservado consome um uso; nenhum acerto, PE ou prazo é recuperado.',
    'recarga_modelada': 'Contador completo em cada combate. Limite superior de disponibilidade para recarga por descanso curto; não presume que descansos efetivamente ocorram.',
    'cases': {},
}
old_results = json.loads((ROOT/'vanguarda-nv23-contas.json').read_text())['cases']
cases = [
    ('referencia', reference, None, {}),
    ('referencia_inicio_T2', reference, None, {'start_turn': 2}),
    ('referencia_T2_sem_ataque', reference, None, {'skip_turns': (2,)}),
    ('cobertura_parcial', replace(reference, cover=2), None, {}),
    ('cobertura_boa', replace(reference, cover=5), None, {}),
    ('sem_requisito_fixar', replace(reference, external_slow=False), None, {}),
    ('versado', replace(reference, school='', school_open_value=7.2), None, {}),
    ('melee_sem_cotacao_PE', melee, None, {'pe_rate': 0.}),
    ('extremo', replace(reference, p_die=.95, q_physical=.85, q_vigor=.85), None, {}),
    ('referencia_6_turnos', reference, 6, {}),
    ('referencia_8_turnos', reference, 8, {}),
]
for name, cfg, duration, kwargs in cases:
    row = inspect(cfg, duration, **kwargs)
    if name in old_results:
        old = old_results[name]
        for key in ('marginal_23_sem_30', 'marginal_23_com_30', 'marginal_30_apos_23', 'incremento_conjunto_23_30'):
            assert abs(row['marginais']['1'][key] - old[key]) < 1e-8, (name, key)
    output['cases'][name] = row
    print(name, json.dumps(row['marginais'], ensure_ascii=False), flush=True)

proof = replace(reference, recovery=True, recovery_uses=3, capstone=True)
assert solve(proof, 2, 0)['double_attempts'] == 0
assert solve(proof, 3, 0, skip_turns=(1, 2), initial_sequence=(2, 2))['double_attempts'] == 0
output['checks'] = 'Regressão com 1 uso, limite do contador, PE sem reembolso, ordem dos valores, requisitos e prazo: OK.'
(ROOT/'vanguarda-nv23-usos-contas.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(output['checks'], flush=True)
