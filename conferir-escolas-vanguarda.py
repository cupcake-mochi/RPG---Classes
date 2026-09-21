"""Comparação marginal do rascunho de Escolas com a Sequência já auditada.

Instrumenta uma cópia em memória do modelo v2, sem modificar sua fonte.
Os valores de movimento/Defesa são convenções herdadas, não dados de mesa.
"""
from pathlib import Path
from dataclasses import replace
import json
import runpy
import sys
import types

ROOT = Path(__file__).resolve().parent
original = runpy.run_path(str(ROOT / 'conferir-vanguarda-v2.py'))
source = (ROOT / 'conferir-vanguarda-v2.py').read_text().split('\ndef audit():')[0]


def change(old, new, count=1):
    global source
    assert source.count(old) == count, (old, source.count(old))
    source = source.replace(old, new)


change('    recoil_value:float=5.40', '    school:str=""\n    school_open_value:float=0.\n    recoil_value:float=5.40')
change("def attack(cfg, pressure=False, condition='', finish='', spell=False):",
       "def attack(cfg, pressure=False, condition='', finish='', spell=False, school_accuracy=False):")
change('base=cfg.p_die-cover*.05+(0.05 if pressure else 0)',
       'base=cfg.p_die-cover*.05+(0.05 if pressure else 0)+(0.05 if school_accuracy else 0)')
change('def v(t,a,n,expiry,used,closed,buff,buff_exp,condition):',
       'def v(t,a,n,expiry,used,closed,buff,buff_exp,condition,school_ready):')
change('n,expiry=-1,-1', 'n,expiry=-1,-1\n                school_ready=False')
change("return v(t+1,0,n,expiry,False,False,buff,buff_exp,'')",
       "return v(t+1,0,n,expiry,False,False,buff,buff_exp,'',school_ready)")
change('return v(t,2,n,expiry,used,closed,buff,buff_exp,condition)',
       'return v(t,2,n,expiry,used,closed,buff,buff_exp,condition,school_ready)')
change('def after(nn=n,ee=expiry,uu=used,cc=closed,bb=buff,be=buff_exp,co=condition):',
       'def after(nn=n,ee=expiry,uu=used,cc=closed,bb=buff,be=buff_exp,co=condition, sr=school_ready if spell else False):')
change('return v(t,a+1,nn,ee,uu,cc,bb,be,co)',
       'return v(t,a+1,nn,ee,uu,cc,bb,be,co,sr)')
change("condition=condition,spell=spell)",
       "condition=condition,spell=spell,school_accuracy=school_ready and not spell)")
change("entry(benefit=damage-baseline,\n                                              opening_loss=",
       "entry(benefit=damage-baseline+p*cfg.school_open_value,\n                                              opening_loss=")
change('scale(after(0,t+2),p)', 'scale(after(0,t+2,sr=cfg.school=="precisao"),p)')
change("condition=condition)\n                    magnitude=",
       "condition=condition,school_accuracy=school_ready)\n                    magnitude=")
change('condition=condition,finish=label)',
       'condition=condition,finish=label,school_accuracy=school_ready)')
change("v(1,0,-1,-1,False,False,'',-1,'')",
       "v(1,0,-1,-1,False,False,'',-1,'',False)")

module = types.ModuleType('escolas_model')
sys.modules[module.__name__] = module
exec(compile(source, '<modelo v2 com escola>', 'exec'), module.__dict__)
Config, day = module.Config, module.day

profiles = [
    Config('corpo_a_corpo', melee=True, weapon_mean=6.5, damage_normal=26.5,
           kokusen=.2, external_explorable=True),
    Config('batedor_referencia', p_die=.65, advantage=True, q_physical=.55,
           q_vigor=.55, movement=12., external_explorable=True,
           weapon_mean=5.5, damage_normal=25.5),
    Config('batedor_extremo', p_die=.95, advantage=True, q_physical=.85,
           q_vigor=.55, movement=12., external_explorable=True,
           weapon_mean=5.5, damage_normal=25.5),
]
scenarios = {'desde_T1': {}, 'desde_T2': {'start_turn': 2},
             'T2_sem_ataque': {'skip_turns': (2,)}}
out = {
    'status': 'Rascunho; preços marginais condicionais, não média observada nem teto universal.',
    'assumptions': [
        '1 fatia = 5.08 equivalentes/rodada; 1 PE = 5.14 equivalentes.',
        'Benefício da escola apenas na abertura acertada; usa a categoria adequada em todos os ataques elegíveis.',
        'Precisão: +1 no próximo ataque elegível; consumido inclusive no erro. Sem bônus em feitiços.',
        'Guarda: +1 Defesa = 3.39 equivalentes por abertura; supõe o benefício integralmente útil.',
        'Empurrar 3m e deslocar 1.5m: 0.60 equivalente/m, multiplicados pela falha do TR Físico; situação sempre útil.',
        'Versado: economia de Movimento avaliada como deslocamento integral. Uso desse gesto para recarga/outras ações não simulado.',
        'O quadro cruza efeitos com todos os perfis para comparação; isso não concede escolas incompatíveis com a arma.',
        'Conserva as limitações do modelo anterior, inclusive condições externas favoráveis para Fixar/Explorar.',
    ],
    'profiles': {},
}
for cfg in profiles:
    # A instrumentação desativada deve reproduzir o modelo aprovado, inclusive atrasos.
    old_cfg = original['Config'](**{k:v for k,v in cfg.__dict__.items()
                                 if k not in ('school', 'school_open_value')})
    rows = {}
    for name, kwargs in scenarios.items():
        baseline = day(cfg, **kwargs)
        old = original['day'](old_cfg, **kwargs)
        for k in original['KEYS']:
            assert abs(baseline[k] - old[k]) < 1e-9, (cfg.name, name, k)
        effects = {
            'precisao': replace(cfg, school='precisao'),
            'guarda': replace(cfg, school_open_value=3.39),
            'empurrar_3m': replace(cfg, school_open_value=1.8*cfg.q_physical),
            'desviar_1_5m': replace(cfg, school_open_value=.9*cfg.q_physical),
            'versado_movimento': replace(cfg, school_open_value=cfg.movement*.6),
        }
        row = {'sem_escola': baseline['net_slices'], 'effects': {}}
        for effect, ecfg in effects.items():
            result = day(ecfg, **kwargs)
            marginal = result['net_slices'] - baseline['net_slices']
            assert marginal >= -1e-9
            row['effects'][effect] = {'net_slices': result['net_slices'],
                                      'incremento': marginal,
                                      'aberturas_acertadas_por_rodada': result['open_hits']/10.5}
        rows[name] = row
    out['profiles'][cfg.name] = rows

out['checks'] = 'Escola desativada reproduz modelo anterior; incrementos não negativos: OK.'
destination = ROOT / 'vanguarda-escolas-contas.json'
destination.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
for profile, rows in out['profiles'].items():
    for name, row in rows.items():
        print(profile, name, 'base=', round(row['sem_escola'], 4),
              {effect: round(data['incremento'], 4) for effect, data in row['effects'].items()})
print(out['checks'])
