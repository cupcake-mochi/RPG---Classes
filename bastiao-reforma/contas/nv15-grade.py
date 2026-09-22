# -*- coding: utf-8 -*-
"""Grade (escala x teto) pro nivel 15 'a reducao e o que voce rolou'."""
from itertools import product
FATIA, DIA, LUTAS, RODADAS = 5.08, 10.5, 3, 3.5
GOLPE={10:25.,20:49.,30:73.}; MAEST={10:2,20:3,30:4}
dist={}
for a,b in product(range(1,11),repeat=2):
    v=a+b-1; dist[v]=dist.get(v,0)+1
tot=sum(dist.values()); T=11
falhas={v:c for v,c in dist.items() if v<T}
E=sum(v*c for v,c in falhas.items())/sum(falhas.values())   # 7,00
P=sum(falhas.values())/tot                                   # 55%
def evit(d): return d/DIA/FATIA

# com teto de 1 por rodada e N ataques, voce pega a MELHOR falha da rodada
import random
random.seed(7)
def E_melhor(n, amostras=200000):
    vals=[v for v,c in dist.items() for _ in range(c)]
    s=0; k=0
    for _ in range(amostras):
        f=[random.choice(vals) for _ in range(n)]
        f=[x for x in f if x<T]
        if f: s+=max(f); k+=1
    return (s/k if k else 0), k/amostras

print("="*78); print("GRADE — fatia no nv30, por escala e por teto")
print("="*78)
escalas=[("so a rolagem", 0), ("rolagem + maestria", 4), ("rolagem + maestria x2", 8),
         ("rolagem + Constituicao", 6)]
print(f"  {'escala':<26}{'magn.':>7}{'sem teto':>10}{'1x/rodada':>11}"
      f"{'% do golpe nv30':>17}")
for atq in (2,3):
    Em, p_rod = E_melhor(atq)
    print(f"\n  --- com {atq} ataques mirados nele por rodada ---")
    for nome, add in escalas:
        sem = evit(atq*P*RODADAS*(E+add)*LUTAS)
        um  = evit(p_rod*RODADAS*(Em+add)*LUTAS)
        print(f"  {nome:<26}{E+add:>7.1f}{sem:>10.2f}{um:>11.2f}"
              f"{(E+add)/GOLPE[30]:>16.0%}")
print()
print(f"  (com teto, voce fica com a MELHOR falha da rodada: media {E_melhor(3)[0]:.2f}"
      f" com 3 ataques, contra {E:.2f} de uma so)")
print()
print("="*78); print("ESCALA AO LONGO DOS NIVEIS — rolagem + maestria")
print("="*78)
print(f"  {'nv':>4}{'golpe':>8}{'maestria':>10}{'reducao':>10}{'% do golpe':>13}")
for nv in (10,20,30):
    m=MAEST[nv]
    print(f"  {nv:>4}{GOLPE[nv]:>8.0f}{m:>10}{E+m:>10.1f}{(E+m)/GOLPE[nv]:>12.0%}")
print()
print("  36% -> 20% -> 15%. Encolhe menos que os 28% -> 10% da rolagem pura,")
print("  e a auto-limitacao sobrevive: rolagem ruim + maestria continua pequena.")
