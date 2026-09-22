# -*- coding: utf-8 -*-
"""Calibragem do nivel 2: puxar UM golpe por rodada, sem reducao, nos tres niveis
que a peca 26 §4.1 publica. Pergunta: o Bastiao atravessa a luta, e sente?"""
CHEFE = {10:(390.,75.), 20:(660.,147.), 30:(945.,219.)}
ACOES, ACERTO = 3, 0.50
print(f"{'nv':>4}{'vida Bast.':>12}{'golpe':>8}{'luta':>7}{'come/rod':>10}"
      f"{'total':>8}{'sobra':>8}{'% da vida':>11}")
for nv,(vc,dr) in CHEFE.items():
    vida, golpe = 7*nv, dr/ACOES
    saida_pj = vc/3.00/4                 # a luta base dura 3,00 rodadas
    luta = 3.00
    come = golpe*ACERTO
    total = come*luta
    print(f"{nv:>4}{vida:>12.0f}{golpe:>8.1f}{luta:>7.2f}{come:>10.1f}"
          f"{total:>8.1f}{vida-total:>8.1f}{total/vida:>10.0%}")
print()
print("A fracao da vida que ele gasta e praticamente a mesma nos tres niveis,")
print("entao a peca nao precisa de tabela por faixa: a regra e uma so.")
print()
print("TESTE DE BONUS AUTOMATICO — puxar e sempre de graca?")
for nv,(vc,dr) in CHEFE.items():
    vida, golpe = 7*nv, dr/ACOES
    for n in (1,2,3):
        r = vida/(n*golpe*ACERTO)
        marca = "  cai na luta" if r < 4.0 else ""
        print(f"  nv{nv:>2}  puxando {n}: aguenta {r:>4.1f} rodadas{marca}")
