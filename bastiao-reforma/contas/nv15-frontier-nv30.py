# -*- coding: utf-8 -*-
"""Fronteira do nivel 15 pendurado no Bloquear, e preco do nivel 30 escolhido.
Bases: fatia 5,08 · dia 10,5 · 3 lutas · luta 3,5 rodadas · golpe 73 · CON max 6
       dano evitado 1 pra 1 · dano movido 0,30 · sobra depois do nv2 = 2,54
"""
FATIA, DIA, LUTAS, RODADAS, GOLPE, TAXA = 5.08, 10.5, 3, 3.5, 73.0, 0.30
def evit(dia_total): return dia_total/DIA/FATIA

print("="*76)
print("1 · QUANTAS FALHAS DE BLOQUEIO ELE TEM POR CENA — o gatilho nao e escasso")
print("="*76)
print("  O Encarar transfere o acerto SEM nova rolagem, entao golpe puxado NAO")
print("  se bloqueia. So conta ataque mirado nele. Mas o Provocar e o que traz")
print("  esses ataques — as duas metades do nivel 2 se conversam por aqui.\n")
for atq in (1, 2, 3):
    f_cena = atq * 0.5 * RODADAS
    print(f"  {atq} ataque mirado nele por rodada -> {f_cena:.1f} falhas por cena")
print()

print("="*76)
print("2 · FRONTEIRA — magnitude x teto por cena, medida com 3 ataques/rodada")
print("="*76)
mags = [("1d8", 4.5), ("1d8 + CON", 4.5+6), ("1d8 + maestria x2", 4.5+8),
        ("1d8 + metade do nivel", 4.5+15)]
tetos = [1, 2, 3, 4, "sem teto"]
falhas_nat = 3 * 0.5 * RODADAS       # 5,25 por cena
print(f"  {'magnitude':<24}" + "".join(f"{str(t):>10}" for t in tetos))
for nome, m in mags:
    linha = f"  {nome:<24}"
    for t in tetos:
        usos = falhas_nat if t == "sem teto" else min(t, falhas_nat)
        linha += f"{evit(usos*m*LUTAS):>10.2f}"
    print(linha)
print()
print(f"  orcamento do degrau: 0,85 se dividir a sobra em tres; ate 1,26 se o 30 for barato")
print(f"  teto de CON/2+1: CON 2 -> 2 · CON 4 -> 3 · CON 6 -> 4")
print(f"  falhas naturais por cena: {falhas_nat:.2f} — o teto MORDE em toda faixa de CON")
print()

print("="*76)
print("3 · O NIVEL 30 — aliado que cairia fica com 1, voce leva o excedente")
print("="*76)
# excedente medio: o aliado tinha X de vida, 0<X<golpe; excedente = golpe - X
exc = GOLPE/2
print(f"  excedente medio quando alguem cairia: metade do golpe = {exc:.1f}")
for vezes in (1, 2):
    movido_dia = vezes * exc * LUTAS
    f = movido_dia/DIA*TAXA/FATIA
    print(f"  {vezes}x por cena: move {movido_dia:.1f} por dia -> {f:.2f} fatia")
print()
print(f"  E o custo no corpo do Bastiao: {exc:.1f} de {7*30} = {exc/210:.0%} da vida dele,")
print(f"  de uma vez, fora de turno. Se o excedente derrubar ELE, ele cai.")
print()

print("="*76)
print("4 · TRES FECHAMENTOS")
print("="*76)
for nome, f15, f30 in (
    ("1d8 + CON, 2x por cena", evit(2*(4.5+6)*LUTAS), evit(1*exc*LUTAS*TAXA/1)*0+ (1*exc*LUTAS)/DIA*TAXA/FATIA),
    ("1d8 + CON, teto CON/2+1 (CON 6 = 4x)", evit(4*(4.5+6)*LUTAS), (1*exc*LUTAS)/DIA*TAXA/FATIA),
    ("1d8 + metade do nivel, 1x por cena", evit(1*(4.5+15)*LUTAS), (1*exc*LUTAS)/DIA*TAXA/FATIA)):
    tot = f15 + f30
    print(f"  15: {nome:<38}{f15:>6.2f}")
    print(f"  23: Provocar redispara + aura 9 m     {'':<14}{0.00:>6.2f}")
    print(f"  30: aliado fica com 1, 1x por cena    {'':<14}{f30:>6.2f}")
    print(f"      {'TOTAL':<42}{tot:>6.2f}   sobra {2.54-tot:+.2f}\n")
