# -*- coding: utf-8 -*-
"""Quanto cabe no nivel 2 do Bastiao, e o que cada 'rider' custa.
Bases (documento dono):
  fatia 5,08 · dia 10,5 rodadas · golpe simples nv30 = 11,50 (bruto)
  desvantagem no proximo ataque do alvo = 18,00 permanente (DESENHO-manhas, Sap)
  posicionamento +1,5 m = 0,90 permanente (peca 5 §4)
  +1 de Defesa = 3,39 permanente (peca 5 §4)
  acerto = 50% · golpe do Desastre nv30 = 73 · vida do Bastiao nv30 = 210
"""
FATIA, DIA, ACERTO = 5.08, 10.5, 0.50
NV = 30
RED = NV + 3.5                 # 33,5
GOLPE = 11.50
SAP  = 18.00                   # desvantagem em UM ataque do alvo, permanente
POS  = 0.90                    # por 1,5 m
DEF1 = 3.39

def taxa(usos): return usos / DIA
def fat(dr):    return dr / FATIA

print("=" * 72)
print("A · O CORPO DA HABILIDADE — magnitude x quantos usos")
print("=" * 72)
print(f"{'usos/dia':>9}{'taxa':>8} | " + "".join(f"{r:>9}" for r in
      ("nivel+1d6","2/3 dela","metade","um terco")))
mags = [RED, RED*2/3, RED/2, RED/3]
for u in (2,3,4,6,8,10.5):
    linha = f"{u:>9.1f}{taxa(u):>8.0%} | "
    for m in mags:
        linha += f"{fat(u*m/DIA):>9.2f}"
    print(linha)
print("  (cada celula = fatias que a habilidade inteira custa, gatilho 'ACERTA')")
print("  com gatilho 'ATACA' — antes do dado — divida tudo por 2.")
print()

print("=" * 72)
print("B · RIDERS — o que somar por cima, ao preco de 2 usos por dia")
print("=" * 72)
t = taxa(2)
riders = [
 ("revide: um golpe simples no atacante",      GOLPE*ACERTO),
 ("o atacante leva desvantagem no proximo",    SAP),
 ("-1 no acerto dele ate o fim do turno dele", SAP/5),
 ("voce se desloca ate 6 m ate o aliado",      4*POS),
 ("+1 de Defesa ate o seu proximo turno",      DEF1),
 ("PV temporario = metade do seu nivel",       NV/2),
]
for nome, botao in riders:
    dr = botao * t
    print(f"  {nome:<44}{dr:>7.2f} dano/rodada = {fat(dr):>5.2f} fatia")
print()
print("  o mesmo rider com o dobro de usos custa o dobro.")
print()

print("=" * 72)
print("C · TRES MONTAGENS, pra ver o que cabe em 1,25 fatia")
print("=" * 72)
montagens = [
 ("hoje (2 usos, gatilho ATACA, sem rider)",  2, RED, ACERTO, []),
 ("2 usos, gatilho ACERTA, sem rider",        2, RED, 1.0,   []),
 ("2 usos, ACERTA + revide",                  2, RED, 1.0,   [GOLPE*ACERTO]),
 ("2 usos, ACERTA + revide + desloca 6 m",    2, RED, 1.0,   [GOLPE*ACERTO, 4*POS]),
 ("4 usos, ACERTA, metade da magnitude",      4, RED/2, 1.0, []),
 ("4 usos, ACERTA, metade + revide",          4, RED/2, 1.0, [GOLPE*ACERTO]),
 ("1 por rodada, ACERTA, um terco da magn.",  DIA, RED/3, 1.0, []),
]
for nome, u, m, pg, rs in montagens:
    dr = u*m*pg/DIA + sum(r*taxa(u) for r in rs)
    print(f"  {nome:<42}{dr:>7.2f} dano/rodada = {fat(dr):>5.2f} fatia")
print()
print(f"  orcamento do Caminho: 5,00 fatia em 4 degraus = 1,25 de media")
print(f"  precedente do projeto: o nv2 do Guia leva 0,68 de uma media de 1,00 (68%)")
print(f"  68% de 1,25 = {0.68*1.25:.2f} fatia")
