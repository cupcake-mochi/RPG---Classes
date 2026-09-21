"""Auditoria exploratória da Sequência de Combate, 2026-09-18.

Não altera nem importa o repositório de consulta. Sem simulação aleatória.
As unidades de controle são equivalentes da régua publicada, não dano real.
Os preços propostos ainda dependem da decisão do autor.
"""
from collections import defaultdict
from itertools import product
from functools import lru_cache
import json

FATIA = 5.08
PE_EQ = 5.14


def route(turns, attacks, hit, conducts, save_fail=.35, pressure=False,
          adv=False, stop_condition=False):
    """Enumera abrir -> N conduções acertadas -> concluir.

    Uma condução OU conclusão/turno; abertura pode usar qualquer outro ataque.
    Falha ao conduzir mantém o prazo anterior. Prazo t+2, inclusivo.
    Conclusão gasta sequência mesmo na falha e trava reabertura nesse turno.
    Buff Pressionar termina no fim do turno seguinte; refresh só no acerto.
    Contagem do TR é externa: sucesso na condução é acertar, mesmo resistido.
    'stop_condition' só serve para medir um uso de Fixar por combate.
    Retorna frequências e nunca desconta PE de benefício automaticamente.
    """
    # conduções bem sucedidas (-1 = sem sequência), validade, buff, finisher usado
    states = {(-1, -1, -1, False): 1.0}
    totals = defaultdict(float)
    for t in range(1, turns + 1):
        # used: condução/conclusão já declarada neste turno; closed: terminou
        step = {(n, exp, buff, done, False, False): prob
                for (n, exp, buff, done), prob in states.items()}
        for _ in range(attacks):
            nxt = defaultdict(float)
            for (n, exp, buff, done, used, closed), prob in step.items():
                p0 = hit
                p1 = min(.95, hit + .05) if pressure and buff >= t else hit
                p = 1 - (1-p1)**2 if adv else p1
                pb = 1 - (1-p0)**2 if adv else p0
                totals['extra_hit_from_pressure'] += prob * (p-pb)
                if stop_condition and done:
                    kind = 'normal'
                elif n < 0 and not closed:
                    kind = 'open'
                elif n >= 0 and not used:
                    kind = 'conduct' if n < conducts else 'finish'
                else:
                    kind = 'normal'
                totals[kind+'_attempts'] += prob
                totals[kind+'_hits'] += prob*p
                for success, chance in [(True, p), (False, 1-p)]:
                    nn, ee, bb, dd, uu, cc = n, exp, buff, done, used, closed
                    if kind == 'open' and success:
                        nn, ee = 0, t+2
                    elif kind == 'conduct':
                        uu = True
                        if success:
                            nn, ee = n+1, t+2
                            if pressure:
                                bb = t+1
                    elif kind == 'finish':
                        nn, ee, uu, cc, dd = -1, -1, True, True, True
                    nxt[nn, ee, bb, dd, uu, cc] += prob*chance
            step = nxt
        states = defaultdict(float)
        for (n, exp, buff, done, used, closed), prob in step.items():
            if n >= 0 and exp <= t:
                n, exp = -1, -1
            states[n, exp, buff, done] += prob
        assert abs(sum(states.values()) - 1) < 1e-9
    totals['condition_applications'] = totals['finish_hits'] * save_fail
    for kind in ('open', 'conduct', 'finish', 'normal'):
        totals[kind+'_attempts'] += 0
        totals[kind+'_hits'] += 0
    return dict(totals)


def weapon_profile(dice, mod, energy, hit=.55, kokusen=.0, adv=False):
    """Primeiro crítico adicional, sem bônus de trilha ou efeitos pós-crítico.
    A chance de Kokusen é um estado, não uma média do dia (acúmulo existe).
    A energia e o atributo NÃO dobram no crítico. Kokusen multiplica o total.
    """
    w = sum((s+1)/2 for s in dice)
    e = sum((s+1)/2 for s in energy)
    normal = w+mod+e
    critical = (2*w+mod+e)*(1+.5*kokusen)
    p = 1-(1-hit)**2 if adv else hit
    natural20 = 1-.95**2 if adv else .05
    extra19 = (.95**2-.9**2) if adv else .05
    return dict(normal=normal, critical=critical,
                mean_attack=(p-natural20)*normal+natural20*critical,
                impact_gain_per_attempt=extra19*(critical-normal),
                opening_cost_2_per_attempt=2*p,
                opening_cost_half_per_attempt=((p-natural20)*normal+natural20*critical)/2,
                open_then_impact_delta_2=-2*p+p*extra19*(critical-normal))


def optimized_day(lengths, p, q, fixar_cap=None, conduct_value=3.39, opening_cost=2):
    """Modelo agregado otimista para comparar LIMITES, não uma ficha completa.

    Escolhe a cada ataque entre continuar/conduzir/concluir. Desconta a perda
    de dano da abertura, SEM descontar PE. Alvos atendem requisitos externos.
    Toda condução acertada recebe conduct_value, mesmo sem situação útil.
    Toda conclusão recebe ainda -1 ao TR, como se Explorar estivesse ativo:
    isso é uma folga intencional, não permissão para empilhar conduções.
    Ignora Fechar a Rota atual, ataques de oportunidade, modificadores próprios
    das Trilhas e o dano de outros personagens além da régua da peça 19.
    Valores de cobertura/reação aqui não constituem sua precificação final.
    """
    total_turns=sum(lengths)
    boundaries=set()
    pos=0
    for length in lengths:
        pos+=length
        boundaries.add(pos)
    cap=total_turns if fixar_cap is None else fixar_cap
    q=min(1,q+.05)

    @lru_cache(None)
    def v(t, a, n, expiry, used, closed, remaining):
        if t > total_turns:
            return 0.
        if a == 2:
            if t in boundaries or expiry <= t:
                n,expiry=-1,-1
            return v(t+1,0,n,expiry,False,False,remaining)
        def nxt(nn=n,ee=expiry,uu=used,cc=closed,rr=remaining):
            return v(t,a+1,nn,ee,uu,cc,rr)
        choices=[nxt()]
        if n < 0 and not closed:
            choices.append(p*(nxt(0,t+2)-opening_cost)+(1-p)*nxt())
        if n >= 0 and not used:
            if n < 2:
                choices.append(p*(conduct_value+nxt(n+1,t+2,True))
                               +(1-p)*nxt(uu=True))
            # Conclusão inicial: ganho favorável de cobertura disponível.
            finish=3.45
            if n >= 1:
                finish=max(finish,p*q*39.2)
            choices.append(finish+nxt(-1,-1,True,True))
            if n >= 2 and remaining:
                choices.append(p*q*132.15+nxt(-1,-1,True,True,remaining-1))
        return max(choices)
    return v(1,0,-1,-1,False,False,cap)


def audit():
    assert abs(FATIA*5 - 25.4) < 1e-9
    # Regras determinísticas: não se permite conduzir e concluir no mesmo turno.
    for attacks, n, turns, expected in [(2, 0, 1, 1), (2, 1, 1, 0),
                                       (2, 1, 2, 1), (2, 2, 2, 0),
                                       (2, 2, 3, 1), (1, 2, 4, 1)]:
        assert abs(route(turns, attacks, 1, n)['finish_attempts']-expected)<1e-9
    assert route(5, 2, 0, 2)['finish_attempts'] == 0
    # Manual atual. A peça técnica 11 tem uma escada anterior: registrar diferença.
    weapons = {
        'katana_nv2_ref1': ([8], 3, [4], .02),
        'katana_nv30_ref8': ([8], 6, [4]*3, .16),
        'katana_nv30_ref10': ([8], 6, [6]*4, .20),
        'espadao_nv30_ref10': ([12], 6, [6]*4, .20),
        'espadao_kokusen_melhorado_ref10': ([12], 6, [6]*4, 1-.8**2),
        'arco_nv30_lap10': ([10], 6, [6]*4, 0),
        'rifle_nv30_ref10': ([8,8], 0, [6]*4, 0),
    }
    out = {'weapons': {name: weapon_profile(*v[:3], kokusen=v[3])
                       for name, v in weapons.items()}, 'routes': {}}
    # A auditoria usa o teto do efeito, sem desconto por redundância, imunidade,
    # morte/troca do alvo, iniciativa ou requisito externo de Fixar.
    for hit, adv, q, label in [(.50,False,.35,'historico50'),
                              (.55,False,.35,'base55'),
                              (.55,True,.35,'vantagem55'),
                              (.65,True,.55,'batedor65_tr_fraco'),
                              (.95,False,.75,'estresse95')]:
        for n in range(3):
            # 50% combates de três turnos e 50% de quatro: média de 3,5.
            a, b = route(3,2,hit,n,q,adv=adv),route(4,2,hit,n,q,adv=adv)
            avg = {k:(a.get(k,0)+b.get(k,0))/2 for k in a.keys()|b.keys()}
            long = route(120,2,hit,n,q,adv=adv)
            for span, r, length in [('curta',avg,3.5),('longa',long,120)]:
                conducts_per_round=r.get('conduct_attempts',0)/length
                app=r['condition_applications']/length
                per_hit=r.get('conduct_hits',0)/length
                row={'finishes_per_round':r['finish_attempts']/length,
                     'conduct_attempts_per_round':conducts_per_round,
                     'conduct_hits_per_round':per_hit,
                     'opening_hits_per_round':r['open_hits']/length,
                     'condition_applications_per_round':app,
                     'PE_day_at_1':conducts_per_round*10.5}
                # Desarmado 3,45 já inclui caminhar 3 m até a arma: não somar de novo.
                for name,value in [('derrubada',8.45+.9),('desarme',3.45),
                                   ('lento',39.2),('impedido',132.15)]:
                    gross=app*value
                    row[name]={'alone_slices':gross/FATIA,
                       'plus_conduction_3_39':(gross+per_hit*3.39)/FATIA,
                       'net_if_1PE_fully_competes':(gross+per_hit*3.39-conducts_per_round*PE_EQ)/FATIA}
                # Teste separado de terreno: alvo tem zero alvos legais sem se aproximar.
                row['direction_denial_219_slices']=per_hit*q*219/FATIA
                out['routes'][f'{label}_N{n}_{span}']=row
    out['pressure']={}
    for adv in (False,True):
        for n in (1,2):
            r=route(120,2,.55,n,pressure=True,adv=adv)
            out['pressure'][f'adv{adv}_N{n}']={
                'extra_hits_per_round':r['extra_hit_from_pressure']/120,
                'damage_gain_26_5':r['extra_hit_from_pressure']/120*26.5,
                'conducts_per_round':r['conduct_attempts']/120,
                'finishes_per_round':r['finish_attempts']/120}
    out['one_fixar_per_combat']={}
    for p,adv,q,label in [(.55,False,.35,'base'),(.65,True,.55,'batedor'),(.95,False,.75,'estresse')]:
        vals=[]
        for t in (3,4):
            r=route(t,2,p,2,q,adv=adv,stop_condition=True)
            vals.append(r['condition_applications']*132.15)
        out['one_fixar_per_combat'][label]=sum(vals)/7/FATIA
    out['optimized_day_simplified']={}
    for p,q,label in [(.55,.35,'base'),(1-.35**2,.55,'batedor'),(.95,.75,'estresse')]:
        for cap in (None,2,1):
            value=sum(optimized_day(lengths,p,q,cap)
                      for lengths in product((3,4),repeat=3))/8/10.5/FATIA
            out['optimized_day_simplified'][f'{label}_cap{cap}']=value
    out['low_level_energy']={}
    for n in (1,2):
        a=route(3,1,.55,n); b=route(4,1,.55,n)
        out['low_level_energy'][f'N{n}_PE_day_at1']=(a['conduct_attempts']+b['conduct_attempts'])/2*3
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    audit()
