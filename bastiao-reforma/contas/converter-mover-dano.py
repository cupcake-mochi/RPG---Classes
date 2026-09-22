# -*- coding: utf-8 -*-
"""
Fechar o buraco: quanto vale MOVER dano, em dano por rodada.
Bases, todas de documento dono:
  Rotina                 nv2 13 · nv10 45 · nv20 76 · nv30 108        peca 5 §2
  vida por nivel         Bastiao 7 · Vanguarda/Guia 5 · Eman/Evoc 4   peca 6
  Desastre               nv10 390·75 · nv20 660·147 · nv30 945·219    peca 26 §4.1
  acoes do Desastre      3                                            peca 26 §4.2
  acerto                 50%                                          peca 1
  fatia                  5,08 de dano por rodada, no nv30             DESENHO-manhas
ATENCAO: a peca 26 roda o modelo SEM atrito — quem cai continua contando.
Aqui o atrito entra, porque e a unica lente em que mover dano vale alguma coisa.
A propria peca ja mediu com atrito no §4.2; o que ela nao faz e orcar com ele.
"""
FATIA, ACERTO = 5.08, 0.50
ROTINA   = {10: 45.0, 20: 76.0, 30: 108.0}
CHEFE    = {10: (390.0, 75.0), 20: (660.0, 147.0), 30: (945.0, 219.0)}
ACOES    = 3
VIDA_NV  = {"Bastiao": 7, "Vanguarda": 5, "Guia": 5, "Emanador": 4}

def luta(nv, redirects, passo=0.1):
    """roda em passos de 0,1 rodada pra tirar a granularidade de rodada inteira"""
    vida_chefe, dano_chefe = CHEFE[nv]
    golpe = dano_chefe / ACOES
    pjs = {k: v*nv for k, v in VIDA_NV.items()}
    rot, saida, t = ROTINA[nv], 0.0, 0.0
    while vida_chefe > 0 and t < 20:
        vivos = [k for k, v in pjs.items() if v > 0]
        if not vivos: break
        saida      += len(vivos) * rot * passo
        vida_chefe -= len(vivos) * rot * passo
        if vida_chefe <= 0: break
        alvo = min(vivos, key=lambda k: pjs[k])          # o chefe concentra
        for a in range(ACOES):
            d = golpe * ACERTO * passo
            puxa = (a < redirects and pjs["Bastiao"] > 0 and alvo != "Bastiao")
            pjs["Bastiao" if puxa else alvo] -= d
        t += passo
    caidos = sum(1 for v in pjs.values() if v <= 0)
    return t, caidos, saida, pjs

print("="*78)
print("1 · A CURVA — quanto o grupo entrega, por quantos golpes o Bastiao puxa")
print("="*78)
for nv in (10, 20, 30):
    base_t, base_c, base_s, _ = luta(nv, 0)
    print(f"\n  nivel {nv}   (luta base: {base_t:.1f} rodadas, {base_c} caido(s), saida {base_s:.0f})")
    print(f"   {'puxa':>5}{'rodadas':>9}{'caidos':>8}{'saida':>9}{'ganho':>9}"
          f"{'/rodada':>9}{'fatias':>8}")
    for n in (0, 1, 2, 3):
        t, c, s, pjs = luta(nv, n)
        ganho = s - base_s
        por_r = ganho / t if t else 0
        # fatia so tem sentido no nv30, onde ela foi definida
        f = por_r / FATIA if nv == 30 else float('nan')
        fs = f"{f:>8.2f}" if nv == 30 else f"{'—':>8}"
        print(f"   {n:>5}{t:>9.1f}{c:>8}{s:>9.0f}{ganho:>+9.0f}{por_r:>+9.1f}{fs}")

print()
print("="*78)
print("2 · O MESMO, com o Bastiao gastando a propria vida — quanto sobra dele")
print("="*78)
for n in (0,1,2,3):
    t, c, s, pjs = luta(30, n)
    print(f"  puxa {n}: Bastiao termina com {max(0,pjs['Bastiao']):>5.0f} de 210"
          f"   ({max(0,pjs['Bastiao'])/210:>5.0%})"
          f"   Emanador {max(0,pjs['Emanador']):>5.0f} de 120")
print()
print("="*78)
print("3 · O TETO QUE ISSO IMPOE")
print("="*78)
print("  Se puxar 1 por rodada ja vale mais que uma fatia, um estado PERMANENTE")
print("  que puxa nao cabe num degrau de 1,25 — nem no Caminho inteiro de 5,00.")
print("  O que segura o preco nao pode ser o teto escrito; tem de ser o corpo.")
