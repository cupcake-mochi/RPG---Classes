# -*- coding: utf-8 -*-
"""
'Eu sou o problema agora' — o que a conta trava antes de a gente escolher a forma.
Bases (documento dono):
  Bastiao 7 vida/nivel · Vanguarda e Guia 5 · Emanador e Evocador 4   -> peca 6
  Desastre nv26-30: 219/rodada em 3 acoes, golpe 8d8+37 = 73          -> peca 26 §4.4
  Capanga nv26-30: 55/rodada em 1 acao                                -> peca 26 §4.4
  acerto 50% · luta 3,4 a 4,0 rodadas · Rotina nv30 = 108/PJ          -> peca 1, DESENHO-manhas
  quem cai tira um quarto da saida do grupo                           -> peca 26 §4.2
"""
ACERTO, ROTINA = 0.50, 108.0
GOLPE_CHEFE, ACOES_CHEFE = 73.0, 3
GOLPE_CAPANGA = 55.0

print("="*70)
print("1 · O TETO: quantos ataques o Bastiao aguenta comer por rodada")
print("="*70)
print(f"{'nivel':>6}{'vida':>7}{'1 ataque':>11}{'2 ataques':>11}{'3 ataques':>11}")
for nv in (10, 20, 30):
    vida = 7*nv
    # golpe do inimigo da faixa; so tenho a tabela do 26-30, entao escalo pela vida do PJ
    golpe = GOLPE_CHEFE * (vida/210)
    linha = f"{nv:>6}{vida:>7}"
    for n in (1,2,3):
        por_rodada = n * golpe * ACERTO
        linha += f"{vida/por_rodada:>10.1f}r"
    print(linha)
print()
print("  'r' = rodadas ate o Bastiao cair, so com o que ele redirecionou.")
print("  A luta dura 3,4 a 4,0 rodadas. Entao:")
print("    1 ataque por rodada -> ele sobrevive a luta")
print("    2 -> ele cai no fim")
print("    3 -> ele cai na metade, e ai o grupo perde o tanque E um quarto da saida")
print()

print("="*70)
print("2 · O MESMO TETO contra turba, que e onde a coisa quebra de verdade")
print("="*70)
vida = 210
for n_capangas in (2, 3, 4, 6):
    dano = n_capangas * GOLPE_CAPANGA * ACERTO
    print(f"  {n_capangas} capangas, um ataque cada, TODOS redirecionados: "
          f"{dano:>6.1f}/rodada -> {vida/dano:>4.1f} rodadas de vida")
print()
print("  Um estado que puxa TUDO mata o Bastiao mais rapido que ninguem puxar nada.")
print("  O teto tem de estar no lado DELE — quantos ele aceita por rodada —")
print("  e nao no lado do inimigo — quantos estao encarados.")
print()

print("="*70)
print("3 · QUANTO VALE MOVER DANO — o buraco que o projeto declara em aberto")
print("="*70)
# 4 PJs contra um Desastre. O chefe foca o de menor vida vivo.
def luta(redirects_por_rodada, rodadas_max=8):
    pjs = {"Bastiao":7*30, "Vanguarda":5*30, "Guia":5*30, "Emanador":4*30}
    vida_chefe, saida_total = 945.0, 0.0
    for r in range(1, rodadas_max+1):
        vivos = [k for k,v in pjs.items() if v > 0]
        if not vivos or vida_chefe <= 0: break
        saida_total += len(vivos) * ROTINA
        vida_chefe -= len(vivos) * ROTINA
        if vida_chefe <= 0: break
        # o chefe foca o mais fragil vivo
        alvo = min(vivos, key=lambda k: pjs[k])
        for a in range(ACOES_CHEFE):
            dano = GOLPE_CHEFE * ACERTO
            if a < redirects_por_rodada and pjs["Bastiao"] > 0 and alvo != "Bastiao":
                pjs["Bastiao"] -= dano
            else:
                pjs[alvo] -= dano
    caidos = sum(1 for v in pjs.values() if v <= 0)
    return r, caidos, saida_total, pjs

for n in (0, 1, 2, 3):
    r, caidos, saida, pjs = luta(n)
    est = " · ".join(f"{k[:4]} {max(0,v):.0f}" for k,v in pjs.items())
    print(f"  {n} redirect/rodada: luta em {r} rodadas, {caidos} caido(s), "
          f"saida {saida:.0f}  [{est}]")
print()
print("  O ganho nao aparece em dano evitado — aparece em gente de pe no fim.")
