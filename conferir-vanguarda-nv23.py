"""Candidata nv23: preservar uma sequência após erro de condução, 1/cena.

Instrumentação isolada da v3. Não altera as regras já aprovadas nem os arquivos
de consulta. Usa a mesma régua para medir interação com Conclusão Dupla.
"""
from pathlib import Path
from dataclasses import replace
import runpy
import types
import sys
import json

ROOT = Path(__file__).resolve().parent
original = runpy.run_path(str(ROOT/'conferir-vanguarda-v3.py'))
source = (ROOT/'conferir-vanguarda-v3.py').read_text().split('\ndef audit():')[0]


def change(old,new):
    global source
    assert source.count(old)==1,(old,source.count(old))
    source=source.replace(old,new)


change('+ PAIR_NAMES', '+ PAIR_NAMES + ("recoveries",)')
change('    slow_from_turn:int=1', '    slow_from_turn:int=1\n    recovery:bool=False')
change('def v(t,a,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent):',
       'def v(t,a,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent,recovery_spent):')
change("return v(t+1,0,n,expiry,False,False,buff,buff_exp,(),precision,duo_spent)",
       "return v(t+1,0,n,expiry,False,False,buff,buff_exp,(),precision,duo_spent,recovery_spent)")
change('return v(t,2,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent)',
       'return v(t,2,n,expiry,used,closed,buff,buff_exp,condition,precision,duo_spent,recovery_spent)')
change('pr=precision if spell else False,ds=duo_spent):',
       'pr=precision if spell else False,ds=duo_spent,rs=recovery_spent):')
change('return v(t,a+1,nn,ee,uu,cc,bb,be,co,pr,ds)',
       'return v(t,a+1,nn,ee,uu,cc,bb,be,co,pr,ds,rs)')
change('                    choices.append(add(entry(benefit=dd-baseline+pp*magnitude,',
       '''                    if cfg.recovery and not recovery_spent and cfg.break_on_miss:
                        preserved=add(entry(recoveries=1.),after(uu=True,bb=bb,be=be,rs=True))
                        # A decisão de gastar o uso ocorre depois de conhecer o erro.
                        # Manter n e expiry não registra um acerto nem renova o prazo.
                        if score(preserved)>score(miss)+1e-12:
                            miss=preserved
                    choices.append(add(entry(benefit=dd-baseline+pp*magnitude,''')
change("result = v(1,0,initial_n,initial_expiry,False,False,'',-1,(),False,False)",
       "result = v(1,0,initial_n,initial_expiry,False,False,'',-1,(),False,False,False)")

module=types.ModuleType('vanguarda_nv23_model')
module.__file__=str(ROOT/'conferir-vanguarda-v3.py')
sys.modules[module.__name__]=module
exec(compile(source,'<v3 com candidata nv23>','exec'),module.__dict__)
Config,day,solve=module.Config,module.day,module.solve


def compare(cfg,**kwargs):
    values={}
    for recovery,capstone in ((False,False),(True,False),(False,True),(True,True)):
        row=day(replace(cfg,recovery=recovery,capstone=capstone),**kwargs)
        assert row['recoveries']<=3+1e-9
        assert row['double_attempts']<=3+1e-9
        assert abs(row['pe']-row['conduct_attempts']*((cfg.mastery+1)//2+1))<1e-8
        values[f'nv23_{recovery}_nv30_{capstone}']=row
    b=values['nv23_False_nv30_False']['net_slices']
    a=values['nv23_True_nv30_False']['net_slices']
    z=values['nv23_False_nv30_True']['net_slices']
    both=values['nv23_True_nv30_True']['net_slices']
    assert a>=b-1e-9 and both>=z-1e-9
    values['marginal_23_sem_30']=a-b
    values['marginal_23_com_30']=both-z
    values['marginal_30_apos_23']=both-a
    values['incremento_conjunto_23_30']=both-b
    return values


reference=Config('yumi_referencia',p_die=.65,advantage=True,q_physical=.55,q_vigor=.55,
                 movement=12.,weapon_mean=5.5,damage_normal=25.5,
                 external_explorable=True,school='precisao')
melee=Config('lamina_longa',melee=True,weapon_mean=6.5,damage_normal=26.5,kokusen=.2,
             external_explorable=True,school_open_value=3.39)
result={'status':'Proposta de nível 23, não aprovada. Comparação condicional com a régua v3.',
        'rules':'Uma vez/cena, após errar uma condução, pode preservar sequência e progresso, sem dano, efeito, acerto, reembolso de PE ou renovação do prazo.',
        'cases':{}}
for name,cfg,kwargs in [
    ('referencia',reference,{}),
    ('referencia_inicio_T2',reference,{'start_turn':2}),
    ('referencia_T2_sem_ataque',reference,{'skip_turns':(2,)}),
    ('cobertura_parcial',replace(reference,cover=2),{}),
    ('cobertura_boa',replace(reference,cover=5),{}),
    ('sem_requisito_fixar',replace(reference,external_slow=False),{}),
    ('versado',replace(reference,school='',school_open_value=7.2),{}),
    ('melee',melee,{}),
    ('melee_sem_cotacao_PE',melee,{'pe_rate':0.}),
    ('defesa_18',replace(reference,p_die=.75,q_physical=.65),{}),
    ('defesa_16',replace(reference,p_die=.85,q_physical=.75),{}),
    ('extremo',replace(reference,p_die=.95,q_physical=.85,q_vigor=.85),{}),
]:
    # Desativada, a instrumentação deve reproduzir o arquivo vigente.
    oldcfg=original['Config'](**{k:v for k,v in cfg.__dict__.items() if k!='recovery'})
    for cap in (False,True):
        old=original['day'](replace(oldcfg,capstone=cap),**kwargs)
        new=day(replace(cfg,capstone=cap,recovery=False),**kwargs)
        for k in original['KEYS']:
            assert abs(old[k]-new[k])<1e-8,(name,cap,k)
    result['cases'][name]=compare(cfg,**kwargs)
    r=result['cases'][name]
    print(name,'23',round(r['marginal_23_sem_30'],4),
          '23 com 30',round(r['marginal_23_com_30'],4),
          '30 apos 23',round(r['marginal_30_apos_23'],4),
          'conjunto',round(r['incremento_conjunto_23_30'],4),flush=True)

proof=replace(reference,recovery=True,capstone=True)
assert solve(proof,2,0)['double_attempts']==0
assert solve(proof,6,0)['recoveries']<=1+1e-9
assert solve(proof,3,0,skip_turns=(1,2),initial_sequence=(2,2))['double_attempts']==0
result['checks']='Regressão desativada, um uso/cena, PE sem reembolso, sem acerto fictício e prazo preservado: OK.'
(ROOT/'vanguarda-nv23-contas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['checks'],flush=True)
