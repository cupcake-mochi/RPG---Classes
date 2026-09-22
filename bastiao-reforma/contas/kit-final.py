# -*- coding: utf-8 -*-
"""Fechamento do Caminho do Bastiao — soma das quatro entregas pagas."""
ORC = 5.00
linhas = [
 ("2  · Encarar",                      2.46, 2.46, "dano movido x 0,30"),
 ("7  · ataque extra + Nao Pega + Ainda de Pe", 0.00, 0.00, "gratis: correcao de base"),
 ("15 · a reducao e o que voce rolou",  1.18, 1.43, "dano evitado 1 pra 1"),
 ("23 · Provocar redispara + aura 9 m", 0.00, 0.00, "regua de pontos percentuais"),
 ("30 · o aliado fica com 1, voce leva o excedente", 0.62, 0.62, "dano movido x 0,30"),
]
lo = sum(a for _,a,_,_ in linhas); hi = sum(b for _,_,b,_ in linhas)
print("="*80)
print(f"  {'degrau':<48}{'min':>7}{'max':>8}   regua")
print("-"*80)
for nome, a, b, reg in linhas:
    print(f"  {nome:<48}{a:>7.2f}{b:>8.2f}   {reg}")
print("-"*80)
print(f"  {'TOTAL':<48}{lo:>7.2f}{hi:>8.2f}")
print(f"  {'ORCAMENTO':<48}{ORC:>7.2f}{ORC:>8.2f}")
print(f"  {'SOBRA':<48}{ORC-lo:>7.2f}{ORC-hi:>8.2f}")
print("="*80)
print()
print("  A faixa do nivel 15 e a discordancia de frequencia: 2 ou 3 ataques")
print("  mirados nele por rodada. Nao muda o veredito — cabe nas duas leituras.")
print()
print("  Calendario combinado com a Trilha (2/11/19/27) e o 7 gratis:")
print("     2 · 7 · 11 · 15 · 19 · 23 · 27 · 30")
print("     vaos de 5 · 4 · 4 · 4 · 4 · 4 · 3 — sem buraco em lugar nenhum")
