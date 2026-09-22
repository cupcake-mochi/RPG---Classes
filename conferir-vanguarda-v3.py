"""Auditoria de 19/09: conduções sem teto, erro encerra, Conclusão Dupla.

Programação dinâmica, sem amostragem. Preserva as âncoras da auditoria v2,
compara a mesma ficha com/sem o nível 30 e declara a sobreposição de condições.
"""
from pathlib import Path
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import combinations, product
import runpy
import json

ROOT = Path(__file__).resolve().parent
OLD = runpy.run_path(str(ROOT/'conferir-vanguarda-v2.py'))
SLICE, PE_RATE = OLD['SLICE'], OLD['PE_RATE']
CONDUCTS, FINISHES = OLD['CONDUCTS'], OLD['FINISHES']
PAIRS = tuple(combinations(FINISHES, 2))
PAIR_NAMES = tuple('dupla:'+'+'.join(p) for p in PAIRS)
KEYS = ('benefit','opening_loss','pe','open_hits','conduct_attempts','finish_attempts',
        'double_attempts','double_both_saves_failed') + PAIR_NAMES
IDX = {k:i for i,k in enumerate(KEYS)}
ZERO = (0.,)*len(KEYS)
chance, critical_chance = OLD['chance'], OLD['critical_chance']
SAVE_FINISHES = frozenset(('derrubada','desarme','resposta','ritmo','fixar'))


@dataclass(frozen=True)
class Config(OLD['Config']):
    conduct_cap:int=0
    break_on_miss:bool=True
    capstone:bool=False
    school:str=''
    school_open_value:float=0.
    overlap_mode:str='union'
    # Parte do valor de impedir Reação que resta quando Impedido já prejudicou ataques.
    reaction_after_fixar:float=.5
    slow_from_turn:int=1
    response_magnitude:float|None=None
    response_enabled:bool=True


def add(*vectors):
    return tuple(map(sum,zip(*vectors)))


def scale(vector, weight):
    return tuple(x*weight for x in vector)


def entry(**kwargs):
    v = list(ZERO)
    for k,x in kwargs.items():
        v[IDX[k]] = x
    return tuple(v)


def attack(cfg, pressure=False, condition=(), finishes=(), spell=False, precision=False):
    cover = cfg.cover
    if 'cobertura' in finishes:
        cover = 0 if cover==2 else 2 if cover==5 else 0
    base = cfg.p_die-.05*cover+.05*pressure+.05*precision
    adv = (cfg.advantage and not spell) or 'fixar' in condition or ('derrubada' in condition and cfg.melee)
    dis = 'derrubada' in condition and not cfg.melee
    p = chance(base,adv,dis)
    critical = critical_chance(19 if 'impacto' in finishes else 20,adv,dis)
    damage = cfg.spell_damage if spell else cfg.damage_normal
    extra = damage if spell else (damage+cfg.weapon_mean)*(1+.5*cfg.kokusen)-damage
    return p,p*damage+critical*extra


def condition_value(effects, cfg):
    """Mesmas magnitudes individuais da v2; efeitos simultâneos não somam cegamente.

    Não é simulador de mapa/turno inimigo. Movimento, ação bônus, reação e vantagem
    conservam a conversão histórica. Os modos alternativos medem sensibilidade.
    """
    e = frozenset(effects)
    magnitudes = {'derrubada':9.35,'desarme':3.45,'resposta':36.5,'ritmo':39.2,'fixar':132.15}
    if cfg.response_magnitude is not None:
        magnitudes['resposta'] = cfg.response_magnitude
    if cfg.overlap_mode=='additive':
        return sum(magnitudes[k] for k in e)
    value = 0.
    movement = []
    if 'fixar' in e:
        value += 109.5
        # Um aliado próximo, dois distantes. Derrubado cancela vantagem dos distantes.
        value += 5.75 if 'derrubada' in e else 17.25
        movement.append(5.4)
    if 'derrubada' in e:
        if 'fixar' not in e:
            value += 5.75
        value += .9  # empurrão é efeito distinto da limitação de movimento
        movement.append(2.7)
    if 'ritmo' in e:
        value += 36.5
        movement.append(2.7)
    if 'desarme' in e:
        value += 3.45
    if 'resposta' in e:
        value += magnitudes['resposta']*(cfg.reaction_after_fixar if 'fixar' in e else 1.)
    return value+max(movement,default=0.)


def resistance_outcomes(cfg, finishes, exploring=False):
    """A ordem é declarada antes dos dados. Explorar modifica só o primeiro TR.

    Todos os TRs são calculados antes dos efeitos: Fixar não piora o outro teste
    do mesmo ataque. O acerto compartilhado é aplicado pelo chamador, uma vez.
    """
    saves = [f for f in finishes if f in SAVE_FINISHES]
    qs = []
    for i,f in enumerate(saves):
        q = cfg.q_vigor if f=='ritmo' else cfg.q_physical
        qs.append(min(1.,q+(.05 if exploring and i==0 else 0.)))
    outcomes = []
    for failures in product((False,True),repeat=len(saves)):
        weight = 1.
        successful_effects = []
        for f,q,failed in zip(saves,qs,failures):
            weight *= q if failed else 1-q
            if failed:
                successful_effects.append(f)
        if weight:
            outcomes.append((weight,tuple(successful_effects)))
    return outcomes


def available_finishes(cfg, n, turn):
    allowed = ['impacto'] if cfg.melee else (['cobertura'] if cfg.cover else [])
    if n>=1:
        allowed += ['derrubada','ritmo']
        allowed += ['desarme'] if cfg.melee else (['resposta'] if cfg.response_enabled else [])
    if n>=2 and not cfg.melee and cfg.external_slow and turn>=cfg.slow_from_turn:
        allowed.append('fixar')
    return allowed


def solve(cfg, turns, pe_rate=PE_RATE, start_turn=1, skip_turns=(),
          force_conduct=None, force_finish=None, force_pair=None,
          initial_sequence=None):
    cost = (cfg.mastery+1)//2+1

    def score(v):
        return v[0]-v[1]-pe_rate*v[2]

    @lru_cache(None)
    def v(t,a,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent):
        if t>turns:
            return ZERO
        if a==2:
            if expiry<=t:
                n,expiry,precision=-1,-1,False
            if buff_exp<=t:
                buff,buff_exp='',-1
            return v(t+1,0,n,expiry,False,False,buff,buff_exp,(),precision,duo_spent)
        if t in skip_turns:
            return v(t,2,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent)
        spell = cfg.schedule=='hybrid' and t%2==0 and a==0
        active = buff if buff_exp>=t else ''
        _,baseline = attack(cfg,spell=spell)

        def after(nn=n,ee=expiry,uu=used,cc=closed,bb=buff,be=buff_exp,co=condition,
                  pr=precision if spell else False,ds=duo_spent):
            return v(t,a+1,nn,ee,uu,cc,bb,be,co,pr,ds)

        p,damage = attack(cfg,pressure=active=='pressionar',condition=condition,
                          spell=spell,precision=precision and not spell)
        choices = [add(entry(benefit=damage-baseline),after())]
        if spell or t<start_turn:
            return choices[0]
        if n<0 and not closed:
            choices.append(add(entry(benefit=damage-baseline+p*cfg.school_open_value,
                                     opening_loss=p*cfg.opening_mean_loss,open_hits=p),
                               scale(after(0,t+2,pr=cfg.school=='precisao'),p),
                               scale(after(),1-p)))
        if n>=0 and not used:
            if cfg.conduct_cap==0 or n<cfg.conduct_cap:
                for label in CONDUCTS:
                    if force_conduct and label!=force_conduct:
                        continue
                    if label=='explorar' and not cfg.external_explorable:
                        continue
                    bb,be = (buff,buff_exp) if label==active else ('',-1)
                    pp,dd = attack(cfg,pressure=bb=='pressionar' and be>=t,
                                   condition=condition,precision=precision)
                    magnitude = {'angulo':1.8,'proteger':cfg.protect_value,
                                 'acompanhar':cfg.movement/2*.6,
                                 'fechar':cfg.recoil_value*cfg.q_physical}.get(label,0.)
                    # 2 representa "duas ou mais", nunca um teto quando conduct_cap=0.
                    hit = after(min(2,n+1),t+2,True,bb=label,be=t+1)
                    miss = after(-1,-1,True,bb=bb,be=be) if cfg.break_on_miss else after(uu=True,bb=bb,be=be)
                    choices.append(add(entry(benefit=dd-baseline+pp*magnitude,
                                             pe=cost,conduct_attempts=1),
                                       scale(hit,pp),scale(miss,1-pp)))
            allowed = available_finishes(cfg,n,t)
            options = [(f,) for f in allowed if not force_finish or f==force_finish]
            if cfg.capstone and not duo_spent and n>=2:
                for pair in combinations(allowed,2):
                    if force_pair and frozenset(pair)!=frozenset(force_pair):
                        continue
                    options.append(pair)
                    if active=='explorar' and all(f in SAVE_FINISHES for f in pair):
                        options.append(pair[::-1])
            for finishes in options:
                double = len(finishes)==2
                pp,dd = attack(cfg,pressure=active=='pressionar',condition=condition,
                               finishes=finishes,precision=precision)
                miss = after(-1,-1,True,True,ds=duo_spent or double)
                total = scale(miss,1-pp)
                immediate_benefit = dd-baseline
                both_failed = 0.
                for prob,effects in resistance_outcomes(cfg,finishes,active=='explorar'):
                    new_condition = tuple(sorted(set(condition)|({'fixar','derrubada'}&set(effects))))
                    immediate_benefit += pp*prob*condition_value(effects,cfg)
                    if double and len(effects)==2:
                        both_failed += pp*prob
                    total = add(total,scale(after(-1,-1,True,True,co=new_condition,
                                                  ds=duo_spent or double),pp*prob))
                metric = {}
                if double:
                    pair = next(p for p in PAIRS if frozenset(p)==frozenset(finishes))
                    metric['dupla:'+'+'.join(pair)] = 1.
                choices.append(add(entry(benefit=immediate_benefit,finish_attempts=1.,
                                         double_attempts=float(double),
                                         double_both_saves_failed=both_failed,**metric),total))
        return max(choices,key=lambda x:(score(x),-x[6],-x[2],-x[1]))

    initial_n,initial_expiry = initial_sequence if initial_sequence else (-1,-1)
    result = v(1,0,initial_n,initial_expiry,False,False,'',-1,(),False,False)
    r = dict(zip(KEYS,result))
    r['net_slices'] = score(result)/turns/SLICE
    r['after_opening_slices'] = (r['benefit']-r['opening_loss'])/turns/SLICE
    r['pe_slices_at_selected_rate'] = r['pe']*pe_rate/turns/SLICE
    return r


def day(cfg, pe_rate=PE_RATE, **kwargs):
    results = [solve(cfg,n,pe_rate,**kwargs) for n in (3,4)]
    r = {k:sum(x[k] for x in results)/2*3 for k in KEYS}
    r['net_slices'] = (r['benefit']-r['opening_loss']-pe_rate*r['pe'])/10.5/SLICE
    r['after_opening_slices'] = (r['benefit']-r['opening_loss'])/10.5/SLICE
    r['pe_slices_at_selected_rate'] = r['pe']*pe_rate/10.5/SLICE
    return r


def compare(cfg, **kwargs):
    without = day(replace(cfg,capstone=False),**kwargs)
    with_cap = day(replace(cfg,capstone=True),**kwargs)
    delta = with_cap['net_slices']-without['net_slices']
    assert delta>=-1e-9
    assert with_cap['double_attempts']<=3+1e-9
    for r in (without,with_cap):
        assert abs(r['pe']-r['conduct_attempts']*((cfg.mastery+1)//2+1))<1e-8
        assert abs(r['opening_loss']-r['open_hits']*cfg.opening_mean_loss)<1e-8
        assert r['finish_attempts']+r['conduct_attempts']<=10.5+1e-8
    return {'sem_nivel_30':without,'com_nivel_30':with_cap,'custo_marginal_fatias':delta}


def audit():
    reference = Config('yumi_referencia',p_die=.65,advantage=True,q_physical=.55,q_vigor=.55,
                       movement=12.,weapon_mean=5.5,damage_normal=25.5,
                       external_explorable=True,school='precisao')
    melee = Config('lamina_longa',melee=True,weapon_mean=6.5,damage_normal=26.5,kokusen=.2,
                   external_explorable=True,school_open_value=3.39)
    output = {'status':'Validação condicional, não média empírica nem teto universal.',
              'rules':{'conduct_cap':None,'conduct_miss_ends':True,
                       'deadline':'fim do segundo turno seguinte à última abertura/condução acertada',
                       'double':'uma vez por cena, duas conclusões após pelo menos duas conduções acertadas'},
              'old_regression':{},'profiles':{},'utilization':{},'pairs':{},'sensitivity':{}}

    # A versão nova desligada deve reproduzir os seis componentes contábeis da v2.
    for cfg in (replace(reference,school=''),replace(melee,school_open_value=0.),
                replace(reference,name='cobertura_boa',cover=5,school='')):
        oldcfg = OLD['Config'](**{k:v for k,v in cfg.__dict__.items() if k in OLD['Config'].__dataclass_fields__})
        oldcfg = replace(oldcfg,conduct_cap=2)
        old = OLD['day'](oldcfg)
        new = day(replace(cfg,conduct_cap=2,break_on_miss=False,capstone=False))
        for k in KEYS[:6]:
            assert abs(old[k]-new[k])<1e-7,(cfg.name,k,old[k],new[k])
        output['old_regression'][cfg.name] = new['net_slices']
    print('Regressão contra v2: OK',flush=True)

    output['sequence_without_school']=compare(replace(reference,school=''))

    for cfg in (reference,melee,
                replace(melee,name='lamina_curta',school='precisao',school_open_value=0.,weapon_mean=4.5,damage_normal=24.5),
                replace(reference,name='yumi_versado',school='',school_open_value=7.2),
                replace(reference,name='yumi_sem_requisito_fixar',external_slow=False),
                replace(reference,name='yumi_cobertura_parcial',cover=2),
                replace(reference,name='yumi_cobertura_boa',cover=5),
                replace(melee,name='estocada_hibrida',schedule='hybrid',kokusen=.36)):
        output['profiles'][cfg.name] = {'params':cfg.__dict__,**compare(cfg)}
        row=output['profiles'][cfg.name]
        print(cfg.name,round(row['sem_nivel_30']['net_slices'],4),
              round(row['com_nivel_30']['net_slices'],4),
              'adicional',round(row['custo_marginal_fatias'],4),flush=True)

    for dex in (6,4,2,0):
        p=min(.95,max(.05,(21-(14+dex-12))/20))
        q=(18-dex-1)/20
        cfg=replace(reference,name=f'dex{dex}',p_die=p,q_physical=q)
        output['utilization'][cfg.name]={}
        for label,kwargs in [('desde_T1',{}),('desde_T2',{'start_turn':2}),
                             ('T2_sem_ataque',{'skip_turns':(2,)})]:
            output['utilization'][cfg.name][label]=compare(cfg,**kwargs)
        print('Defesa/TR correlacionados DEX',dex,'OK',flush=True)

    for cfg in (reference,melee,replace(reference,name='yumi_cobertura_boa',cover=5)):
        output['pairs'][cfg.name]={}
        allowed=available_finishes(cfg,2,3)
        for pair in combinations(allowed,2):
            output['pairs'][cfg.name]['+'.join(pair)]=compare(cfg,force_pair=pair)

    for label,cfg,kwargs in [
        ('sobreposicao_aditiva',replace(reference,overlap_mode='additive'),{}),
        ('reacao_integral_mesmo_impedido',replace(reference,reaction_after_fixar=1.),{}),
        ('sem_cotacao_PE',reference,{'pe_rate':0.}),
        ('metade_cotacao_PE',reference,{'pe_rate':PE_RATE/2}),
        ('melee_sem_cotacao_PE',melee,{'pe_rate':0.}),
        ('TR_vigor_85',replace(reference,q_vigor=.85),{}),
        ('TR_vigor_35',replace(reference,q_vigor=.35),{}),
        ('extremo_ambos_TR_85',replace(reference,p_die=.95,q_physical=.85,q_vigor=.85),{}),
        ('lamina_precisa',replace(melee,p_die=.75,q_physical=.55,q_vigor=.55),{}),
        ('lamina_com_vantagem',replace(melee,p_die=.75,advantage=True,q_physical=.55,q_vigor=.55),{}),
    ]:
        output['sensitivity'][label]=compare(cfg,**kwargs)
    print('Catálogo de duplas e sensibilidade: OK',flush=True)

    output['long_combats']={}
    for name,cfg,turns in [
        ('referencia_6_turnos',reference,6),
        ('referencia_8_turnos',reference,8),
        ('requisito_fixar_so_T6',replace(reference,slow_from_turn=6),8),
    ]:
        without=solve(replace(cfg,capstone=False),turns)
        with_cap=solve(replace(cfg,capstone=True),turns)
        capped=solve(replace(cfg,capstone=True,conduct_cap=2),turns)
        output['long_combats'][name]={'sem_nivel_30':without,'com_nivel_30':with_cap,
                                      'com_teto_antigo':capped,
                                      'custo_marginal_fatias':with_cap['net_slices']-without['net_slices'],
                                      'incremento_sem_teto':with_cap['net_slices']-capped['net_slices']}
        assert with_cap['double_attempts']<=1+1e-9
        print('Luta longa',name,'adicional',round(with_cap['net_slices']-without['net_slices'],4),flush=True)

    # Prova da ausência de teto: é possível a política acertar mais de duas
    # conduções em uma sequência. O benefício artificial isola esta regra.
    continuity=replace(melee,p_die=.95,protect_value=100.,school_open_value=0.,capstone=False)
    unlimited=solve(continuity,6,0,force_conduct='proteger',force_finish='impacto')
    capped=solve(replace(continuity,conduct_cap=2),6,0,force_conduct='proteger',force_finish='impacto')
    assert unlimited['conduct_attempts']>capped['conduct_attempts']
    assert unlimited['net_slices']>capped['net_slices']
    output['rule_checks']={'unlimited_conduct_attempts':unlimited['conduct_attempts'],
                          'capped_conduct_attempts':capped['conduct_attempts']}

    proof=replace(reference,capstone=True,p_die=.95,q_physical=.85)
    assert solve(proof,2,0)['double_attempts']==0
    assert solve(proof,3,0)['double_attempts']>0
    assert solve(proof,3,0,skip_turns=(1,2),initial_sequence=(2,2))['double_attempts']==0
    assert solve(proof,2,0,skip_turns=(1,),initial_sequence=(2,2))['double_attempts']>0
    no_slow=replace(proof,external_slow=False)
    invalid=solve(no_slow,4,0,force_pair=('ritmo','fixar'))
    assert invalid['double_attempts']==0
    assert condition_value(('ritmo','fixar'),proof)==132.15+36.5
    assert condition_value(('resposta','fixar'),proof)==132.15+18.25
    assert attack(proof,finishes=('fixar','ritmo'))==attack(proof)
    assert attack(melee,finishes=('impacto','derrubada'))==attack(melee,finishes=('impacto',))
    assert 'fixar' not in available_finishes(melee,2,3)
    assert 'impacto' not in available_finishes(reference,2,3)
    assert 'fixar' not in available_finishes(reference,1,3)
    outcomes=resistance_outcomes(replace(proof,q_physical=.55,q_vigor=.55),('fixar','ritmo'),True)
    assert abs(sum(w for w,e in outcomes if 'fixar' in e)-.60)<1e-12
    assert abs(sum(w for w,e in outcomes if 'ritmo' in e)-.55)<1e-12
    assert abs(sum(w for w,e in outcomes)-1)<1e-12
    assert solve(proof,6,0)['double_attempts']<=1+1e-9
    no_error=day(replace(reference,break_on_miss=False,capstone=False))
    with_error=day(replace(reference,break_on_miss=True,capstone=False))
    assert no_error['net_slices']>=with_error['net_slices']-1e-9

    output['rule_checks']['no_error_ends_net']=no_error['net_slices']
    output['rule_checks']['error_ends_net']=with_error['net_slices']
    output['checks']='Regressão, custos, erros, prazo, conduções sem teto, requisitos, limite por cena e sobreposições: OK.'
    (ROOT/'vanguarda-contas-v3.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(output['checks'],flush=True)


def comparar_resposta(publicar=False):
    """Sensibilidade da janela; não adota uma mudança de regra.

    Reutiliza o modelo de Persistência e PE do dono atual. A tabela publicada
    é conferida sem ser reescrita, salvo publicação explícita após revisão.
    """
    import re
    doc = ROOT/'RASCUNHO-comparacao-resposta.md'
    texto = doc.read_text()
    loader = (ROOT/'conferir-vanguarda-pe.py').read_text().split('\noutput = {')[0]
    ns = {'__file__':str(ROOT/'conferir-vanguarda-pe.py')}
    exec(compile(loader, '<resposta: modelo atual com Persistência>', 'exec'), ns)
    medir, referencia, melee = ns['day'], ns['reference'], ns['melee']
    # O número de recuperações pertence ao dono de Persistência usado no preço Br.
    usos = int(re.search(r'recovery_uses=(\d+)', (ROOT/'conferir-vanguarda-pe.py').read_text()).group(1))
    magia = (ROOT/'estocada-conclusoes-feiticos.md').read_text()
    larga = float(re.search(r'magnitude (\d+,\d+)', magia).group(1).replace(',', '.'))
    fonte = (ROOT/'referencia-jjk-project/sistema/03-mecanica/19-dano-e-condicoes.md').read_text()
    def celula(label):
        linha = next(l for l in fonte.splitlines() if l.startswith('| '+label+' |'))
        return float(re.search(r'`([\d,]+)`', linha.split('|')[2]).group(1).replace(',', '.'))
    estreita = celula('vantagem e desvantagem')*celula('`1` ponto percentual na rolagem de um aliado')
    base = json.loads((ROOT/'vanguarda-pe-contas.json').read_text())
    cenarios = [('distancia', referencia), ('corpo_a_corpo', melee),
                ('sem_fixar', replace(referencia, external_slow=False))]
    for rotulo, q in re.findall(r'^\| (vigor_resiste_\w+) \| ([0-9.]+) \|$', texto, re.M):
        cenarios.append((rotulo, replace(referencia, q_vigor=float(q))))
    assert len(cenarios)>3, 'Faltam cenários de sensibilidade de Vigor no documento dono'
    saida = {'magnitudes':{'larga':larga, 'estreita':estreita}, 'cenarios':{}}
    linhas = ['| Grandeza | Larga | Estreita |', '|---|---:|---:|']
    def linha(nome, a, b):
        linhas.append(f'| {nome} | {a:.6f} | {b:.6f} |')
    linha('Magnitude por aplicação bem-sucedida', larga, estreita)
    for nome, cfg in cenarios:
        resultados = {}
        for janela, magnitude in saida['magnitudes'].items():
            c = replace(cfg, response_magnitude=magnitude)
            seq = medir(replace(c, school='', school_open_value=0), pe_rate=0)
            antes = medir(replace(c, recovery=True, recovery_uses=usos), pe_rate=0)
            completo_cfg = replace(c, recovery=True, recovery_uses=usos, capstone=True)
            completo = medir(completo_cfg, pe_rate=0)
            sem = medir(replace(completo_cfg, response_enabled=False), pe_rate=0)
            resultados[janela] = {
                'sequencia':seq['after_opening_slices'],
                'caminho':completo['after_opening_slices']+base['nao_cede_slices'],
                'dupla_marginal':completo['after_opening_slices']-antes['after_opening_slices'],
                'resposta_marginal':completo['after_opening_slices']-sem['after_opening_slices'],
                'duplas_dia':{k:v for k,v in completo.items() if k.startswith('dupla:')},
                'pares_isolados':{},
            }
            if nome == 'distancia':
                for par in combinations(ns['ns']['module'].available_finishes(c, 2, 3), 2):
                    r = medir(completo_cfg, pe_rate=0, force_pair=par)
                    resultados[janela]['pares_isolados']['+'.join(par)] = r['after_opening_slices']-antes['after_opening_slices']
            assert resultados[janela]['resposta_marginal']>=-1e-9
        a, b = resultados['larga'], resultados['estreita']
        if nome in base['perfis']:
            assert abs(a['caminho']-base['perfis'][nome]['total_com_nao_cede']['Br'])<1e-9, f'{nome}: janela larga diverge do preço Br atual'
        assert a['caminho']>=b['caminho']-1e-9, f'{nome}: estreitar aumentou o valor'
        for chave in ('sequencia','caminho','dupla_marginal','resposta_marginal'):
            linha(nome+'/'+chave, a[chave], b[chave])
        for chave in a['duplas_dia']:
            if max(a['duplas_dia'][chave], b['duplas_dia'][chave])>1e-9:
                linha(nome+'/'+chave+'/tentativas_dia', a['duplas_dia'][chave], b['duplas_dia'][chave])
        for chave in a['pares_isolados']:
            linha(nome+'/dupla_isolada/'+chave, a['pares_isolados'][chave], b['pares_isolados'][chave])
        saida['cenarios'][nome] = resultados
        print('Comparação de janelas:', nome, 'OK', flush=True)
    inicio, fim = '<!-- inicio-contas-resposta -->', '<!-- fim-contas-resposta -->'
    anterior = texto.split(inicio)[1].split(fim)[0]
    calculado = '\n'+'\n'.join(linhas)+'\n'
    if publicar:
        doc.write_text(texto.replace(inicio+anterior+fim, inicio+calculado+fim))
    else:
        assert anterior == calculado, 'Tabela publicada da comparação de Resposta diverge do cálculo; revisar a fonte alterada'
    saida['checks'] = 'Preço largo reproduz Br; remoção não aumenta valor; estreitar não aumenta valor; tabela publicada confere.'
    (ROOT/'vanguarda-resposta-contas.json').write_text(json.dumps(saida, ensure_ascii=False, indent=2)+'\n')
    print(saida['checks'], flush=True)


if __name__=='__main__':
    import sys
    if sys.argv[1:] == ['--comparar-resposta']:
        comparar_resposta()
    elif not sys.argv[1:]:
        audit()
    else:
        raise SystemExit('Uso: conferir-vanguarda-v3.py [--comparar-resposta]')
