"""Vanguarda: o que cabe em 3 fatias, e o que 5 fatias obriga a declarar.

Não mede nada novo. Lê os valores que os validadores da raiz já imprimiram
(`vanguarda-contas-v3.json`, `vanguarda-nv23-usos-contas.json`,
`vanguarda-nao-cede-contas.json`) e cruza com a régua do repositório
principal: Caminho em 2 · 7 · 15 · 30, 3 fatias, nível 7 de graça
(`referencia-jjk-project/DESENHO-caminhos.md`, linha 5).

Rode DEPOIS dos dez `conferir-*.py` da raiz: são eles que escrevem os JSON.
"""
from pathlib import Path
from itertools import combinations
import json

RAIZ = Path(__file__).resolve().parent.parent
V3 = json.loads((RAIZ/'vanguarda-contas-v3.json').read_text())
U23 = json.loads((RAIZ/'vanguarda-nv23-usos-contas.json').read_text())
NC = json.loads((RAIZ/'vanguarda-nao-cede-contas.json').read_text())

# --- medidos, cada um com o caminho de onde saiu -------------------------
ref23 = U23['cases']['referencia']['marginais']['2']

MEDIDO = {
    'sequencia':  (V3['sequence_without_school']['sem_nivel_30']['net_slices'],
                   'v3 sequence_without_school.sem_nivel_30.net_slices'),
    'base':       (V3['profiles']['yumi_referencia']['sem_nivel_30']['net_slices'],
                   'v3 profiles.yumi_referencia.sem_nivel_30.net_slices'),
    'nao_cede':   (NC['scenarios']['73_dano_TR_em_metade_das_rodadas']['original_slices'],
                   'nao-cede scenarios.73_dano_TR_em_metade_das_rodadas.original_slices'),
    'persist':    (ref23['marginal_23_sem_30'],
                   'nv23-usos cases.referencia.marginais.2.marginal_23_sem_30'),
    'dupla_com23':(ref23['marginal_30_apos_23'],
                   'nv23-usos cases.referencia.marginais.2.marginal_30_apos_23'),
    'dupla_sem23':(V3['profiles']['yumi_referencia']['custo_marginal_fatias'],
                   'v3 profiles.yumi_referencia.custo_marginal_fatias'),
    'persist_com30':(ref23['marginal_23_com_30'],
                   'nv23-usos cases.referencia.marginais.2.marginal_23_com_30'),
    'conjunto':   (ref23['incremento_conjunto_23_30'],
                   'nv23-usos cases.referencia.marginais.2.incremento_conjunto_23_30'),
}
escola = MEDIDO['base'][0] - MEDIDO['sequencia'][0]

# --- reservas do documento vigente (vanguarda-orcamento.md) --------------
RESERVA = {'sequencia':2.00,'escola':0.75,'nao_cede':1.00,'persist':0.25,'dupla':1.00}
NIVEL   = {'sequencia':2,'escola':2,'nao_cede':15,'persist':23,'dupla':30}
ROTULO  = {'sequencia':'Sequência de Combate','escola':'Escola de Arma (4 Manhas ou Versado)',
           'nao_cede':'Não Cede','persist':'Persistência','dupla':'Conclusão Dupla'}
# quem depende da Sequência para existir
PRECISA_SEQ = {'escola','persist','dupla'}

SLOTS_PAGOS_3 = {2,15,30}      # DESENHO-caminhos: 3 fatias em 2, 15 e 30; o 7 é de graça
SLOTS_PAGOS_5 = {2,15,23,30}   # a escada que a releitura supõe


def medido(peca, subconj):
    if peca=='sequencia': return MEDIDO['sequencia'][0]
    if peca=='escola':    return escola
    if peca=='nao_cede':  return MEDIDO['nao_cede'][0]
    if peca=='persist':   return MEDIDO['persist'][0]
    if peca=='dupla':     return MEDIDO['dupla_com23'][0] if 'persist' in subconj else MEDIDO['dupla_sem23'][0]
    raise KeyError(peca)


def linha(*cs): print(' '.join(cs))

# ------------------------------------------------------------------ 1
print('=== 1. Proveniência: todo medido abaixo veio de um JSON de validador ===')
for k,(v,src) in MEDIDO.items():
    print(f'  {k:14s} {v:8.4f}   <- {src}')
print(f'  {"escola":14s} {escola:8.4f}   <- base menos sequencia (v3, dentro do mesmo cenário)')

# contra-teste: as duas decomposições do par 23+30 têm de fechar no mesmo número
a = MEDIDO['persist'][0] + MEDIDO['dupla_com23'][0]
b = MEDIDO['dupla_sem23'][0] + MEDIDO['persist_com30'][0]
assert abs(a-MEDIDO['conjunto'][0])<1e-9 and abs(b-MEDIDO['conjunto'][0])<1e-9, (a,b)
print(f'  contra-teste: 23-depois-30 = {a:.4f} e 30-depois-23 = {b:.4f}; conjunto publicado = {MEDIDO["conjunto"][0]:.4f}  OK')
assert abs(sum(RESERVA.values())-5.00)<1e-9
print('  contra-teste: as cinco reservas somam 5,00 como o documento vigente diz  OK')

# ------------------------------------------------------------------ 2
print()
print('=== 2. A proposta de hoje: reserva contra medido ===')
print(f'{"peça":38s} {"nv":>3s} {"reserva":>8s} {"medido":>8s} {"margem":>8s}')
tot_r=tot_m=0.
for k in ('sequencia','escola','nao_cede','persist','dupla'):
    m = medido(k,{'persist'})
    tot_r+=RESERVA[k]; tot_m+=m
    print(f'{ROTULO[k]:38s} {NIVEL[k]:3d} {RESERVA[k]:8.2f} {m:8.4f} {RESERVA[k]-m:8.4f}')
print(f'{"TOTAL":38s} {"":3s} {tot_r:8.2f} {tot_m:8.4f} {tot_r-tot_m:8.4f}')
print(f'  A releitura inteira, medida, custa {tot_m:.4f} fatias. Reservada, 5,00.')

sem23 = MEDIDO['base'][0] + MEDIDO['nao_cede'][0] + MEDIDO['dupla_sem23'][0]
print(f'  A mesma releitura SEM o nível 23, medida: {sem23:.4f} fatias.')
print(f'  Régua do repositório: 3,00. Diferença: {sem23-3.0:+.4f}.')

# ------------------------------------------------------------------ 3
print()
print('=== 3. Antes do dinheiro, os degraus: 5 peças para 3 vagas pagas ===')
print('  Repositório (DESENHO-caminhos l.5): degraus em 2 · 7 · 15 · 30; o 7 é de graça.')
print(f'  Vagas pagas em 3 fatias: {sorted(SLOTS_PAGOS_3)}   -> {len(SLOTS_PAGOS_3)} vagas')
print(f'  Vagas pagas na releitura: {sorted(SLOTS_PAGOS_5)}  -> {len(SLOTS_PAGOS_5)} vagas')
por_nivel={}
for k in RESERVA: por_nivel.setdefault(NIVEL[k],[]).append(ROTULO[k])
for nv in sorted(por_nivel):
    marca = 'existe' if nv in SLOTS_PAGOS_3 else 'NÃO EXISTE na régua do repositório'
    print(f'   nv{nv:2d} [{marca}]: ' + ' + '.join(por_nivel[nv]))

# ------------------------------------------------------------------ 4
print()
print('=== 4. Busca exaustiva: que subconjuntos cabem em 3,00 ===')
pecas = list(RESERVA)
for moeda in ('reserva','medido'):
    print(f'\n  -- preço em {moeda.upper()} --')
    cabem=[]
    for n in range(len(pecas),0,-1):
        for sub in combinations(pecas,n):
            s=set(sub)
            if (PRECISA_SEQ & s) and 'sequencia' not in s: continue   # nada roda sem a Sequência
            custo = sum(RESERVA[k] for k in s) if moeda=='reserva' else sum(medido(k,s) for k in s)
            if custo <= 3.0+1e-9:
                niveis = {NIVEL[k] for k in s}
                cabem.append((custo, sorted(s), niveis <= SLOTS_PAGOS_3))
    cabem.sort(key=lambda r:-r[0])
    if not cabem: print('    nenhum subconjunto cabe.')
    for custo,s,na_escada in cabem[:8]:
        flag = 'cabe na escada 2·7·15·30' if na_escada else 'PRECISA do nível 23'
        print(f'    {custo:6.4f}  {", ".join(ROTULO[k] for k in s)}   [{flag}]')
    maiores = [r for r in cabem if r[2]]
    if maiores:
        c,s,_ = maiores[0]
        print(f'    -> maior conjunto que cabe E respeita a escada: {c:.4f} = {", ".join(ROTULO[k] for k in s)}')

# ------------------------------------------------------------------ 5
print()
print('=== 5. O que mais mexe no resultado: quantos TR a luta tem (Não Cede) ===')
print('  A reserva de 1,00 do Não Cede sai de UM cenário. Os outros do mesmo script:')
for nome,row in NC['scenarios'].items():
    if not nome.startswith('73_dano'): continue
    v=row['original_slices']
    print(f'    {nome:42s} {v:7.4f} fatias   (total da releitura sem nv23: {MEDIDO["base"][0]+v+MEDIDO["dupla_sem23"][0]:6.4f})')
print('  Nenhum documento do projeto fixa quantos TR uma luta tem.')

print()
print('Conferido: proveniência dos medidos, as duas decomposições do par 23+30, a soma das reservas,')
print('a escada do repositório contra a da releitura e a busca exaustiva nas duas moedas: OK.')


# ------------------------------------------------------------------ 6
print()
print('=== 6. De que build sai o 1,3869 (e o que sobra sem ela) ===')
import runpy
from dataclasses import replace
M = runpy.run_path(str(RAIZ/'conferir-vanguarda-v3.py'))
Config, compare = M['Config'], M['compare']
yumi = Config('yumi',p_die=.65,advantage=True,q_physical=.55,q_vigor=.55,movement=12.,
              weapon_mean=5.5,damage_normal=25.5,external_explorable=True,school='precisao')
mel  = Config('lamina',melee=True,weapon_mean=6.5,damage_normal=26.5,kokusen=.2,
              external_explorable=True,school_open_value=3.39)
print('  O Mirar do Batedor (manual 35, nv11) dá vantagem no próximo tiro E, no Yumi, +2 no acerto.')
print('  O +2 já está dentro do p_die=0,65; a vantagem é o parâmetro advantage.')
print(f'  {"cenário":46s} {"base":>8s} {"total c/ nv30 e Não Cede":>26s}')
for nome,cfg in [('Yumi com Mirar (o que a pasta preçou)', replace(yumi)),
                 ('o mesmo Yumi na rodada em que se deslocou', replace(yumi,advantage=False)),
                 ('lâmina longa, do jeito que a pasta rodou', replace(mel)),
                 ('lâmina longa com vantagem de fora e alvo frágil', replace(mel,advantage=True,p_die=.75,q_physical=.55,q_vigor=.55))]:
    c=compare(cfg); base=c['sem_nivel_30']['net_slices']
    print(f'  {nome:46s} {base:8.4f} {base+c["custo_marginal_fatias"]+MEDIDO["nao_cede"][0]:26.4f}')
print('  O Mirar se perde se você se deslocar na rodada (manual 35).')
print('  Nos JSON da pasta, lamina_longa, lamina_curta e estocada_hibrida dão 0,0000 em TODAS as linhas')
print('  contábeis (benefício, perda de abertura, PE, conduções): a política ótima é nunca abrir.')

# ------------------------------------------------------------------ 7
print()
print('=== 7. A escolha de Manha muda o total ===')
versado = V3['profiles']['yumi_versado']
tot_p = MEDIDO['base'][0] + MEDIDO['nao_cede'][0] + MEDIDO['dupla_sem23'][0]
tot_v = versado['sem_nivel_30']['net_slices'] + MEDIDO['nao_cede'][0] + versado['custo_marginal_fatias']
print(f'  com a Manha Precisão: base {MEDIDO["base"][0]:.4f} -> total sem nv23 {tot_p:.4f}  (régua 3,00: {tot_p-3:+.4f})')
print(f'  com Versado:          base {versado["sem_nivel_30"]["net_slices"]:.4f} -> total sem nv23 {tot_v:.4f}  (régua 3,00: {tot_v-3:+.4f})')
print('  A mesma reserva de 0,75 paga as duas, mas medido são 0,1248 e 0,5149.')

# ------------------------------------------------------------------ 8
print()
print('=== 8. Bastião: o que existe de preço ===')
print('  Escada do repositório (DESENHO-caminhos): 2 · 7 · 15 · 30, o 7 de graça -> 3 vagas pagas.')
print('  Escada da releitura (bastiao-nomes-aprovados.md): 2 · 7 · 15 · 23 · 30 -> 4 vagas pagas.')
BAST = [(2,'Olhos Em Mim','substitui Corpo Duro/Absorver','Absorver = 1,60 no repo; Olhos Em Mim sem preço'),
        (7,'Nem Um Arranhão + Ainda de Pé','mantidos','de graça pela régua (correção de base)'),
        (15,'Duro de Matar','era Aparar com Corpo','sem preço aqui; Puxar Para Si nunca foi medido no repo'),
        (23,'Chega Mais','área de 9 m + Provocar ao entrar','sem preço, e sem degrau na escada do repo'),
        (30,'Passa Pra Mim','aliado fica com 1 de vida','sem preço aqui; Segurar nunca foi medido no repo')]
for nv,nome,oq,preco in BAST:
    print(f'   nv{nv:2d} {nome:30s} {oq:34s} {preco}')
print('  Nenhuma das cinco tem número nesta pasta. O único número de Bastião aqui é Fagulha,')
print('  que é entrega de TRILHA (Combatente Amaldiçoado), não do Caminho.')
base_crua = 27*0.56/5.08
vant      = 27*0.25*0.75*0.56/5.08
print(f'   Fagulha na régua com acerto (a correção da pasta): {27*0.50*0.56/5.08+vant:.4f}')
print(f'   Fagulha na régua crua (achado 12 da revisão):      {base_crua+vant:.4f}')
assert abs((base_crua+vant)-3.53)<0.005 and abs((27*0.50*0.56/5.08+vant)-2.05)<0.005
print('   contra-teste: as duas reproduzem 3,53 e 2,05 dos documentos  OK')
print()
print('Seções 6 a 8 conferidas: sensibilidade de build, escolha de Manha e inventário do Bastião: OK.')
