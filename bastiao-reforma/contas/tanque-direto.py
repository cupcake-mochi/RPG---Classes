# -*- coding: utf-8 -*-
"""Preco do nivel 2 contado direto: o Bastiao toma 2 golpes numa luta de 3 rodadas.
Sem falar em queda. Bases de dono:
  golpe do Desastre por faixa .......... nv10 25 · nv20 49 · nv30 73   peca 26 §4.4
  vida por nivel ....................... Bastiao 7 · outros 5/5/4/4    peca 6
  3 lutas de graca por dia · 10,5 rodadas de luta no dia               peca 10 §4
  fatia ................................ 5,08 dano/rodada no nv30      DESENHO-manhas
  PV temporario e reducao contam 1 pra 1 com dano causado              reforma
"""
FATIA, DIA, LUTAS = 5.08, 10.5, 3
GOLPES_POR_LUTA = 2
GOLPE = {10: 25.0, 20: 49.0, 30: 73.0}

print("="*74)
print("1 · O TRABALHO BRUTO — quanto dano ele tira dos outros e poe em si")
print("="*74)
print(f"  {'nv':>4}{'golpe':>8}{'por luta':>11}{'por dia':>10}"
      f"{'/rodada':>10}{'% da vida dele':>16}")
for nv, g in GOLPE.items():
    luta = GOLPES_POR_LUTA * g
    dia  = luta * LUTAS
    print(f"  {nv:>4}{g:>8.0f}{luta:>11.0f}{dia:>10.0f}{dia/DIA:>10.2f}"
          f"{luta/(7*nv):>15.0%}")
print()
print("  Ele come entre 21% e 35% da propria vida por luta, so no que puxou.")
print()

print("="*74)
print("2 · EM FATIA — e o numero depende so de UMA taxa, que nao existe ainda")
print("="*74)
nv = 30
movido_rodada = GOLPES_POR_LUTA * GOLPE[nv] * LUTAS / DIA
print(f"  no nv30 ele move {movido_rodada:.2f} de dano por rodada do dia.\n")
print(f"  {'quanto vale 1 ponto movido':<46}{'fatia':>8}{'cabe em 1,25?':>15}")
for rot, taxa in (
    ("1,00 — igual a PV temporario e reducao", 1.00),
    ("0,43 — a diferenca de barra (1 - 120/210)", 1 - 120/210),
    ("0,30", 0.30),
    ("0,15", 0.15)):
    f = movido_rodada * taxa / FATIA
    print(f"  {rot:<46}{f:>8.2f}{'sim' if f<=1.25 else 'NAO':>15}")
print()

print("="*74)
print("3 · RESOLVENDO PELA OUTRA PONTA — que taxa faz o degrau caber?")
print("="*74)
for rot, alvo in (("1,25 — um quarto do Caminho, degrau parelho", 1.25),
                  ("2,50 — metade, porque ele carrega 13 niveis", 2.50),
                  ("5,00 — o Caminho inteiro e so tancar", 5.00)):
    taxa = alvo * FATIA / movido_rodada
    print(f"  pra custar {rot:<44} taxa = {taxa:.3f}")
print()
print("  A taxa e a peca que falta. Ela nao sai de conta — sai de decisao,")
print("  igual o 5,00 do Caminho saiu.")
print()

print("="*74)
print("4 · TESTE DE ESCALA — a mesma taxa serve nos tres niveis?")
print("="*74)
TAXA = 0.30
print(f"  fixando a taxa em {TAXA:.2f} e medindo o degrau em cada faixa:")
print(f"  {'nv':>4}{'move/rodada':>14}{'em dano':>10}{'fatia local':>14}")
for nv, g in GOLPE.items():
    mv = GOLPES_POR_LUTA * g * LUTAS / DIA
    # a fatia so foi definida no nv30; aqui mostro a proporcao contra a Rotina da faixa
    rotina = {10: 45.0, 20: 76.0, 30: 108.0}[nv]
    print(f"  {nv:>4}{mv:>14.2f}{mv*TAXA:>10.2f}{mv*TAXA/rotina*100:>13.1f}%")
print()
print("  ultima coluna = quanto por cento da Rotina daquela faixa o degrau vale.")
print("  Se as tres baterem, a taxa e plana e nao precisa de tabela por nivel.")
