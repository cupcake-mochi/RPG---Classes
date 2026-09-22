# -*- coding: utf-8 -*-
"""Preco completo do 'Bloquear sozinho': a reducao E o que voce rolou.
Bases: Bloquear = 2d10-1 no lugar do 10 (peca 23 §2) · Defesa = 10 + Destreza + protecao
       fatia 5,08 · dia 10,5 · 3 lutas · luta 3,5 rodadas
       golpe do Desastre: nv10 25 · nv20 49 · nv30 73
       maestria 1/2/3/4 · Destreza ate 6 · protecao ate 4 (peca 14)
"""
from itertools import product
FATIA, DIA, LUTAS, RODADAS = 5.08, 10.5, 3, 3.5
GOLPE = {10:25.0, 20:49.0, 30:73.0}
MAEST = {10:2, 20:3, 30:4}
def evit(d): return d/DIA/FATIA

dist={}
for a,b in product(range(1,11),repeat=2):
    v=a+b-1; dist[v]=dist.get(v,0)+1
tot=sum(dist.values())

def cond(T):
    """media do 2d10-1 e taxa de falha, dado um alvo T (ataque - modificadores)"""
    f={v:c for v,c in dist.items() if v<T}
    n=sum(f.values())
    return (sum(v*c for v,c in f.items())/n if n else 0), n/tot

print("="*76); print("1 · A PROPRIEDADE QUE FAZ ELA SE SEGURAR SOZINHA")
print("="*76)
print(f"  {'quanto o ataque supera seus mods':<34}{'falha':>8}{'E[rolagem|falha]':>19}")
for T in (7, 9, 11, 13, 15):
    e,p = cond(T)
    print(f"  precisa tirar {T:>2} ou mais{'':<15}{p:>7.0%}{e:>19.2f}")
print()
print("  Quanto mais dificil o bloqueio, MAIS voce falha e MENOS voce reduz.")
print("  A condicional desconta sozinha: nenhuma outra variante faz isso.")
print()

print("="*76); print("2 · PRECO — 'a reducao e o 2d10-1 que voce rolou', SEM TETO")
print("="*76)
E, P = cond(11)          # caso parelho: 55% de falha, media 7,00 na falha
print(f"  caso parelho: falha {P:.0%}, reducao media na falha {E:.2f}\n")
print(f"  {'ataques mirados nele/rodada':<32}{'falhas/cena':>13}{'fatia':>9}")
for atq in (1,2,3):
    fc = atq*P*RODADAS
    print(f"  {atq:<32}{fc:>13.2f}{evit(fc*E*LUTAS):>9.2f}")
print(f"\n  orcamento do degrau: 0,85 a 1,26")
print()

print("="*76); print("3 · SE SOMAR OS MODIFICADORES (reducao = o Bloquear inteiro)")
print("="*76)
for nv in (10,20,30):
    mods = min(6, 2+nv//10) + min(4, 1+nv//10)      # Destreza + protecao plausiveis
    print(f"  nv{nv:>2}: mods ~{mods} -> reducao media na falha {E+mods:>5.2f}"
          f"  = {(E+mods)/GOLPE[nv]:>4.0%} do golpe"
          f"  -> {evit(3*P*RODADAS*(E+mods)*LUTAS):>5.2f} fatia (3 atq/rodada)")
print()

print("="*76); print("4 · O ENCOLHIMENTO, e tres escalas que o seguram")
print("="*76)
print(f"  {'variante':<28}" + "".join(f"{'nv'+str(n):>10}" for n in (10,20,30))
      + f"{'fatia nv30':>12}")
for nome, fn in (("so a rolagem", lambda nv: E),
                 ("rolagem + Constituicao", lambda nv: E+6),
                 ("rolagem x maestria", lambda nv: E*MAEST[nv]),
                 ("rolagem + metade do nivel", lambda nv: E+nv/2)):
    linha=f"  {nome:<28}"
    for nv in (10,20,30):
        linha += f"{fn(nv)/GOLPE[nv]:>9.0%} "
    linha += f"{evit(3*P*RODADAS*fn(30)*LUTAS):>11.2f}"
    print(linha)
print()
print("  'rolagem x maestria' e a mais plana das que escalam, e a unica que")
print("  preserva a auto-limitacao: rolagem ruim x 4 continua ruim.")
