"""Decisão de 21/09: o preço da Vanguarda conta o PE gasto bruto, sem descontar.

Reproduz a Sequência, a Escola, Persistência (nv23) e Conclusão Dupla (nv30) em
duas contabilidades, para os dois perfis de arma, e soma Não Cede ao total do
Caminho. Não altera nenhuma regra: só muda se o benefício líquido desconta ou
não os 5,14 de dano equivalente por PE gasto.

  L  = líquido: política ótima cobrando 5,14 por PE (benefício - abertura - PE*5,14)
  Br = bruto: política reotimizada com PE de graça na decisão (pe_rate=0);
       o jogador ainda paga o PE em mesa — só não é descontado do preço.

Decisão do Mizuki, 21/09: o preço registrado é Br. Vanguarda de distância
fecha em 5,07 fatias; a diferença entre perfis de arma fica registrada como
pendência aberta, não resolvida por esta conta.
"""
from pathlib import Path
from dataclasses import replace
import json

ROOT = Path(__file__).resolve().parent
NAO_CEDE = json.loads((ROOT/'vanguarda-nao-cede-contas.json').read_text())
NAO_CEDE_SLICES = NAO_CEDE['scenarios']['73_dano_TR_em_metade_das_rodadas']['original_slices']

nv23 = ROOT / 'conferir-vanguarda-nv23.py'
loader = nv23.read_text().split("result={'status':")[0]
old = "'    slow_from_turn:int=1\\n    recovery:bool=False'"
new = "'    slow_from_turn:int=1\\n    recovery:bool=False\\n    recovery_uses:int=1'"
assert loader.count(old) == 1
loader = loader.replace(old, new)
assert loader.count('cfg.recovery and not recovery_spent and cfg.break_on_miss') == 1
loader = loader.replace('cfg.recovery and not recovery_spent and cfg.break_on_miss',
                        'cfg.recovery and recovery_spent < cfg.recovery_uses and cfg.break_on_miss')
assert loader.count('be=be,rs=True') == 1
loader = loader.replace('be=be,rs=True', 'be=be,rs=recovery_spent+1')
ns = {'__file__': str(nv23)}
exec(compile(loader, '<vanguarda-pe: nv23 com contador>', 'exec'), ns)
day, reference, melee = ns['day'], ns['reference'], ns['melee']
SLICE, PE_RATE, DAY = 5.08, 5.14, 10.5


def fatias(x):
    return x / DAY / SLICE


def medir(cfg):
    L = day(cfg)
    Br = day(cfg, pe_rate=0.)
    return {
        'L': fatias(L['benefit'] - L['opening_loss'] - PE_RATE * L['pe']),
        'Br': fatias(Br['benefit'] - Br['opening_loss']),
        'PE_dia_L': L['pe'], 'PE_dia_Br': Br['pe'],
    }


PERFIS = {
    'distancia': (replace(reference, school=''), dict(school='precisao')),
    'corpo_a_corpo': (replace(melee, school_open_value=0.), dict(school_open_value=3.39)),
}

output = {
    'status': 'Decisão de 21/09: preço registrado é o bruto (Br). PE continua custando PE em mesa nos dois casos.',
    'nao_cede_slices': NAO_CEDE_SLICES,
    'perfis': {},
}
for nome, (base, escola) in PERFIS.items():
    passos = [
        ('sequencia', base),
        ('escola', replace(base, **escola)),
        ('persistencia_23', replace(base, **escola, recovery=True, recovery_uses=3)),
        ('conclusao_dupla_30', replace(base, **escola, recovery=True, recovery_uses=3, capstone=True)),
    ]
    linhas = {}
    anterior = None
    for rot, cfg in passos:
        m = medir(cfg)
        marg = {k: m[k] - (anterior[k] if anterior else 0.) for k in ('L', 'Br')}
        linhas[rot] = {'acumulado': m, 'marginal': marg}
        anterior = m
    total_L = anterior['L'] + NAO_CEDE_SLICES
    total_Br = anterior['Br'] + NAO_CEDE_SLICES
    output['perfis'][nome] = {'etapas': linhas, 'total_com_nao_cede': {'L': total_L, 'Br': total_Br}}
    print(nome, 'total L', round(total_L, 4), 'total Br', round(total_Br, 4), flush=True)

# A decisão registra o bruto; confere que ele nunca fica abaixo do líquido
# (PE de graça na decisão nunca piora a política ótima).
for nome, dados in output['perfis'].items():
    assert dados['total_com_nao_cede']['Br'] + 1e-9 >= dados['total_com_nao_cede']['L']

# Achado que motiva registrar a diferença entre perfis como pendência aberta:
# no líquido, o corpo a corpo não usa a Sequência (ela vale zero).
assert output['perfis']['corpo_a_corpo']['etapas']['conclusao_dupla_30']['acumulado']['L'] < 1e-9

output['checks'] = ('Bruto nunca abaixo do líquido; corpo a corpo em líquido reproduz o zero '
                     'da Sequência (o modelo escolhe não usá-la): OK.')
(ROOT / 'vanguarda-pe-contas.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(output['checks'], flush=True)
