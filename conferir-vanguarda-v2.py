"""Preço de catálogo da Sequência, com custos propostos pelo autor em 18/09.

Somente arquivos nesta pasta autorizada; não importa o projeto de consulta.
Enumeração por programação dinâmica: nenhuma amostragem aleatória.
Valores de controle vêm da régua histórica e não são dano adicional real.
"""
from dataclasses import dataclass, replace
from functools import lru_cache
from collections import Counter
import json

SLICE = 5.08
PE_RATE = 5.14
CONDUCTS = ('angulo','pressionar','proteger','acompanhar','explorar','fechar')
FINISHES = ('impacto','derrubada','desarme','cobertura','resposta','ritmo','fixar')
KEYS = ('benefit','opening_loss','pe','open_hits','conduct_attempts','finish_attempts') + CONDUCTS + FINISHES
IDX = {k:i for i,k in enumerate(KEYS)}
ZERO = (0.,)*len(KEYS)


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(len(KEYS)))


def scale(v, w):
    return tuple(x*w for x in v)


def entry(**kwargs):
    result = list(ZERO)
    for key,value in kwargs.items():
        result[IDX[key]]=value
    return tuple(result)


def pmf(dice, fixed=0):
    dist={fixed:1.}
    for sides in dice:
        nxt=Counter()
        for value,prob in dist.items():
            for face in range(1,sides+1):
                nxt[value+face]+=prob/sides
        dist=dict(nxt)
    return dist


def clipped_loss(damage_dice, fixed, penalty_dice):
    return sum(pd*pc*min(d,c)
               for d,pd in pmf(damage_dice,fixed).items()
               for c,pc in pmf(penalty_dice).items())


@dataclass(frozen=True)
class Config:
    name:str
    p_die:float=.55       # chance antes de vantagem e cobertura
    advantage:bool=False
    q_physical:float=.35
    q_vigor:float=.35
    melee:bool=False
    weapon_mean:float=9.
    damage_normal:float=23.
    kokusen:float=0.
    movement:float=9.
    cover:int=0          # 0, 2, 5; cobertura do alvo contra atirador
    mastery:int=4
    opening_mean_loss:float=5.
    external_slow:bool=True
    external_explorable:bool=False
    conduct_cap:int=2    # 0 = sem limite, só para comparação
    # 'hybrid' alterna dois ataques de arma com feitiço + arma.
    schedule:str='weapons'
    spell_damage:float=126.
    # Livre: todos os efeitos estão úteis quando usados (limite favorável).
    protect_value:float=3.39
    recoil_value:float=5.40


def chance(p, adv, disadvantage=False):
    p=max(.05,min(.95,p))
    if adv and disadvantage:
        return p
    if adv:
        return 1-(1-p)**2
    if disadvantage:
        return p*p
    return p


def critical_chance(threshold, adv, disadvantage=False):
    p=(21-threshold)/20
    if adv and disadvantage:
        return p
    if adv:
        return 1-(1-p)**2
    if disadvantage:
        return p*p
    return p


def attack(cfg, pressure=False, condition='', finish='', spell=False):
    cover=cfg.cover
    if finish=='cobertura':
        cover=0 if cover==2 else 2 if cover==5 else 0
    base=cfg.p_die-cover*.05+(0.05 if pressure else 0)
    # Mirar concede vantagem à arma de projétil, não ao feitiço.
    adv=(cfg.advantage and not spell) or condition=='fixar' or (condition=='derrubada' and cfg.melee)
    dis=condition=='derrubada' and not cfg.melee
    p=chance(base,adv,dis)
    threshold=19 if finish=='impacto' else 20
    crit=critical_chance(threshold,adv,dis)
    if spell:
        damage=cfg.spell_damage
        extra=damage
    else:
        damage=cfg.damage_normal
        critical=(damage+cfg.weapon_mean)*(1+.5*cfg.kokusen)
        extra=critical-damage
    return p,p*damage+crit*extra


def solve(cfg, turns, pe_rate=PE_RATE, force_conduct=None, force_finish=None,
          start_turn=1, skip_turns=()):
    """Política que maximiza benefício - abertura - pe_rate*PE.

    O uso do efeito e o sucesso dos pré-requisitos externos não são sorteados.
    Os ataques, TRs, prazo, troca de condução e custos são probabilísticos.
    Não há limite diário de Fixar. Duas conduções acertadas por sequência.
    'force_*' restringe catálogo; sempre permite não usar a habilidade.
    start_turn adia o primeiro acesso sem retirar rodadas do denominador.
    skip_turns são rodadas sem ataques elegíveis: outra tarefa ou feitiço de TR,
    por exemplo. A ação substituta existe dos dois lados e não é ganho da classe.
    """
    cost=(cfg.mastery+1)//2+1
    decisions=Counter()

    def score(vector):
        return vector[0]-vector[1]-pe_rate*vector[2]

    @lru_cache(None)
    def v(t,a,n,expiry,used,closed,buff,buff_exp,condition):
        if t>turns:
            return ZERO
        if a==2:
            if expiry<=t:
                n,expiry=-1,-1
            if buff_exp<=t:
                buff,buff_exp='',-1
            return v(t+1,0,n,expiry,False,False,buff,buff_exp,'')
        if t in skip_turns:
            return v(t,2,n,expiry,used,closed,buff,buff_exp,condition)
        spell=cfg.schedule=='hybrid' and t%2==0 and a==0
        active=buff if buff_exp>=t else ''
        _,baseline=attack(cfg,spell=spell)

        def after(nn=n,ee=expiry,uu=used,cc=closed,bb=buff,be=buff_exp,co=condition):
            return v(t,a+1,nn,ee,uu,cc,bb,be,co)

        p,damage=attack(cfg,pressure=active=='pressionar',condition=condition,spell=spell)
        choices=[('normal',add(entry(benefit=damage-baseline),after()))]
        if spell or t<start_turn:
            return choices[0][1]
        if n<0 and not closed:
            choices.append(('abrir',add(entry(benefit=damage-baseline,
                                              opening_loss=p*cfg.opening_mean_loss,open_hits=p),
                                        scale(after(0,t+2),p),scale(after(),1-p))))
        if n>=0 and not used:
            if cfg.conduct_cap==0 or n<cfg.conduct_cap:
                for label in CONDUCTS:
                    if force_conduct and label!=force_conduct:
                        continue
                    if label=='explorar' and not cfg.external_explorable:
                        continue
                    # Ao declarar diferente, perde efeitos anteriores ANTES do ataque.
                    bb,be=(buff,buff_exp) if label==active else ('',-1)
                    pp,dd=attack(cfg,pressure=bb=='pressionar' and be>=t,condition=condition)
                    magnitude={'angulo':1.8,'proteger':cfg.protect_value,
                               'acompanhar':cfg.movement/2*.6,
                               'fechar':cfg.recoil_value*cfg.q_physical}.get(label,0.)
                    hit=after(min(2,n+1),t+2,True,bb=label,be=t+1)
                    miss=after(uu=True,bb=bb,be=be)
                    immediate=entry(benefit=dd-baseline+pp*magnitude,pe=cost,conduct_attempts=1,
                                    **{label:1})
                    choices.append((label,add(immediate,scale(hit,pp),scale(miss,1-pp))))
            allowed=[]
            if cfg.melee:
                allowed.append('impacto')
            elif cfg.cover:
                allowed.append('cobertura')
            if n>=1:
                allowed+=['derrubada','ritmo']
                allowed+=['desarme'] if cfg.melee else ['resposta']
            if n>=2 and not cfg.melee and cfg.external_slow:
                allowed.append('fixar')
            for label in allowed:
                if force_finish and label!=force_finish:
                    continue
                pp,dd=attack(cfg,pressure=active=='pressionar',condition=condition,finish=label)
                q=cfg.q_vigor if label=='ritmo' else cfg.q_physical
                q=min(1,q+(.05 if active=='explorar' else 0))
                magnitude={'derrubada':9.35,'desarme':3.45,'resposta':36.5,
                           'ritmo':39.2,'fixar':132.15}.get(label,0.)
                effect=pp*q if magnitude else 0.
                newcondition=label if label in ('fixar','derrubada') else condition
                done=after(-1,-1,True,True)
                success=after(-1,-1,True,True,co=newcondition)
                immediate=entry(benefit=dd-baseline+effect*magnitude,finish_attempts=1,**{label:1})
                choices.append((label,add(immediate,scale(success,effect),scale(done,1-effect))))
        chosen=max(choices,key=lambda pair:(score(pair[1]),-pair[1][2],-pair[1][1]))
        decisions[chosen[0]]+=1
        return chosen[1]

    result=v(1,0,-1,-1,False,False,'',-1,'')
    return dict(zip(KEYS,result))


def day(cfg,pe_rate=PE_RATE,**kwargs):
    results=[solve(cfg,n,pe_rate,**kwargs) for n in (3,4)]
    # Três lutas, cada uma com P(3 turnos)=P(4 turnos)=1/2.
    r={k:sum(x[k] for x in results)/2*3 for k in KEYS}
    r['gross_slices']=r['benefit']/10.5/SLICE
    r['opening_slices']=r['opening_loss']/10.5/SLICE
    r['pe_slices']=r['pe']*PE_RATE/10.5/SLICE
    r['after_opening_slices']=r['gross_slices']-r['opening_slices']
    r['net_slices']=r['after_opening_slices']-r['pe_slices']
    return r


def audit():
    configs=[
        Config('ranged_reference'),
        Config('melee_reference',melee=True,weapon_mean=6.5,damage_normal=26.5,kokusen=.2,
               external_explorable=True),
        Config('batedor',p_die=.65,advantage=True,q_physical=.55,q_vigor=.55,
               movement=12.,weapon_mean=5.5,damage_normal=25.5),
        Config('stress',p_die=.95,q_physical=.75,q_vigor=.75,movement=12.,
               weapon_mean=5.5,damage_normal=25.5,external_explorable=True),
        Config('hybrid',melee=True,weapon_mean=6.5,damage_normal=26.5,kokusen=.36,
               external_explorable=True,schedule='hybrid'),
    ]
    output={'costs':[{ 'mastery':m,'d4':(m+1)//2,'opening_mean':(m+1)//2*2.5,
                      'PE':(m+1)//2+1} for m in range(1,5)],'profiles':{}}
    for cfg in configs:
        output['profiles'][cfg.name]={
            'params':cfg.__dict__,
            'nominal_policy':day(cfg),
            'no_PE_opportunity_policy':day(cfg,0),
            'half_PE_opportunity_policy':day(cfg,PE_RATE/2),
            'no_conduct_cap_nominal':day(replace(cfg,conduct_cap=0)),
        }
    output['ranged_options']={}
    rich=replace(configs[2],external_explorable=True)
    for finish in ('derrubada','resposta','ritmo','fixar'):
        output['ranged_options'][finish]=day(rich,force_finish=finish)
    output['cover_cases']={}
    for c in (2,5):
        cfg=replace(configs[2],cover=c)
        output['cover_cases'][str(c)]=day(cfg)
    output['standalone_conductions']={}
    for label in CONDUCTS:
        output['standalone_conductions'][label]={
            'nominal':day(rich,force_conduct=label),
            'gross_policy':day(rich,0,force_conduct=label),
        }
    output['clipping']={
        'katana_nv2':clipped_loss([8,4],3,[4]),
        'rifle_nv30':clipped_loss([8,8]+[6]*4,0,[4,4]),
        'pistol_nv30':clipped_loss([10]+[6]*4,0,[4,4]),
    }
    output['coupled_defense_resistance']={}
    for dex in (6,4,2,0):
        for trained in (False,True):
            p=min(.95,max(.05,(21-(14+dex-12))/20))
            q=max(0,min(1,(18-dex-(4 if trained else 0)-1)/20))
            cfg=Config(f'DEX{dex}_trained{trained}',p_die=p,advantage=True,
                       q_physical=q,q_vigor=.55,movement=12.,external_explorable=True,
                       weapon_mean=5.5,damage_normal=25.5)
            long=solve(cfg,12)
            output['coupled_defense_resistance'][cfg.name]={
                'params':cfg.__dict__,'p_hit':chance(p,True),
                'day':day(cfg),
                'long_12_net_slices':(long['benefit']-long['opening_loss']-PE_RATE*long['pe'])/12/SLICE,
            }
    # Verificações que falham se os custos passarem a ser subtraídos duas vezes
    # ou se os gates das conclusões forem ignorados.
    test=Config('test',p_die=.95,q_physical=.75,q_vigor=.75,external_explorable=True)
    assert solve(test,1,0)['fixar']==0
    assert solve(test,2,0)['fixar']==0
    assert solve(test,3,0)['fixar']>0
    no_slow=replace(test,external_slow=False)
    assert solve(no_slow,4,0)['fixar']==0
    for label in CONDUCTS:
        row=day(test,0,force_conduct=label)
        assert abs(row['pe']-3*row['conduct_attempts'])<1e-9
        assert abs(row['opening_loss']-5*row['open_hits'])<1e-9
        assert row['conduct_attempts']<=10.5+1e-9
        assert row['finish_attempts']+row['conduct_attempts']<=10.5+1e-9
    for cfg in configs:
        row=day(cfg)
        for label in CONDUCTS:
            restricted=day(cfg,force_conduct=label)
            assert row['net_slices']+1e-9>=restricted['net_slices']
        assert row['net_slices']>=-1e-9
    output['checks']='custos, gates, limite por turno e escolha de catálogo: OK'
    output['utilization_scenarios']={}
    for dex in (6,4,2,0):
        saved=output['coupled_defense_resistance'][f'DEX{dex}_trainedFalse']
        cfg=Config(**saved['params'])
        output['utilization_scenarios'][f'DEX{dex}']={}
        for label,kwargs in [
            ('inicio_T1',{}),('inicio_T2',{'start_turn':2}),
            ('T2_sem_ataque',{'skip_turns':(2,)}),
            ('inicio_T2_e_T3_sem_ataque',{'start_turn':2,'skip_turns':(3,)}),
        ]:
            row=day(cfg,**kwargs)
            output['utilization_scenarios'][f'DEX{dex}'][label]=row
            assert row['pe']<=3*(10.5-3*len(kwargs.get('skip_turns',())))+1e-9
        # Adiar acesso não pode tornar a escolha ótima mais valiosa.
        assert output['utilization_scenarios'][f'DEX{dex}']['inicio_T1']['net_slices']+1e-9>=output['utilization_scenarios'][f'DEX{dex}']['inicio_T2']['net_slices']
    print(json.dumps(output,indent=2,ensure_ascii=False))


if __name__=='__main__':
    audit()
