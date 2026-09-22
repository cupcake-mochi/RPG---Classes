# -*- coding: utf-8 -*-
"""O 'conserto' funciona? Bloquear + metade do nivel como reducao."""
from itertools import product
FATIA, DIA, LUTAS, RODADAS = 5.08, 10.5, 3, 3.5
GOLPE = {10:25.0, 20:49.0, 30:73.0}
def evit(d): return d/DIA/FATIA

dist = {}
for a,b in product(range(1,11), repeat=2):
    v=a+b-1; dist[v]=dist.get(v,0)+1
tot=sum(dist.values()); T=11
falhas={v:c for v,c in dist.items() if v<T}
E_falha = sum(v*c for v,c in falhas.items())/sum(falhas.values())
p_falha = sum(falhas.values())/tot

print("="*74); print("1 · AS DUAS ESCALAS, e por que elas se afastam")
print("="*74)
print(f"  media do 2d10-1 quando falha: {E_falha:.2f}  (nunca muda: o dado e fixo)")
print(f"  {'nv':>4}{'golpe':>8}{'reducao = rolagem':>20}{'% do golpe':>13}")
for nv,g in GOLPE.items():
    print(f"  {nv:>4}{g:>8.0f}{E_falha:>20.2f}{E_falha/g:>12.0%}")
print()
print("  O Bloquear vive na escala da DEFESA (10 a 25 a campanha inteira).")
print("  O dano vive na escala do DANO (25 -> 73). As duas nunca se encontram.")
print()

print("="*74); print("2 · O CONSERTO, medido contra o que ele deveria consertar")
print("="*74)
nv=30; g=GOLPE[30]
opts=[("1d8 + metade do nivel",          4.5+15),
      ("Bloquear rolado + metade do nivel", E_falha+15),
      ("Bloquear rolado, sozinho",          E_falha),
      ("Bloquear rolado x maestria (4)",    E_falha*4)]
print(f"  {'variante':<36}{'magnitude':>11}{'sem teto':>11}{'1x/rodada':>12}")
for nome,m in opts:
    sem  = evit(3*p_falha*RODADAS*m*LUTAS)
    umpr = evit((1-(1-p_falha)**3)*RODADAS*m*LUTAS)
    print(f"  {nome:<36}{m:>11.2f}{sem:>11.2f}{umpr:>12.2f}")
print()
print("  O conserto e MAIOR que o original: 22,00 contra 19,50.")
print("  Ele nao barateia nada — ele troca 1d8 (media 4,5) por uma rolagem")
print("  de media 7,0, e ainda paga o custo de olhar dois numeros.")
print()

print("="*74); print("3 · O QUE A IDEIA ORIGINAL TINHA DE BOM, e o que sobra dela")
print("="*74)
print(f"  auto-limitada: rolagem ruim reduz pouco. E[falha] = {E_falha:.2f},")
print(f"  contra E[2d10-1] = 10,00 — a condicional ja desconta {1-E_falha/10:.0%}.")
print(f"  Sem contador, sem teto, sem 'uma vez por'.")
print(f"  Preco sozinha, sem teto nenhum, 3 ataques/rodada: "
      f"{evit(3*p_falha*RODADAS*E_falha*LUTAS):.2f} fatia")
print()
print("  Mas some no fim do jogo, e somar nivel pra consertar mata exatamente")
print("  a propriedade que fazia ela valer a pena.")
