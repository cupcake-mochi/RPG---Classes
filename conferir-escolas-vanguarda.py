"""Escola de Arma na Sequência vigente (v3), com preços líquido e bruto.

L cobra o PE da Condução; Br permite o gasto real de PE, mas não o desconta
na avaliação do benefício. Br é a contabilidade adotada para o Caminho.
O cruzamento das cinco opções com cada perfil serve para comparar magnitudes;
não autoriza uma Manha em categoria de arma incompatível.
"""
from dataclasses import replace
from pathlib import Path
import json
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parent
model = runpy.run_path(str(ROOT/'conferir-vanguarda-v3.py'))
Config, day, PE_RATE = model['Config'], model['day'], model['PE_RATE']
v3 = json.loads((ROOT/'vanguarda-contas-v3.json').read_text())
pe = json.loads((ROOT/'vanguarda-pe-contas.json').read_text())
doc = ROOT/'vanguarda-escolas-rascunho.md'
text = doc.read_text()

def numero(padrao):
    match = re.search(padrao, text)
    assert match, f'Fonte da Escola ausente: {padrao}'
    return float(match.group(1).replace(',','.'))

POSTURA = numero(r'\+1 Defesa = (\d+,\d+) equivalentes')
METRO = numero(r'movimento = (\d+,\d+) equivalente/m')
EMPUXO_METROS = numero(r'\*\*Empuxo\*\* \|[^\n]*?até (\d+) m')
MOVER_METROS = numero(r'\*\*Mover Alvo\*\* \|[^\n]*?até (\d+,\d+) m')
assert METRO > 0 and POSTURA > 0 and EMPUXO_METROS > 0 and MOVER_METROS > 0

profiles = {}
for name in ('yumi_referencia','lamina_longa','lamina_curta'):
    cfg = Config(**v3['profiles'][name]['params'])
    profiles[name] = replace(cfg, school='', school_open_value=0., capstone=False)
scenarios = {'desde_T1':{}, 'desde_T2':{'start_turn':2},
             'T2_sem_ataque':{'skip_turns':(2,)}}


def options(cfg):
    return {
        'ritmo':replace(cfg, school='precisao'),
        'postura_firme':replace(cfg, school_open_value=POSTURA),
        'empuxo':replace(cfg, school_open_value=EMPUXO_METROS*METRO*cfg.q_physical),
        'mover_alvo':replace(cfg, school_open_value=MOVER_METROS*METRO*cfg.q_physical),
        'versado':replace(cfg, school_open_value=cfg.movement*METRO),
    }


def medir(cfg, kwargs, rate):
    return day(cfg,pe_rate=rate,**kwargs)

out = {
    'status':'Modelo v3 vigente; L desconta PE, Br não desconta PE e é a contabilidade adotada. Perfis cruzados não concedem escolhas ilegais de arma.',
    'fontes':{'modelo':'conferir-vanguarda-v3.py',
              'precos':'vanguarda-escolas-rascunho.md',
              'perfis':'vanguarda-contas-v3.json',
              'ancora_bruta':'vanguarda-pe-contas.json'},
    'perfis':{},
}
for name,cfg in profiles.items():
    out['perfis'][name] = {}
    for scenario,kwargs in scenarios.items():
        rows = {}
        for label,rate in [('L',PE_RATE),('Br',0.)]:
            base = medir(cfg,kwargs,rate)
            effects = {}
            for effect,ecfg in options(cfg).items():
                result = medir(ecfg,kwargs,rate)
                marginal = result['net_slices']-base['net_slices']
                assert marginal >= -1e-9, (name,scenario,label,effect,marginal)
                effects[effect] = {'total_fatias':result['net_slices'],
                                   'acrescimo_fatias':marginal,
                                   'golpes_iniciais_dia':result['open_hits']}
            rows[label] = {'sem_escola_fatias':base['net_slices'],
                           'effects':effects}
        out['perfis'][name][scenario] = rows
        print(name,scenario,'OK',flush=True)

# O mesmo perfil sem Escola reproduz os dois donos atuais, cada qual em sua
# contabilidade. O antigo validador v2 não participa desta regressão.
ref = out['perfis']['yumi_referencia']['desde_T1']
assert abs(ref['L']['sem_escola_fatias'] -
           v3['sequence_without_school']['sem_nivel_30']['net_slices']) < 1e-9
assert abs(ref['Br']['sem_escola_fatias'] -
           pe['perfis']['distancia']['etapas']['sequencia']['acumulado']['Br']) < 1e-9

# Confere a tabela do documento dono sem esconder uma mudança em fonte,
# política, parâmetro ou valor publicado.
lines = ['| Yumi de referência, desde T1 | Líquido | Bruto |','|---|---:|---:|']
def line(label,l,b):
    lines.append(f'| {label} | {l:.6f} | {b:.6f} |'.replace('.',','))
line('Sem Escola',ref['L']['sem_escola_fatias'],ref['Br']['sem_escola_fatias'])
for effect,label in [('ritmo','Ritmo'),('postura_firme','Postura Firme'),
                     ('empuxo','Empuxo'),('mover_alvo','Mover Alvo'),
                     ('versado','Versado')]:
    line(label+' — acréscimo',ref['L']['effects'][effect]['acrescimo_fatias'],
         ref['Br']['effects'][effect]['acrescimo_fatias'])
start,end='<!-- inicio-contas-escola-v3 -->','<!-- fim-contas-escola-v3 -->'
assert text.count(start)==text.count(end)==1
published=text.split(start)[1].split(end)[0]
calculated='\n'+'\n'.join(lines)+'\n'
if sys.argv[1:]==['--publicar']:
    doc.write_text(text.replace(start+published+end,start+calculated+end))
elif not sys.argv[1:]:
    assert published==calculated, 'Tabela da Escola v3 diverge dos valores atuais; revisar a fonte alterada'
else:
    raise SystemExit('Uso: conferir-escolas-vanguarda.py [--publicar]')
out['checks']='v3 atual, regressão L/Br dos donos e tabela publicada: OK.'
(ROOT/'vanguarda-escolas-contas.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(out['checks'],flush=True)
