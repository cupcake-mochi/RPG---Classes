# -*- coding: utf-8 -*-
# Quanto de VIDA do Bastiao cada leitura da Interposicao custa, no nv30.
# vida do Bastiao = 7/nivel -> 210.  Golpe do Desastre = 73, e ele tem 3 acoes.
VIDA, GOLPE, RED = 7*30, 73.0, 30+3.5
for n, rot in ((1,"um golpe"), (2,"dois golpes"), (3,"a Acao inteira")):
    bruto  = n*GOLPE
    sofre  = n*(GOLPE-RED)
    print(f"{rot:<16} redireciona {bruto:>6.1f}  voce sofre {sofre:>6.1f}  "
          f"= {sofre/VIDA:>5.1%} da sua vida   evita {n*RED:>5.1f}")
print()
print(f"vida do Bastiao no nv30: {VIDA}.  Chefe entrega 219 por rodada.")
print("Sem a Interposicao, um aliado de 4 vida/nivel (120) leva 73 e perde 61% da vida.")
