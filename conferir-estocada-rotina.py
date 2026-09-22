"""A rotina da Vanguarda com a conjuração no lugar: o Caminho e a Estocada
medidos numa ficha que conjura quantas vezes a régua do repositório principal
diz que ela conjura.

POR QUE ESTE ARQUIVO FOI REFEITO (21/09, noite). A primeira versão comparava a
Estocada com uma Vanguarda que NUNCA conjura, e cobrava o PE do feitiço a 5,14
por ponto. Deu "Compasso nunca vence a arma pura" -- e estava errado duas vezes:
  1. A base estava errada. O conferir-orcamento.py do repositório principal
     (bloco 1) calcula conjurações por dia = PE do Caminho x nível // custo do
     maior feitiço, e a peça 6 publica "Vanguarda conjura 67% das rodadas no
     nível 30"; o ataque extra do nível 7 é preçado nas rodadas que sobram.
     Uma Vanguarda que nunca conjura joga 150 PE fora.
  2. O preço do PE era circular. O 5,14 saiu dos próprios feitiços
     (DESENHO-trilhas.md: "gastar PE para ter dano é sempre mais ou menos zero
     por definição"), então cobrar o feitiço a 5,14 faz qualquer feitiço valer
     zero -- e aí o otimizador nunca conjura. O PE do dia é um orçamento de
     conjurações, não um preço.
O que o Compasso muda não é "conjurar ou atacar": é ter um ataque de arma nas
rodadas em que você já ia conjurar. É isso que se mede aqui.

COMO SE MEDE. O feitiço é o mesmo e é conjurado o mesmo número de vezes nos
dois lados; o valor dele se cancela. Mede-se o lado da arma. As rodadas de
conjuração: sem Compasso, a rodada inteira não tem ataque (desde a v0.147 o
ataque extra exige a Ação de Atacar); com Compasso, só o primeiro ataque some e
o segundo é o de bônus, com acesso normal à Sequência. O jogador escolhe em que
rodadas conjura; toma-se a melhor posição de cada luta. PE da Condução em bruto
(decisão de 21/09, vanguarda-orcamento.md).

DUAS IMPLEMENTAÇÕES, QUE TÊM DE CONCORDAR.
  A -- o próprio v3 (via o loader do nv23, com Escola, Persistência e
       Conclusão Dupla), remendado com uma "meia rodada" pro Compasso.
  B -- um modelo novo, mais curto, que também faz as conclusões mágicas, Bote
       e Ferrão, que o v3 não tem.
Nas duas, Compasso sobre a Sequência sozinha dá o mesmo número (assert).
"""
from pathlib import Path
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import combinations
import json
import math
import runpy
import re
import sys

ROOT = Path(__file__).resolve().parent
SLICE, DAY, PE_RATE = 5.08, 10.5, 5.14

# Conjurações por dia, pelo método do conferir-orcamento.py (bloco 1):
PE_POR_NIVEL_VANGUARDA = 5      # peça 6: "5 na Vanguarda e no Guia"
NIVEL = 30
MAIOR_CLASSE_NV30 = 7           # conferir-orcamento.py, maior_classe(30)
CUSTO_FEITICO = 3 * MAIOR_CLASSE_NV30   # peça 1: um feitiço custa 3 x Classe
CONJURACOES_DIA = (PE_POR_NIVEL_VANGUARDA * NIVEL) // CUSTO_FEITICO   # 150 // 21 = 7

NAO_CEDE = json.loads((ROOT / 'vanguarda-nao-cede-contas.json').read_text())[
    'scenarios']['73_dano_TR_em_metade_das_rodadas']['original_slices']
PE_CONTAS = json.loads((ROOT / 'vanguarda-pe-contas.json').read_text())


# ---------------------------------------------------------------- A: v3 remendado
nv23 = ROOT / 'conferir-vanguarda-nv23.py'
_loader = nv23.read_text().split("result={'status':")[0]
for old, new in (
        ("'    slow_from_turn:int=1\\n    recovery:bool=False'",
         "'    slow_from_turn:int=1\\n    recovery:bool=False\\n    recovery_uses:int=1'"),
        ('cfg.recovery and not recovery_spent and cfg.break_on_miss',
         'cfg.recovery and recovery_spent < cfg.recovery_uses and cfg.break_on_miss'),
        ('be=be,rs=True', 'be=be,rs=recovery_spent+1')):
    assert _loader.count(old) == 1, old
    _loader = _loader.replace(old, new)
_meia_rodada = (
    "change('def solve(cfg, turns, pe_rate=PE_RATE, start_turn=1, skip_turns=(),',\n"
    "       'def solve(cfg, turns, pe_rate=PE_RATE, start_turn=1, skip_turns=(), half_turns=(),')\n"
    "change('        if t in skip_turns:\\n',\n"
    "       '        if t in half_turns and a==0:\\n'\n"
    "       '            return v(t,1,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent,recovery_spent)\\n'\n"
    "       '        if t in skip_turns:\\n')\n")
assert _loader.count('module=types.ModuleType') == 1
_loader = _loader.replace('module=types.ModuleType', _meia_rodada + 'module=types.ModuleType')
NS = {'__file__': str(nv23)}
exec(compile(_loader, '<nv23 + meia rodada>', 'exec'), NS)
A_solve, REFERENCIA, MELEE = NS['solve'], NS['reference'], NS['melee']
attack = NS['module'].attack
condition_value = NS['module'].condition_value
resistance_outcomes = NS['module'].resistance_outcomes
available_finishes = NS['module'].available_finishes
CONDUCTS = NS['module'].CONDUCTS


def _mistura(casts_per_day):
    """Três lutas de 3 ou 4 turnos com peso igual; conjurações por luta em
    mistura de piso e teto que dá casts_per_day no dia."""
    m = casts_per_day / 3
    lo = math.floor(m)
    w = m - lo
    for turns in (3, 4):
        for b, wt in ((lo, 1 - w), (lo + 1, w)):
            if wt:
                yield turns, min(b, turns), wt / 2 * 3


def A_dia(cfg, casts_per_day, compasso, pe_rate=0.):
    tot = 0.
    for turns, b, peso in _mistura(casts_per_day):
        best = None
        for pos in combinations(range(1, turns + 1), b):
            kw = {'half_turns': pos} if compasso else {'skip_turns': pos}
            r = A_solve(cfg, turns, pe_rate, **kw)
            s = r['benefit'] - r['opening_loss'] - pe_rate * r['pe']
            best = s if best is None or s > best else best
        tot += best * peso
    return tot / DAY / SLICE


def A_ataque_de_bonus_cru(cfg, casts_per_day):
    """O benefit do v3 é relativo ao ataque simples de cada slot; o ataque que o
    Compasso cria não tem slot equivalente sem ele, então o dano dele entra à parte."""
    _, dano = attack(cfg)
    return casts_per_day * dano / DAY / SLICE


# ---------------------------------------------------------------- B: modelo novo
@dataclass(frozen=True)
class Config(NS['Config']):
    sequencia: bool = True
    compasso: bool = False
    magicas: bool = False
    bote: bool = False
    ferrao: bool = False
    classe0: float = 27.


KEYS = ('value', 'opening_loss', 'pe', 'casts', 'bonus_attacks', 'magic_finishes',
        'conduct_attempts', 'finish_attempts')
ZERO = (0.,) * len(KEYS)


def _e(**kw):
    return tuple(kw.get(k, 0.) for k in KEYS)


def _add(*vs):
    return tuple(sum(x) for x in zip(*vs))


def _sc(v, w):
    return tuple(x * w for x in v)


# Mesmas magnitudes de conferir-estocada-conclusoes-magicas.py (mecânica de 21/09).
_PP, _M, _IMP = .230, .60, 132.15
MAGICAS = {
    'cortar_a_resposta': (25 * _PP, True, 2),
    'expor_a_guarda': (25 * _PP, True, 2),
    'romper_fileira': (12 * _M, True, 1),
    'refluxo': (1 * PE_RATE, False, 1),
    'desorientar': (25 * _PP, False, 1),
    'ancorar': (_IMP - _IMP / 1.10, True, 2),
}


def _melhor_magica(n):
    ops = [(k, m * (.55 if tr else 1.)) for k, (m, tr, req) in MAGICAS.items() if n >= req]
    return max(ops, key=lambda o: o[1]) if ops else (None, 0.)


def B_solve(cfg, turns, casts, pe_rate=0.):
    cost = (cfg.mastery + 1) // 2 + 1
    p_spell, _ = attack(cfg, spell=True)
    _, e_c0 = attack(replace(cfg, spell_damage=cfg.classe0), spell=True)

    def score(v):
        return v[0] - v[1] - pe_rate * v[2]

    def best(ch):
        return max(ch, key=lambda v: (score(v), -v[2], -v[1]))

    @lru_cache(None)
    def end_turn(t, c, n, e, b, be):
        if e <= t:
            n, e = -1, -1
        if be <= t:
            b, be = '', -1
        return turn(t + 1, c, n, e, b, be)

    @lru_cache(None)
    def slot(t, c, n, expiry, used, closed, buff, buff_exp, cond, left, plain):
        active = buff if buff_exp >= t else ''

        def after(nn=n, ee=expiry, uu=used, cc=closed, bb=buff, be=buff_exp, co=cond):
            if left > 1:
                return slot(t, c, nn, ee, uu, cc, bb, be, co, left - 1, plain)
            return end_turn(t, c, nn, ee, bb, be)

        p, damage = attack(cfg, pressure=active == 'pressionar', condition=cond)
        ch = [_add(_e(value=damage), after())]
        if plain or not cfg.sequencia:
            return best(ch)
        if n < 0 and not closed:
            ch.append(_add(_e(value=damage, opening_loss=p * cfg.opening_mean_loss),
                           _sc(after(0, t + 2), p), _sc(after(), 1 - p)))
        if n >= 0 and not used:
            for lab in CONDUCTS:
                if lab == 'explorar' and not cfg.external_explorable:
                    continue
                bb, be = (buff, buff_exp) if lab == active else ('', -1)
                pp, dd = attack(cfg, pressure=bb == 'pressionar' and be >= t, condition=cond)
                mag = {'angulo': 1.8, 'proteger': cfg.protect_value, 'acompanhar': cfg.movement / 2 * .6,
                       'fechar': cfg.recoil_value * cfg.q_physical}.get(lab, 0.)
                hit = after(min(2, n + 1), t + 2, True, bb=lab, be=t + 1)
                miss = after(-1, -1, True, bb=bb, be=be) if cfg.break_on_miss else after(uu=True, bb=bb, be=be)
                ch.append(_add(_e(value=dd + pp * mag, pe=cost, conduct_attempts=1),
                               _sc(hit, pp), _sc(miss, 1 - pp)))
            for lab in available_finishes(cfg, n, t):
                fin = (lab,)
                pp, dd = attack(cfg, pressure=active == 'pressionar', condition=cond, finishes=fin)
                total = _sc(after(-1, -1, True, True), 1 - pp)
                imm = dd
                for prob, eff in resistance_outcomes(cfg, fin, active == 'explorar'):
                    nc = tuple(sorted(set(cond) | ({'fixar', 'derrubada'} & set(eff))))
                    imm += pp * prob * condition_value(eff, cfg)
                    total = _add(total, _sc(after(-1, -1, True, True, co=nc), pp * prob))
                ch.append(_add(_e(value=imm, finish_attempts=1), total))
        return best(ch)

    @lru_cache(None)
    def turn(t, c, n, e, b, be):
        if t > turns:
            return ZERO
        ops = []
        if c < turns - t + 1:
            ops.append(slot(t, c, n, e, False, False, b, be, (), 2, False))
        if c > 0:
            k = (2 if cfg.bote else 1) if cfg.compasso else 0
            if k == 0:
                ops.append(_add(_e(casts=1), end_turn(t, c - 1, n, e, b, be)))
            else:
                ops.append(_add(_e(casts=1, bonus_attacks=k), slot(t, c - 1, n, e, False, False, b, be, (), k, False)))
                if cfg.magicas and n >= 0:
                    nome, comp = _melhor_magica(n)
                    if nome:
                        val = p_spell * comp
                        if cfg.ferrao and not cfg.bote:   # Bote e Ferrão não no mesmo turno
                            p_hit, _ = attack(cfg)
                            val += p_spell * p_hit * e_c0
                        ops.append(_add(_e(casts=1, bonus_attacks=k, magic_finishes=1, value=val),
                                        slot(t, c - 1, -1, -1, True, True, b, be, (), k, True)))
        return best(ops)

    r = dict(zip(KEYS, turn(1, casts, -1, -1, '', -1)))
    r['score'] = score(tuple(r[k] for k in KEYS))
    return r


def B_dia(cfg, casts_per_day, pe_rate=0.):
    tot = {k: 0. for k in KEYS + ('score',)}
    for turns, b, peso in _mistura(casts_per_day):
        r = B_solve(cfg, turns, b, pe_rate)
        for k in tot:
            tot[k] += r[k] * peso
    return tot


def f(x):
    return x / DAY / SLICE


def audit():
    out = {'conjuracoes_dia': CONJURACOES_DIA}
    assert CONJURACOES_DIA == 7

    yumi = Config('yumi_referencia', p_die=.65, advantage=True, q_physical=.55, q_vigor=.55,
                  movement=12., weapon_mean=5.5, damage_normal=25.5, external_explorable=True,
                  break_on_miss=True)
    lamina = Config('lamina_longa', melee=True, weapon_mean=6.5, damage_normal=26.5, kokusen=.2,
                    external_explorable=True, break_on_miss=True, q_physical=.55, q_vigor=.55)

    # Regressão 1 (modelo B): sem conjurar nunca, o valor da Sequência dá o já medido.
    # Os dois alvos vêm do documento dono (vanguarda-pe-contas.json), não escritos aqui:
    # perturbar o JSON tem de acender esta checagem.
    seq = PE_CONTAS['perfis']['distancia']['etapas']['sequencia']['acumulado']
    for rate, alvo in ((PE_RATE, seq['L']), (0., seq['Br'])):
        v = f(B_dia(yumi, 0, rate)['score'] - B_dia(replace(yumi, sequencia=False), 0, rate)['score'])
        assert abs(v - alvo) < 1e-12, (rate, v, alvo)

    # Regressão 2 (modelo A): sem conjurar nunca, o Caminho completo dá o 5,07 e o 1,34
    # que vanguarda-pe-contas.json registra.
    ref_caminho = replace(REFERENCIA, recovery=True, recovery_uses=3, capstone=True)
    mel_caminho = replace(MELEE, recovery=True, recovery_uses=3, capstone=True)
    for cfg, chave in ((ref_caminho, 'distancia'), (mel_caminho, 'corpo_a_corpo')):
        v = A_dia(cfg, 0, False) + NAO_CEDE
        alvo = PE_CONTAS['perfis'][chave]['total_com_nao_cede']['Br']
        assert abs(v - alvo) < 1e-6, (chave, v, alvo)

    # Contra-teste: o erro da primeira versão. Sem rodada de conjuração, o Compasso
    # não tem onde agir -- vale exatamente zero. A base antiga não podia enxergá-lo.
    assert abs(B_dia(replace(yumi, compasso=True), 0)['score'] - B_dia(yumi, 0)['score']) < 1e-9

    # Concordância: Compasso sobre a Sequência sozinha, nas duas implementações.
    seq_A = replace(REFERENCIA, school='')
    comp_A = A_ataque_de_bonus_cru(seq_A, CONJURACOES_DIA) + \
        A_dia(seq_A, CONJURACOES_DIA, True) - A_dia(seq_A, CONJURACOES_DIA, False)
    comp_B = f(B_dia(replace(yumi, compasso=True), CONJURACOES_DIA)['score'] - B_dia(yumi, CONJURACOES_DIA)['score'])
    assert abs(comp_A - comp_B) < 1e-6, (comp_A, comp_B)
    out['concordancia_compasso_so_sequencia'] = {'A_v3_remendado': comp_A, 'B_modelo_novo': comp_B}

    # O Caminho, nos dois cenários.
    caminho = {}
    for nome, cfg in (('distancia', ref_caminho), ('corpo_a_corpo', mel_caminho)):
        linha = {}
        for casts in (0, CONJURACOES_DIA):
            linha[f'{casts}_conjuracoes'] = {
                'sem_compasso': A_dia(cfg, casts, False) + NAO_CEDE,
                'com_compasso': A_dia(cfg, casts, True) + NAO_CEDE,
            }
        base = cfg if nome == 'distancia' else cfg
        linha['compasso_ataque_cru'] = A_ataque_de_bonus_cru(base, CONJURACOES_DIA)
        caminho[nome] = linha
    out['caminho_completo'] = caminho

    # A escada da Estocada (modelo B, sobre a Sequência), 7 conjurações/dia.
    escada = {}
    for nome, cfg in (('distancia', yumi), ('corpo_a_corpo', lamina)):
        def v(**kw):
            return B_dia(replace(cfg, **kw), CONJURACOES_DIA)
        base, comp = v(), v(compasso=True)
        mag = v(compasso=True, magicas=True)
        bote = v(compasso=True, magicas=True, bote=True)
        fer = v(compasso=True, magicas=True, ferrao=True)
        assert abs(comp['casts'] - CONJURACOES_DIA) < 1e-9 and abs(comp['bonus_attacks'] - CONJURACOES_DIA) < 1e-9
        escada[nome] = {
            'compasso_nv2': f(comp['score'] - base['score']),
            'magicas_nv11': f(mag['score'] - comp['score']),
            'magicas_usadas_dia': mag['magic_finishes'],
            'bote_nv19_se_todo_feitico_for_de_condicao': f(bote['score'] - mag['score']),
            'ferrao_nv27': f(fer['score'] - mag['score']),
        }
    out['escada_estocada'] = escada

    print(json.dumps(out, ensure_ascii=False, indent=2))
    (ROOT / 'estocada-rotina-contas.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print('\nTUDO OK — regressões (Sequência 1,26/3,01; Caminho 5,07/1,34), contra-teste da base '
          'antiga, e as duas implementações concordando.')


if __name__ == '__main__' and len(sys.argv)==1:
    audit()


def comparar_orcamento(publicar=False):
    """Cenários de usos de Compasso/Bote no Caminho completo, sem mudar regras."""
    doc = ROOT/'RASCUNHO-orcamento-estocada.md'
    texto = doc.read_text()
    premissas = dict((k,int(v)) for k,v in re.findall(
        r'^\| (orcamento_trilha_fatias|descanso_curto_min|descanso_curto_max) \| (\d+) \|$', texto, re.M))
    assert len(premissas)==3, 'Faltam orçamento e descansos na fonte dos cenários'
    pe_rows = json.loads((ROOT/'estocada-compasso-pe-contas.json').read_text())['orcamento_nivel_30']
    def pe_fatias(rests):
        return next(row['fatias_nominais'] for row in pe_rows if row['descansos_curto_25_porcento']==rests)
    pe_min,pe_max=pe_fatias(premissas['descanso_curto_min']),pe_fatias(premissas['descanso_curto_max'])
    assert pe_min<=pe_max
    scenarios=[]
    for label,c,b in re.findall(r'^\| ([^|]+) \| (0|1|2|sem_teto) \| (0|1|sem_teto) \|$',texto,re.M):
        scenarios.append((label,4 if c=='sem_teto' else int(c),4 if b=='sem_teto' else int(b)))
    assert scenarios and scenarios[0][1:]==(0,0) and len(scenarios)>=4
    assert len({label for label,_,_ in scenarios})==len(scenarios), 'Cenários repetidos no documento'
    cfgs={'distancia':replace(REFERENCIA,recovery=True,recovery_uses=3,capstone=True),
          'corpo_a_corpo':replace(MELEE,recovery=True,recovery_uses=3,capstone=True)}
    scores={};out={'premissas':premissas,'pe_nominal':{'min':pe_min,'max':pe_max},'cenarios':{}}
    for profile,cfg in cfgs.items():
        raw=attack(cfg)[1]
        scores[profile]={}
        for label,climit,blimit in scenarios:
            total=0.;uses=0.;botes=0.
            for turns,casts,weight in _mistura(CONJURACOES_DIA):
                best=None;counts=(0,0)
                for spell_turns in combinations(range(1,turns+1),casts):
                    for ncomp in range(min(climit,casts)+1):
                        for comp_turns in combinations(spell_turns,ncomp):
                            for nbote in range(min(blimit,ncomp)+1):
                                for bote_turns in combinations(comp_turns,nbote):
                                    half=tuple(t for t in comp_turns if t not in bote_turns)
                                    skipped=tuple(t for t in spell_turns if t not in comp_turns)
                                    row=A_solve(cfg,turns,0.,half_turns=half,skip_turns=skipped)
                                    value=row['benefit']-row['opening_loss']+(ncomp+nbote)*raw
                                    if best is None or value>best:
                                        best=value;counts=(ncomp,nbote)
                total+=best*weight;uses+=counts[0]*weight;botes+=counts[1]*weight
            scores[profile][label]={'score':total/DAY/SLICE,'compasso_usos':uses,'bote_usos':botes}
            print('Orçamento:',profile,label,'OK',flush=True)
    baseline_label=scenarios[0][0]
    for profile in cfgs:
        base=scores[profile][baseline_label]['score']
        for label,climit,blimit in scenarios:
            r=scores[profile][label]
            out['cenarios'].setdefault(label,{})[profile]={
                'marginal_fatias':r['score']-base,
                'compasso_usos_dia':r['compasso_usos'],
                'bote_usos_dia':r['bote_usos']}
        owner=json.loads((ROOT/'estocada-rotina-contas.json').read_text())['caminho_completo'][profile]
        assert abs(base+NAO_CEDE-owner['7_conjuracoes']['sem_compasso'])<1e-9
        current=next(label for label,c,b in scenarios if c==4 and b==0)
        target=owner['7_conjuracoes']['com_compasso']+owner['compasso_ataque_cru']-owner['7_conjuracoes']['sem_compasso']
        assert abs(out['cenarios'][current][profile]['marginal_fatias']-target)<1e-9
    lines=[f"| Cenário | Distância | Corpo a corpo | Distância + PE, {premissas['descanso_curto_min']} descanso(s) | Distância + PE, {premissas['descanso_curto_max']} descanso(s) |",
           '|---|---:|---:|---:|---:|']
    def number(n): return f'{n:.6f}'.replace('.',',')
    for label,c,b in scenarios:
        ranged=out['cenarios'][label]['distancia']['marginal_fatias']
        melee=out['cenarios'][label]['corpo_a_corpo']['marginal_fatias']
        lines.append(f'| {label} | {number(ranged)} | {number(melee)} | {number(ranged+pe_min)} | {number(ranged+pe_max)} |')
    def check_block(start,end,generated):
        assert texto.count(start)==texto.count(end)==1
        previous=texto.split(start)[1].split(end)[0]
        expected='\n'+'\n'.join(generated)+'\n'
        if publicar:
            nonlocal_text[0]=nonlocal_text[0].replace(start+previous+end,start+expected+end)
        else:
            assert previous==expected, 'Tabela de orçamento da Estocada diverge do cálculo ou das premissas'
    nonlocal_text=[texto]
    check_block('<!-- inicio-contas-orcamento-estocada -->','<!-- fim-contas-orcamento-estocada -->',lines)
    current=next(label for label,c,b in scenarios if c==4 and b==0)
    full=next(label for label,c,b in scenarios if c==4 and b==4)
    attack_eq=attack(cfgs['distancia'])[1]
    threshold=[]
    for label in (current,full):
        gain=out['cenarios'][label]['distancia']['marginal_fatias']
        for rest,extra in ((premissas['descanso_curto_min'],pe_min),(premissas['descanso_curto_max'],pe_max)):
            required=max(0.,(gain+extra-premissas['orcamento_trilha_fatias'])*DAY*SLICE/CONJURACOES_DIA)
            threshold.append(f'| {label}, {rest} descanso(s) | {number(required)} | {number(required/attack_eq)} |')
    threshold=['| Versão sem limite, PE aproveitado | Alternativa por ação bônus em equivalentes | Fração de um ataque comum |',
               '|---|---:|---:|']+threshold
    out['ataque_comum_equivalentes']=attack_eq
    check_block('<!-- inicio-limiar-orcamento-estocada -->','<!-- fim-limiar-orcamento-estocada -->',threshold)
    if publicar:
        doc.write_text(nonlocal_text[0])
    out['checks']='Regressões do Caminho completo, tabela de cenários e limiares de ação bônus: OK.'
    (ROOT/'estocada-orcamento-cenarios-contas.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(out['checks'],flush=True)


if len(sys.argv)>1:
    if sys.argv[1:]==['--comparar-orcamento']:
        comparar_orcamento()
    elif sys.argv[1:]==['--publicar-cenarios']:
        comparar_orcamento(publicar=True)
    else:
        raise SystemExit('Uso: conferir-estocada-rotina.py [--comparar-orcamento]')
