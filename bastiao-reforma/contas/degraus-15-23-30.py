# -*- coding: utf-8 -*-
"""O que cabe nos niveis 15, 23 e 30 do Bastiao.
Unidade do projeto: golpe tancado por luta, x taxa de dano movido.
  base do nivel 2 = 2 golpes por luta = 2,46 fatia
  golpe do Desastre nv30 = 73 · 3 lutas/dia · 10,5 rodadas/dia · fatia 5,08
  taxa de dano movido = 0,30 (provisoria)
"""
FATIA, DIA, LUTAS, GOLPE, TAXA = 5.08, 10.5, 3, 73.0, 0.30
ORC, NV2 = 5.00, 2.46

def por_golpes(n):
    """n golpes tancados por luta -> fatia"""
    return n * GOLPE * LUTAS / DIA * TAXA / FATIA

print("="*72)
print("1 · O QUE SOBRA, E O QUE ISSO SIGNIFICA")
print("="*72)
sobra = ORC - NV2
print(f"  orcamento do Caminho     {ORC:.2f}")
print(f"  nivel 2 (Encarar)       -{NV2:.2f}")
print(f"  sobra para 15/23/30      {sobra:.2f}   = {sobra/3:.2f} por degrau se dividir igual")
print()
print(f"  1 golpe tancado a mais por luta custa {por_golpes(1):.2f} fatia")
print(f"  -> a sobra inteira compra {sobra/por_golpes(1):.2f} golpe por luta, nos TRES degraus juntos")
print()
print("  Comparacao: o capstone do Guia (Ninguem Cai) vale ~1,26 de um orcamento")
print("  de 3,00, ou seja 42% do Caminho dele. Aqui um capstone de 1,26 seria 25%.")
print()

print("="*72)
print("2 · CANDIDATOS, na unidade do projeto")
print("="*72)
cands = [
 ("segundo redirecionamento, SEM portao",        2.0),
 ("segundo redirecionamento, so contra provocado", 1.0),
 ("segundo redirecionamento, 1x por cena",        1.0),
 ("segundo redirecionamento abaixo de metade da vida", 0.7),
 ("o redirecionamento passa a pegar area (Explosao/Cone/Linha/Onda)", 0.8),
 ("o Provocar dispara de novo quando alguem ENTRA na area", 0.0),
 ("alcance da aura 6 m -> 9 m", 0.0),
]
print(f"  {'candidato':<52}{'golpes/luta':>12}{'fatia':>8}")
for nome, g in cands:
    print(f"  {nome:<52}{g:>+12.1f}{por_golpes(g):>8.2f}")
print()
print("  Os de 0,00 movem na regua de pontos percentuais, nao na de dano movido.")
print()

print("="*72)
print("3 · TRES MONTAGENS QUE FECHAM EM 2,54")
print("="*72)
montagens = [
 ("A", [("15 · Provocar redispara na entrada", 0.0),
        ("23 · 2o redirect so contra provocado", 1.0),
        ("30 · 2o redirect livre (substitui o 23)", 1.0)]),
 ("B", [("15 · 2o redirect 1x por cena", 1.0),
        ("23 · aura 9 m + Provocar redispara", 0.0),
        ("30 · 2o redirect livre", 1.0)]),
 ("C", [("15 · 2o redirect abaixo de metade da vida", 0.7),
        ("23 · redirect passa a pegar area", 0.8),
        ("30 · 2o redirect livre", 0.7)]),
]
for letra, linhas in montagens:
    tot = sum(por_golpes(g) for _, g in linhas)
    print(f"  montagem {letra}:")
    for nome, g in linhas:
        print(f"     {nome:<44}{por_golpes(g):>6.2f}")
    print(f"     {'TOTAL':<44}{tot:>6.2f}   sobra {sobra-tot:+.2f}")
    print()

print("="*72)
print("4 · TETO DE SOBREVIVENCIA — quantos golpes ele aguenta puxar por rodada")
print("="*72)
for n in (1,2,3):
    print(f"  puxando {n} por rodada no nv30: aguenta {210/(n*GOLPE*0.5):.1f} rodadas"
          f"{'  — CAI na luta de 3,4 a 4,0' if 210/(n*GOLPE*0.5) < 4.0 else ''}")
print()
print("  Um segundo redirect SEM portao mata o proprio Bastiao.")
print("  O portao nao e so orcamento: e o que faz o degrau ser jogavel.")
