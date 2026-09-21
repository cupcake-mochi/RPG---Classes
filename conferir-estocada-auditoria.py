"""Auditoria estrutural da Estocada, não validação de um preço universal.

1) Enumera acertos e críticos de arma/Classe 0 no Ferrão de alvo único.
2) Enumera estados da sequência em rotinas declaradas, sem frequência inventada.
3) Confere os ataques que Compasso/Bote acrescentam à ação Conjurar atual.

Os roteiros são políticas fixas, não um otimizador de todas as ações possíveis.
Não precifica o catálogo mágico inteiro nem transforma seu melhor caso em média.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SLICE=5.08
CHANNEL={1:2.5,3:5.,6:7.5,9:10.,10:14.}
KEYS=('opening_attempts','opening_hits','conduct_attempts','conduct_hits',
      'closing_attempts','closing_affected','ferrão_uses','recovery_uses',
      'weapon_attempts','weapon_damage','opening_loss','conduct_pe')
ZERO=(0.,)*len(KEYS)


def add(*vs): return tuple(map(sum,zip(*vs)))
def scale(v,p): return tuple(x*p for x in v)
def entry(**kw): return tuple(float(kw.get(k,0)) for k in KEYS)


def attack_mean(p,channel):
    threshold=21-round(20*p)
    return sum((6.5+6+channel+(6.5 if d==20 else 0)) if d>=threshold else 0
               for d in range(1,21))/20


def ferrão(p_weapon=.55,p_c0=.55,channel=7.5):
    """Condicional ao feitiço principal já ter afetado o alvo.
    Arma d12+6, Classe 0 6d8, crítico próprio. Sem Kokusen, Bloquear ou outros mods.
    """
    tw,tc=21-round(20*p_weapon),21-round(20*p_c0)
    old=new=0.
    for w,c in product(range(1,21),repeat=2):
        if w<tw: continue
        weapon=6.5+6+(6.5 if w==20 else 0)
        old+=weapon+channel
        new+=weapon+(27*(2 if c==20 else 1) if c>=tc else 0)
    delta=(new-old)/400
    direct=p_weapon*((p_c0+.05)*27-channel)
    assert abs(delta-direct)<1e-9
    return {'normal_weapon':old/400,'with_ferrão':new/400,
            'delta_after_main_spell_affected':delta,
            'delta_per_closing_attempt_p55':.55*delta}


def scene(schedule,channel,required=1,with_ferrão=True,start_sequence=1,p=.55,
          recovery_uses=3):
    """W=Atacar, D=Conjurar dano, C=Conjurar condição sem dano, X=sem ataque.
    Acompanha o Movimento é a condução fixa, sem alterar chances de acerto.
    Fecha no primeiro feitiço elegível após required acertos, sem otimizar o efeito.
    """
    normal=attack_mean(p,channel)
    delta=ferrão(p,p,channel)['delta_after_main_spell_affected']

    @lru_cache(None)
    def turn(t,n,expiry,recoveries):
        if t>len(schedule): return ZERO
        if expiry<t: n,expiry=-1,-1
        mode=schedule[t-1]
        if mode=='X': return turn(t+1,n,expiry,recoveries)
        eligible=mode in ('C','D') and n>=required and t>=start_sequence
        if eligible:
            # Todo feitiço de encerramento ocupa a etapa do turno, mesmo na falha.
            return add(entry(closing_attempts=1,closing_affected=p),
                       scale(bonus(t,-1,-1,recoveries,True,True,True),p),
                       scale(bonus(t,-1,-1,recoveries,True,True,False),1-p))
        return bonus(t,n,expiry,recoveries,False,False,False)

    def bonus(t,n,expiry,recoveries,used,closed,main_affected):
        mode=schedule[t-1]
        can_f=with_ferrão and main_affected
        attacks=2 if mode in ('W','C') else 1
        use_f=can_f and delta>(normal if mode=='C' else 0.)
        if use_f: attacks=1  # não combina Bote e Ferrão
        value=weapons(t,attacks,n,expiry,recoveries,used,closed)
        return add(entry(ferrão_uses=1,weapon_damage=delta),value) if use_f else value

    @lru_cache(None)
    def weapons(t,left,n,expiry,recoveries,used,closed):
        if left==0: return turn(t+1,n,expiry,recoveries)
        base=entry(weapon_attempts=1,weapon_damage=normal)
        if closed or t<start_sequence:
            return add(base,weapons(t,left-1,n,expiry,recoveries,used,closed))
        if n<0:
            return add(base,entry(opening_attempts=1,opening_hits=p,opening_loss=5*p),
                       scale(weapons(t,left-1,0,t+2,recoveries,used,closed),p),
                       scale(weapons(t,left-1,-1,-1,recoveries,used,closed),1-p))
        if not used and n<required:
            # Erro encerra; Persistência conserva somente progresso e prazo.
            preserve=recoveries>0 and t<expiry
            missed=weapons(t,left-1,n if preserve else -1,expiry if preserve else -1,
                           recoveries-1 if preserve else recoveries,True,closed)
            return add(base,entry(conduct_attempts=1,conduct_hits=p,conduct_pe=3,
                                  recovery_uses=(1-p) if preserve else 0),
                       scale(weapons(t,left-1,n+1,t+2,recoveries,True,closed),p),
                       scale(missed,1-p))
        return add(base,weapons(t,left-1,n,expiry,recoveries,used,closed))

    row=dict(zip(KEYS,turn(1,-1,-1,recovery_uses)))
    assert row['recovery_uses']<=recovery_uses+1e-9
    assert row['closing_attempts']+row['conduct_attempts']<=len(schedule)+1e-9
    assert row['ferrão_uses']<=row['closing_affected']+1e-9
    assert abs(row['conduct_pe']-3*row['conduct_attempts'])<1e-9
    row['net_weapon_damage']=row['weapon_damage']-row['opening_loss']
    return row


def compare_scenes(schedules,channel,required=1,start_sequence=1):
    without=[scene(s,channel,required,False,start_sequence) for s in schedules]
    with_f=[scene(s,channel,required,True,start_sequence) for s in schedules]
    turns=sum(map(len,schedules))/len(schedules)
    diff=sum(b['net_weapon_damage']-a['net_weapon_damage'] for a,b in zip(without,with_f))/len(schedules)
    result={'schedules':schedules,'required_conducts':required,
            'expected_closing_attempts_per_scene':sum(r['closing_attempts'] for r in with_f)/len(with_f),
            'expected_ferrão_uses_per_scene':sum(r['ferrão_uses'] for r in with_f)/len(with_f),
            'marginal_ferrão_slices_per_round':diff/turns/SLICE,
            'with_ferrão':with_f,'without_ferrão':without}
    assert diff>=-1e-8
    return result


def audit():
    result={
      'status':'Conferência estrutural e cenários condicionais; não preço final da Trilha.',
      'premissas':{'weapon':'d12 + atributo 6 + Canalizar conforme refino',
        'p_weapon':.55,'p_main_spell_affects':.55,'p_c0':.55,'c0_mean':27,
        'crit_chance':.05,'kokusen':False,'active_blocking':False,
        'prep':'Abertura perde 2d4; condução paga 3 PE; uma condução/conclusão por turno; erro encerra; prazo T+2; Persistência três usos no começo de cada cena.',
        'bonus_opportunity':'Ataques de Compasso/Bote são comparados com a mesma ação Conjurar, com bônus sem outro uso quantificado. Não é otimização de todas as ações da ficha.',
        'limits':'Feitiços e efeitos de conclusão têm o mesmo resultado-base dos dois lados da comparação de Ferrão. Não enumera todos os modificadores criados por essas condições nem o valor do catálogo mágico.'},
      'ferrão_by_refino':{},'scenes':{},'compasso_bote':{}}
    for ref,channel in CHANNEL.items():
        result['ferrão_by_refino'][str(ref)]=ferrão(channel=channel)
        w=attack_mean(.55,channel)
        result['compasso_bote'][str(ref)]={'weapon_expected':w,
          'one_bonus_weapon_every_round_slices':w/SLICE,
          'two_bonus_weapons_every_round_slices':2*w/SLICE,
          'two_plus_pe_pool_two_rests':2*w/SLICE+10*5.14/10.5/SLICE}
        for name,ss,req,start in [
          ('conjurar_desde_T1',['DDD','DDDD'],1,1),
          ('abrir_com_Atacar',['WDD','WDDD'],1,1),
          ('inicio_T2',['DDD','DDDD'],1,2),
          ('T2_sem_ataque',['WXD','WXDD'],1,1),
          ('duas_conducoes',['WDD','WDDD'],2,1),
          ('condicao_sem_dano',['CCC','CCCC'],1,1),
          ('seis_turnos',['WDDDDD'],1,1),
        ]:
            result['scenes'][f'ref{ref}_{name}']=compare_scenes(ss,channel,req,start)
    # Invariantes da política: sem preparação não inventa conclusão; esperar não renova.
    assert scene('DD',7.5)['closing_attempts']==0
    assert scene('WXXD',7.5)['closing_attempts']==0
    assert scene('CCCC',7.5)['ferrão_uses']==0  # Bote é a escolha melhor neste perfil.
    assert scene('WDDD',7.5,recovery_uses=0)['recovery_uses']==0
    result['checks']='Enumeração de dados = fórmula; contador, custos, prazo, ordem, preparação e incompatibilidade com Bote: OK.'
    (ROOT/'estocada-auditoria-contas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for ref in CHANNEL:
        d=result['ferrão_by_refino'][str(ref)]
        print('Refino',ref,'Ferrão por habilitação',round(d['delta_after_main_spell_affected'],4),
              'fatias no roteiro WDD/WDDD',round(result['scenes'][f'ref{ref}_abrir_com_Atacar']['marginal_ferrão_slices_per_round'],6))
    print('Compasso+Bote, dois ataques em toda rodada de conjuração sem dano:')
    for ref,row in result['compasso_bote'].items(): print(ref,json.dumps(row,ensure_ascii=False))
    print(result['checks'])


if __name__=='__main__': audit()
