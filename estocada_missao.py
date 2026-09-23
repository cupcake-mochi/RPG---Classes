"""Motor conjunto chamado por conferir-estocada-rotina.py --missao.

Invariantes: mesma ficha/Caminho e catálogo de feitiços nos dois lados;
PE nunca negativo; recuperação limitada ao máximo; Persistência por descanso;
Dupla por cena; decisão anterior aos dados, salvo Persistência após erro;
um único gate principal para duas conclusões; Canalizar não dobra no crítico;
Ferrão resolve acerto/crítico próprio; Refluxo é recurso, não bônus de dano.
As condições conservam equivalentes condicionados, não dano real.
"""
from dataclasses import replace
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import re
import sys
import time
import hashlib
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent
ZERO = (0., 0., 0.)  # utilidade, PE normal gasto, recuperação normal efetiva
BAD = (-1e90, 0., 0.)


def mix(*branches, value=0., spent=0., recovered=0.):
    return (value + sum(p*v[0] for p,v in branches),
            spent + sum(p*v[1] for p,v in branches),
            recovered + sum(p*v[2] for p,v in branches))


def sources(model):
    p = json.loads((ROOT/'estocada-missao-premissas.json').read_text())
    assert p['refino']==10 and p['maestria']==4, 'Este recorte usa refino 10 e maestria 4'
    manual = (ROOT/'referencia-jjk-project/sistema/05-material/livro/manual/40-fundamento.md').read_text()
    spells = {}
    for row in manual.splitlines():
        m = re.match(r'^\| \*\*([1-7])\*\* \| (\d+) \| (\d+) \|.*? (\d+)d(\d+) =', row)
        if m:
            cl, level, cost, dice, faces = map(int,m.groups())
            if level <= p['nivel']:
                spells[cl] = (cost, dice*(faces+1)/2)
    assert len(spells)==7, 'Tabela Números da montagem incompleta'
    section = manual.split('### Classe 0')[1].split('### Dado')[0]
    levels = [int(s) for s in next(l for l in section.splitlines() if l.startswith('| Seu nível |')).split('|')[2:-1]]
    dice = re.findall(r'(\d+)d(\d+)', next(l for l in section.splitlines() if l.startswith('| Dano |')))
    idx = max(i for i,n in enumerate(levels) if n<=p['nivel'])
    n,faces = map(int,dice[idx])
    spells[0] = (0,n*(faces+1)/2)
    pe = json.loads((ROOT/'estocada-compasso-pe-contas.json').read_text())['orcamento_nivel_30'][0]
    assert pe['atributo_escolhido']==p['atributo'] and pe['nivel']==p['nivel']
    return p,spells,pe


def solve(model, cfg, p, spells, maximum, fights, rests, *, kit=False,
          minimum=0, control_fraction=0., fixed_seven=False, spell_tr=False,
          conclusions=True, ferron=True, path=True, prune=True):
    """Busca exata de decisões adaptativas no catálogo declarado.

    Seqüência/condições são locais ao combate. Persistência e PE atravessam
    combates. A opção sem Trilha conserva o Caminho completo e pode conjurar.
    """
    attack = model['attack']
    resistance = model['resistance_outcomes']
    condition_value = model['condition_value']
    available = model['available_finishes']
    channel = model['_CANALIZAR']
    cost_conduct = (p['maestria']+1)//2+1
    recovery_max = p['maestria']//2+1
    spellcfg = replace(cfg,p_die=p['acerto_feitico'],advantage=False)
    spell_p = p['acerto_feitico']
    c0 = attack(replace(spellcfg,spell_damage=spells[0][1]),spell=True)[1]
    end = sum(fights)
    boundaries = {sum(fights[:i]):i for i in range(1,len(fights)+1)}
    slots_at = {t:end-t+1 for t in range(1,end+1)}
    q = p['falha_tr_adicional']
    # Romper inclui 6m do alvo e metade do deslocamento da própria ficha.
    catalog = dict(model['MAGICAS'])
    catalog['romper_fileira'] = ((6+cfg.movement/2)*model['_M'],True,1)
    catalog['refluxo'] = (0.,False,1)
    # No caso de arma, o crítico dobra apenas seus dados, não Canalizar.
    normal_cfg = replace(cfg,damage_normal=cfg.damage_normal-channel)
    last_rest_turn = max((t for t,i in boundaries.items() if i in rests), default=0)
    max_turn_cost = max(x[0] for x in spells.values())+cost_conduct
    # Conduções sem efeito sustentado não mudam outro eixo deste modelo.
    # Conserva-se a melhor magnitude, além de Pressionar e Explorar.
    immediate_conduct = {'angulo':1.8,'proteger':cfg.protect_value,
                         'acompanhar':cfg.movement/2*.6,
                         'fechar':cfg.recoil_value*cfg.q_physical}
    conducts = [max(immediate_conduct,key=immediate_conduct.get),'pressionar']
    if cfg.external_explorable:
        conducts.append('explorar')
    if not prune:
        conducts=[c for c in model['CONDUCTS'] if c!='explorar' or cfg.external_explorable]

    @lru_cache(None)
    def hit_info(pressure=False,condition=(),precision=False,finishes=(),carried=False):
        return attack(normal_cfg if carried else cfg,pressure=pressure,condition=condition,
                      precision=precision,finishes=finishes)

    @lru_cache(None)
    def spell_finishes(n,duo,exploring):
        allowed = [k for k,(_,_,req) in catalog.items() if n>=req]
        options = [(k,) for k in allowed]
        if n>=2 and not duo:
            options += list(combinations(allowed,2))
        best = {}
        for finish in options:
            qs = [q if catalog[k][1] else 1. for k in finish]
            if exploring:
                eligible = [i for i,k in enumerate(finish) if catalog[k][1]]
                if eligible:
                    j=max(eligible,key=lambda i:catalog[finish[i]][0])
                    qs[j]=min(1.,qs[j]+.05)
            value=sum(catalog[k][0]*prob for k,prob in zip(finish,qs))
            key=(duo or len(finish)==2,'refluxo' in finish)
            best[key]=max(best.get(key,-1.),value)
        return tuple((dd,refund,value) for (dd,refund),value in best.items())

    def charge(pe,tmp,cost):
        assert cost<=pe+tmp
        temp_spent = min(tmp,cost)
        return pe-(cost-temp_spent),tmp-temp_spent,cost-temp_spent

    @lru_cache(None)
    def next_turn(t,n,e,b,be,pr,duo,r,pe,tmp,c):
        if e<=t:
            n,e,pr = -1,-1,False
        if be<=t:
            b,be = '',-1
        if t in boundaries:
            scene = boundaries[t]
            n,e,b,be,pr = -1,-1,'',-1,False
            if p['cenas_distintas']:
                duo,tmp = False,0
            recovered = 0
            if scene in rests:
                recovered = min(maximum-pe,maximum//4)
                pe += recovered
                r = recovery_max
            return mix((1.,turn(t+1,n,e,b,be,pr,duo,r,pe,tmp,c)),recovered=recovered)
        return turn(t+1,n,e,b,be,pr,duo,r,pe,tmp,c)

    @lru_cache(None)
    def slots(t,left,n,e,b,be,pr,duo,r,pe,tmp,c,used=False,closed=False,cond=(),carry=False):
        if left==0:
            return next_turn(t,n,e,b,be,pr,duo,r,pe,tmp,c)
        active = b if be>=t else ''
        def after(nn=n,ee=e,bb=b,bexp=be,pp=False,dd=duo,rr=r,
                  energy=pe,temporary=tmp,uu=used,cc=closed,co=cond):
            return slots(t,left-1,nn,ee,bb,bexp,pp,dd,rr,energy,temporary,c,uu,cc,co,False)
        args = dict(pressure=active=='pressionar',condition=cond,precision=pr)
        hit,damage = hit_info(**args)
        # Ferrão é escolhido antes da arma e é opcional. O feitiço acoplado
        # não usa o resultado nem o crítico da arma.
        if carry:
            damage = max(damage,hit_info(carried=True,**args)[1]+hit*c0)
        best = mix((1.,after()),value=damage)
        if closed or not path:
            return best
        if n<0:
            candidate = mix((hit,after(0,t+2,pp=cfg.school=='precisao')),
                            (1-hit,after()),value=damage+hit*(cfg.school_open_value-cfg.opening_mean_loss))
            best = max(best,candidate,key=lambda x:x[0])
        if n>=0 and not used:
            if pe+tmp>=cost_conduct:
                npe,ntmp,paid = charge(pe,tmp,cost_conduct)
                for label in conducts:
                    bb,bexp = (b,be) if label==active else ('',-1)
                    ph,dh = hit_info(pressure=bb=='pressionar' and be>=t,condition=cond,precision=pr)
                    magnitude = immediate_conduct.get(label,0.)
                    yes = after(min(2,n+1),t+2,bb=label,bexp=t+1,energy=npe,temporary=ntmp,uu=True)
                    no = after(-1,-1,bb=bb,bexp=bexp,energy=npe,temporary=ntmp,uu=True)
                    if r:
                        keep = after(bb=bb,bexp=bexp,energy=npe,temporary=ntmp,rr=r-1,uu=True)
                        no = max(no,keep,key=lambda x:x[0])
                    candidate = mix((ph,yes),(1-ph,no),value=dh+ph*magnitude,spent=paid)
                    best = max(best,candidate,key=lambda x:x[0])
            allowed = available(cfg,n,t)
            options = [(f,) for f in allowed]
            if n>=2 and not duo:
                options += list(combinations(allowed,2))
                if active=='explorar':
                    options += [pair[::-1] for pair in combinations(allowed,2)]
            for finish in options:
                dd = duo or len(finish)==2
                ph,dh = hit_info(finishes=finish,**args)
                branches = [(1-ph,after(-1,-1,dd=dd,uu=True,cc=True))]
                for prob,effects in resistance(cfg,finish,active=='explorar'):
                    nc = tuple(sorted(set(cond)|({'fixar','derrubada'}&set(effects))))
                    result = mix((1.,after(-1,-1,dd=dd,uu=True,cc=True,co=nc)),value=condition_value(effects,cfg))
                    branches.append((ph*prob,result))
                candidate = mix(*branches,value=dh)
                best = max(best,candidate,key=lambda x:x[0])
        return best

    @lru_cache(None)
    def turn(t,n,e,b,be,pr,duo,r,pe,tmp,c):
        assert 0<=pe<=maximum and tmp>=0 and 0<=r<=recovery_max
        if t>end:
            return BAD if fixed_seven and c else ZERO
        # Após o último descanso, energia acima de todos os gastos possíveis
        # restantes é irrelevante à decisão. A parcela gasta continua exata.
        bound=max_turn_cost*(end-t+1)
        if prune and t>last_rest_turn and pe>bound:
            return turn(t,n,e,b,be,pr,duo,r,bound,tmp,c)
        if fixed_seven and c>slots_at[t]:
            return BAD
        # Outros usos de bônus pertencem também à ficha sem a Trilha.
        best = mix((1.,slots(t,2,n,e,b,be,pr,duo,r,pe,tmp,c)),value=p['alternativa_bonus'])
        classes = (max(spells),) if fixed_seven else tuple(spells)
        for cl in classes:
            if fixed_seven and not c:
                continue
            cost,mean = spells[cl]
            if cost>pe+tmp:
                continue
            npe,ntmp,paid = charge(pe,tmp,cost)
            nc = c-1 if fixed_seven else c
            # Ambos os lados escolhem controle; seu valor próprio não é de Bote.
            pressure=b=='pressionar' and be>=t
            attack_gate,attack_damage=attack(replace(spellcfg,spell_damage=mean),pressure=pressure,spell=True)
            sd = mean*(spell_p+(1-spell_p)/2) if spell_tr else attack_damage
            for control in ((False,True) if kit else (False,)):
                # Classe 0 de condição não é presumida: o catálogo desta missão
                # só oferece Classe 0 de dano, conforme o orçamento cheio acima.
                if control and cl==0:
                    continue
                # O controle desta sensibilidade usa TR próprio; Pressionar
                # melhora ataques, não aumenta a falha nesse TR.
                control_reference=mean*(spell_p+(1-spell_p)/2) if spell_tr else attack(replace(spellcfg,spell_damage=mean),spell=True)[1]
                value = control_reference*control_fraction if control else sd
                main_gate=spell_p if control or spell_tr else attack_gate
                bonus = int(kit and cl>=minimum)
                count = 2 if bonus and control else bonus
                alternative = p['alternativa_bonus'] if not bonus else 0.
                candidate = mix((1.,slots(t,count,n,e,b,be,pr,duo,r,npe,ntmp,nc)),value=value+alternative,spent=paid)
                best = max(best,candidate,key=lambda x:x[0])
                if not kit or not conclusions or cl==0 or n<1:
                    continue
                for dd,refund,magnitude in spell_finishes(n,duo,b=='explorar' and be>=t):
                    success_tmp = max(ntmp,1) if refund else ntmp
                    # Pode renunciar ao segundo ataque de Bote e escolher Ferrão.
                    for k in ((1,2) if count==2 else (count,)):
                        no = slots(t,k,-1,-1,b,be,pr,dd,r,npe,ntmp,nc,True,True)
                        yes = slots(t,k,-1,-1,b,be,pr,dd,r,npe,success_tmp,nc,True,True,
                                    carry=ferron and bonus and k==1)
                        candidate = mix((main_gate,yes),(1-main_gate,no),value=value+alternative+main_gate*magnitude,spent=paid)
                        best = max(best,candidate,key=lambda x:x[0])
        return best

    result = turn(1,-1,-1,'',-1,False,False,recovery_max,maximum,0,7 if fixed_seven else -1)
    assert result[0]>-1e80, 'Missão inviável'
    out = dict(valor=result[0],pe_normal_gasto=result[1],pe_recuperado=result[2],
               saldo_final=maximum+result[2]-result[1],estados=turn.cache_info().currsize+slots.cache_info().currsize)
    next_turn.cache_clear(); turn.cache_clear(); slots.cache_clear()
    return out


def fingerprint():
    paths=list(ROOT.glob('*.py'))+[ROOT/'estocada-missao-premissas.json',ROOT/'estocada-compasso-pe-contas.json']
    paths+=list((ROOT/'referencia-jjk-project/sistema/05-material/livro/manual').glob('*.md'))
    paths.append(ROOT/'referencia-jjk-project/sistema/03-mecanica/19-dano-e-condicoes.md')
    return hashlib.sha256(b''.join(f.read_bytes() for f in sorted(paths))).hexdigest()


def run_job(job):
    model,p,spells,pe,cache = _WORKER
    path=cache/(hashlib.sha256(json.dumps(job).encode()).hexdigest()+'.json')
    if path.exists():
        return json.loads(path.read_text())
    profile_index,fights,rests,fraction,fixed,minimum=job
    profile=p['perfis'][profile_index]
    base=model['MELEE'] if profile['arma']=='Lâmina Longa' else model['REFERENCIA']
    cfg=replace(base,p_die=profile['acerto'],advantage=profile['vantagem'],movement=9.,
                external_slow=profile['fixar'],external_explorable=False,
                q_physical=p['falha_tr_adicional'],q_vigor=p['falha_tr_adicional'])
    r=solve(model,cfg,p,spells,pe['pe_maximo_depois'] if minimum is not None else pe['pe_maximo_antes'],
            fights,rests,kit=minimum is not None,minimum=minimum or 0,
            control_fraction=fraction,fixed_seven=fixed)
    path.write_text(json.dumps(r))
    return r


def main(model, publish=False, quick=False):
    global _WORKER
    p,spells,pe = sources(model)
    digest=fingerprint()
    cache=Path('/tmp/estocada-missao')/digest
    cache.mkdir(parents=True,exist_ok=True)
    _WORKER=(model,p,spells,pe,cache)
    plans=[]
    for i,profile in enumerate(p['perfis'][:1] if quick else p['perfis']):
        rests_list=p['descansos'][:1] if quick else (p['descansos'] if i==1 else [[],[1,2]])
        for rests in rests_list:
            for fraction in ([1] if quick or i!=1 else p['condicao_fracao_do_dano']):
                for fixed in ([True] if quick or i!=1 else [True,False]):
                    if not fixed and (rests not in ([],[1,2]) or fraction!=1):
                        continue
                    versions=[None,0] if fixed else [None,0,4,3]
                    plans.append((i,tuple(rests),fraction,fixed,versions))
    def job_for(i,fights,rests,fraction,fixed,minimum):
        # Sem Bote, controle com valor <= dano é dominado neste catálogo abstrato.
        return (i,tuple(fights),rests,fraction if minimum is not None else 0,fixed,minimum)
    jobs={job_for(i,fights,rests,fraction,fixed,minimum)
          for i,rests,fraction,fixed,versions in plans for fights in p['combates'] for minimum in versions}
    calculated={}
    with ProcessPoolExecutor(max_workers=4,mp_context=multiprocessing.get_context('fork')) as pool:
        futures={pool.submit(run_job,j):j for j in jobs}
        for future in as_completed(futures):
            j=futures[future]; calculated[j]=future.result()
            print('Missões calculadas',len(calculated),'/',len(jobs),j,round(calculated[j]['valor'],3),flush=True)
    results=[]
    for i,rests,fraction,fixed,versions in plans:
        sums={v:[calculated[job_for(i,fights,rests,fraction,fixed,v)] for fights in p['combates']] for v in versions}
        avg={v:{k:sum(r[k] for r in rows)/len(rows) for k in rows[0]} for v,rows in sums.items()}
        day=sum(map(sum,p['combates']))/len(p['combates'])
        gains={str(v):(avg[v]['valor']-avg[None]['valor'])/day/p['fatia'] for v in versions if v is not None}
        if 4 in avg:
            assert avg[0]['valor']+1e-8>=avg[3]['valor']>=avg[4]['valor']-1e-8
        results.append(dict(perfil=p['perfis'][i]['nome'],descansos_apos=list(rests),controle_fracao=fraction,
                            rotina='sete Classe 7' if fixed else 'Classes 0 a 7 livres',
                            fatias=gains,detalhes={str(v):r for v,r in avg.items()}))
    out=dict(fontes_sha256=digest,premissas=p,feiticos={str(k):v for k,v in spells.items()},resultados=results)
    if not quick:
        (ROOT/'estocada-missao-contas.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps([dict(perfil=r['perfil'],descansos=r['descansos_apos'],controle=r['controle_fracao'],rotina=r['rotina'],fatias=r['fatias']) for r in results],ensure_ascii=False,indent=2),flush=True)
    if publish:
        publish_report(out)
    return out


def report_lines(out):
    lines=['| Perfil | Descanso após combate | Controle / dano | Rotina | Atual | Mínimo Classe 4 | Mínimo Classe 3 |',
           '|---|---|---:|---|---:|---:|---:|']
    for r in out['resultados']:
        f=lambda k: format(r['fatias'][k],'.3f').replace('.',',') if k in r['fatias'] else 'igual ao atual'
        rests=', '.join(map(str,r['descansos_apos'])) or 'nenhum'
        lines.append(f"| {r['perfil']} | {rests} | {r['controle_fracao']} | {r['rotina']} | {f('0')} | {f('4')} | {f('3')} |")
    return '\n'.join(lines)


def publish_report(out):
    doc=ROOT/'RASCUNHO-revalidacao-estocada.md'
    start,end='<!-- inicio-missao-conjunta -->','<!-- fim-missao-conjunta -->'
    text=doc.read_text()
    assert text.count(start)==text.count(end)==1
    before,tail=text.split(start); _,after=tail.split(end)
    doc.write_text(before+start+'\n'+report_lines(out)+'\n'+end+after)


def verify(model):
    p,spells,pe=sources(model)
    cfg=replace(model['REFERENCIA'],p_die=p['perfis'][0]['acerto'],advantage=False,
                movement=9.,external_slow=False,external_explorable=False)
    def one(**kw):
        return solve(model,cfg,p,spells,kw.pop('maximum',pe['pe_maximo_depois']),[1],[],**kw)
    weapon=model['attack'](cfg)[1]
    spell=model['attack'](replace(cfg,p_die=p['acerto_feitico'],spell_damage=spells[7][1]),spell=True)[1]
    assert abs(spell-56.7)<1e-9, '21d8: acerto inclui os críticos'
    assert abs(one(path=False)['valor']-max(2*weapon,spell))<1e-9
    assert abs(one(kit=True,path=False,control_fraction=1)['valor']-(spell+2*weapon))<1e-9
    free=one(kit=True,path=False,maximum=0)['valor']
    restricted=one(kit=True,path=False,maximum=0,minimum=4)['valor']
    c0=model['attack'](replace(cfg,p_die=p['acerto_feitico'],spell_damage=spells[0][1]),spell=True)[1]
    assert abs(free-max(2*weapon,c0+weapon))<1e-9
    assert abs(restricted-max(2*weapon,c0))<1e-9
    assert one(kit=True,path=False,maximum=9,minimum=3)['valor']>one(kit=True,path=False,maximum=9,minimum=4)['valor']
    assert one(kit=True,path=False,minimum=0)['valor']==one(kit=True,path=False,minimum=4)['valor']
    for name in ('estocada-compasso.md','vanguarda-completo.md'):
        text=(ROOT/name).read_text()
        rule=next(line for line in text.splitlines() if '**Quando usar a ação Conjurar' in line)
        assert 'metade da maior Classe que você pode conjurar, arredondada para cima' in rule, 'Requisito de Compasso diverge da opção adotada'
    for kit in (False,True):
        a=solve(model,cfg,p,spells,30,[2],[],kit=kit,control_fraction=1,prune=True)
        b=solve(model,cfg,p,spells,30,[2],[],kit=kit,control_fraction=1,prune=False)
        assert abs(a['valor']-b['valor'])<1e-9, 'Poda mudou o valor exato'
    out=json.loads((ROOT/'estocada-missao-contas.json').read_text())
    assert out['fontes_sha256']==fingerprint(), 'Fontes mudaram; execute --missao novamente'
    doc=(ROOT/'RASCUNHO-revalidacao-estocada.md').read_text()
    actual=doc.split('<!-- inicio-missao-conjunta -->')[1].split('<!-- fim-missao-conjunta -->')[0]
    assert actual=='\n'+report_lines(out)+'\n', 'Tabela da missão diverge dos resultados'
    for r in out['resultados']:
        for v in r['detalhes'].values():
            assert v['saldo_final']>=-1e-8
        if '4' in r['fatias']:
            assert r['fatias']['0']+1e-8>=r['fatias']['3']>=r['fatias']['4']-1e-8
    print('TUDO OK — ações, crítico, PE, poda exata, Classe 0, arredondamento e tabela da missão.')
