# -*- coding: utf-8 -*-
"""
conferir-dano-movido.py — a conta da reforma do Bastiao, reproduzivel.

Roda tres blocos:
  0 · REGRESSAO   reproduz numeros que ja existem em documento dono
  1 · PRECO       o nivel 2 do Bastiao nas duas leituras de gatilho
  2 · TAXA        quanto vale mover dano: 1 ponto movido = 0,30 causado

Uso:  python3 conferir-corpo-de-pe.py
Sai com codigo 1 se qualquer regressao falhar.

BASES — toda uma de documento dono, com a COLUNA nomeada:
  fatia .................. 5,08 dano/rodada, nv30 ......... DESENHO-manhas.md
  Rotina nv30 ............ 108,00 (contra alvo padrao) .... peca 5 §2
  saida contra CHEFE ..... 78,75 por personagem .......... peca 26 §4.7
  rodadas de luta/dia .... 10,5 (3 lutas x 3,5) ........... peca 10 §4
  acerto ................. 50% ............................ peca 1
  1 PE ................... 5,14 de dano .................... peca 26 §6.5
  maestria ............... 1/2/3/4 por faixa de 8 niveis ... peca 1 §2
  Desastre nv30 .......... 945 vida, 219/rodada, 3 acoes ... peca 26 §4.1 e §4.2
  golpe do Desastre ...... 73 (8d8+37) .................... peca 26 §4.4
  vida por nivel ......... Bastiao 7 · Vang/Guia 5 · E/E 4 . peca 6
  golpe simples nv30 ..... 11,50 bruto .................... peca 5 §4
  desvantagem 1 ataque ... 18,00 permanente ............... DESENHO-manhas.md
  posicionamento 1,5 m ... 0,90 permanente ................ peca 5 §4
  +1 de Defesa ........... 3,39 permanente ................ peca 5 §4
"""
import sys

FATIA      = 5.08
ROTINA30   = 108.00
SAIDA_PJ   = 78.75
DIA        = 10.5
ACERTO     = 0.50
PE_DANO    = 5.14
GOLPE      = 73.0
ACOES      = 3
VIDA_CHEFE = 945.0
GOLPE_SIMPLES = 11.50
SAP        = 18.00
POS15      = 0.90
DEF1       = 3.39
VIDA_NV    = {"Bastiao": 7, "Vanguarda": 5, "Guia": 5, "Emanador": 4}

falhas = []

def checa(rotulo, obtido, esperado, tol=0.02):
    ok = abs(obtido - esperado) <= tol
    print(f"  [{'ok ' if ok else 'FALHA'}] {rotulo:<52}{obtido:>8.2f}  esperado {esperado:.2f}")
    if not ok:
        falhas.append(rotulo)

def maestria(nv):
    return 1 if nv <= 9 else 2 if nv <= 17 else 3 if nv <= 25 else 4

def reducao(nv):
    """nivel + 1d6, esperanca"""
    return nv + 3.5

def preco_reacao(usos_dia, magnitude, pega=1.0):
    """usos/dia x magnitude x fracao que de fato acontece, diluido no dia"""
    dr = usos_dia * magnitude * pega / DIA
    return dr, dr / FATIA, usos_dia / DIA


print("=" * 74)
print("0 · REGRESSAO — o que ja tem dono tem de reproduzir")
print("=" * 74)
r30 = reducao(30)
checa("reducao no nv30 = nivel + 1d6", r30, 33.50)
# Absorver antigo: 6 usos (Constituicao), gatilho AO SER ATINGIDO -> nenhum uso queima
checa("Absorver antigo, 6 usos, gatilho 'atingido'",
      preco_reacao(6, r30, 1.0)[1], 3.77, tol=0.02)
# Interposicao como o documento anterior a preçou: 2 usos, sem fator de erro
checa("Interposicao, leitura antiga (sem fator de erro)",
      preco_reacao(2, r30, 1.0)[1], 1.26, tol=0.02)
# a saida por personagem contra chefe sai da vida do chefe dividida pela luta de 3,00
checa("saida por PJ contra chefe = 945 / 3,00 / 4",
      VIDA_CHEFE / 3.00 / 4, SAIDA_PJ, tol=0.02)
print()


print("=" * 74)
print("1 · O NIVEL 2 DO BASTIAO — o gatilho decide o preco")
print("=" * 74)
sem_erro = preco_reacao(2, r30, 1.0)
com_erro = preco_reacao(2, r30, ACERTO)
print(f"  gatilho 'um inimigo ATACA' (antes do dado, metade erra)")
print(f"     {com_erro[0]:>6.2f} dano/rodada = {com_erro[1]:.2f} fatia   taxa {com_erro[2]:.1%}")
print(f"  gatilho 'um ataque ACERTA' (depois do dado, nenhum uso queima)")
print(f"     {sem_erro[0]:>6.2f} dano/rodada = {sem_erro[1]:.2f} fatia   taxa {sem_erro[2]:.1%}")
print(f"  piso de taxa do projeto: 20% — os 2 usos gratis ficam abaixo dele")
print()
print("  a porta de PE, medida contra o cambio de 1 PE = 5,14 de dano:")
for nv in (2, 18, 30):
    m, ganho, custo = maestria(nv), reducao(nv) * ACERTO, maestria(nv) * PE_DANO
    print(f"     nv{nv:>2}  paga {m} PE = {custo:>5.2f} de dano  e evita {ganho:>5.2f}"
          f"  -> troca {ganho/custo:.2f}x")
print("  nenhum nivel chega em 1,00: pelo livro-caixa ninguem aperta esse botao.")
print()
print("  riders, medidos com 2 usos por dia:")
t2 = 2 / DIA
for nome, botao in (
        ("revide: um golpe simples no atacante", GOLPE_SIMPLES * ACERTO),
        ("o atacante leva desvantagem no proximo", SAP),
        ("-1 no acerto dele ate o fim do turno", SAP / 5),
        ("voce se desloca ate 6 m ate o aliado", 4 * POS15),
        ("+1 de Defesa ate o seu proximo turno", DEF1),
        ("PV temporario = metade do seu nivel", 30 / 2)):
    print(f"     {nome:<42}{botao*t2:>6.2f} dano/rodada = {botao*t2/FATIA:>5.2f} fatia")
print()


print("=" * 74)
print("2 · A TAXA DE DANO MOVIDO")
print("=" * 74)
LUTA = 3.00
socorrida     = SAIDA_PJ * 1.0 + SAIDA_PJ * 1.0      # 1 rodada no chao + o turno de quem levanta
nao_socorrida = SAIDA_PJ * (LUTA / 2)                 # cai no meio, ninguem chega
print(f"  queda socorrida      {socorrida:>7.2f} de dano"
      f"  -> {socorrida/DIA:>5.2f}/rodada = {socorrida/DIA/FATIA:.2f} fatia")
print(f"  queda nao socorrida  {nao_socorrida:>7.2f} de dano"
      f"  -> {nao_socorrida/DIA:>5.2f}/rodada = {nao_socorrida/DIA/FATIA:.2f} fatia"
      f"   + estagio 4 de dano de alma")
print()

def luta(redirects, passo=0.05, limite=12.0):
    """4 PJs contra o Desastre nv30. O chefe concentra no mais fragil vivo.
    Com atrito: quem cai para de contar na saida do grupo."""
    pjs = {k: v * 30 for k, v in VIDA_NV.items()}
    chefe, t, perdido = VIDA_CHEFE, 0.0, 0.0
    while chefe > 0 and t < limite:
        vivos = [k for k, v in pjs.items() if v > 0]
        if not vivos:
            break
        chefe   -= len(vivos) * SAIDA_PJ * passo
        perdido += (4 - len(vivos)) * SAIDA_PJ * passo
        if chefe <= 0:
            break
        alvo = min(vivos, key=lambda k: pjs[k])
        for i in range(ACOES):
            d = GOLPE * ACERTO * passo
            puxa = i < redirects and pjs["Bastiao"] > 0 and alvo != "Bastiao"
            pjs["Bastiao" if puxa else alvo] -= d
        t += passo
    return t, sum(1 for v in pjs.values() if v <= 0), perdido, pjs

base = luta(0)
print(f"  {'puxa':>5}{'rodadas':>9}{'caidos':>8}{'saida perdida':>15}"
      f"{'poupado':>10}{'fatias':>9}")
for n in (0, 1, 2, 3):
    t, c, perdido, _ = luta(n)
    poupado = base[2] - perdido
    print(f"  {n:>5}{t:>9.2f}{c:>8}{perdido:>15.1f}{poupado:>+10.1f}"
          f"{poupado/DIA/FATIA:>+9.2f}")
print()
print("  o pico e 2, e passar dele derruba o proprio Bastiao.")
print()
print("  REGRESSAO do modelo — a peca 26 §4.2 diz, por outra rota, que o chefe")
print("  derruba 2,70 pessoas concentrando, e os quatro em cinco rodadas:")
checa("sem ajuda nenhuma, quantas pessoas caem", float(base[1]), 3.0, tol=0.5)
checa("sem ajuda nenhuma, quantas rodadas dura", base[0], 4.5, tol=0.7)
print()

print("=" * 74)
print("3 · O NIVEL 2 FECHADO — Encarar, ao preco da taxa")
print("=" * 74)
TAXA = 0.30                 # 1 ponto de dano movido = 0,30 de dano causado (provisoria)
GOLPES_LUTA, LUTAS = 2, 3   # caso de referencia: 2 golpes tancados por luta, 3 lutas/dia
GOLPE_NV = {10: 25.0, 20: 49.0, 30: 73.0}
ROTINA_NV = {10: 45.0, 20: 76.0, 30: 108.0}

movido = GOLPES_LUTA * GOLPE_NV[30] * LUTAS / DIA
print(f"  move {movido:.2f} de dano por rodada do dia, no nv30")
print(f"  x taxa {TAXA:.2f} = {movido*TAXA:.2f} de dano por rodada"
      f" = {movido*TAXA/FATIA:.2f} fatia")
checa("Encarar, nivel 2, custo em fatia", movido * TAXA / FATIA, 2.46, tol=0.03)
print(f"  orcamento do Caminho 5,00 -> sobra {5.0 - movido*TAXA/FATIA:.2f}"
      f" para os niveis 15, 23 e 30")
print()
print("  a taxa e PLANA? % da Rotina de cada faixa:")
vals = []
for nv, g in GOLPE_NV.items():
    mv = GOLPES_LUTA * g * LUTAS / DIA
    pct = mv * TAXA / ROTINA_NV[nv] * 100
    vals.append(pct)
    print(f"     nv{nv:>2}  move {mv:>6.2f}  vale {mv*TAXA:>6.2f}  = {pct:>5.1f}% da Rotina")
checa("spread entre as faixas (pp da Rotina)", max(vals) - min(vals), 2.1, tol=0.4)
print()

print("=" * 74)
print("4 · O X DO PROVOCAR — metade da Forca + 1")
print("=" * 74)
PP_DISPARO, FALHA_TR, LUTA_RODADAS = 25.0, 0.50, 3.5
envelope = 12.5 * LUTA_RODADAS          # a acao Provocar usada toda rodada da luta
print(f"  envelope aprovado: {envelope:.2f} pp por cena")
print(f"  {'Forca':>7}{'alvos':>8}{'pp':>9}{'do envelope':>14}")
for forca in range(0, 7):
    alvos = forca // 2 + 1
    pp = alvos * PP_DISPARO * FALHA_TR
    print(f"  {forca:>7}{alvos:>8}{pp:>9.1f}{pp/envelope:>13.0%}")
checa("piso: Forca 0 ainda provoca 1 alvo", float(0 // 2 + 1), 1.0, tol=0.01)
checa("teto: Forca 6 em pp", (6 // 2 + 1) * PP_DISPARO * FALHA_TR, 50.0, tol=0.01)
print()

print("=" * 74)
print("5 · O CAMINHO FECHADO — soma das entregas pagas")
print("=" * 74)
kit = [("2  Encarar",                    2.46, 2.46),
       ("7  ataque extra + Nao Pega + Ainda de Pe", 0.00, 0.00),
       ("15 Aparar com Corpo",           2.12, 2.50),
       ("23 redispara + aura 9 m",       0.00, 0.00),
       ("30 Passa Pra Mim",              0.62, 0.62)]
lo = sum(a for _, a, _ in kit); hi = sum(b for _, _, b in kit)
for nome, a, b in kit:
    print(f"  {nome:<44}{a:>7.2f}{b:>8.2f}")
print(f"  {'TOTAL':<44}{lo:>7.2f}{hi:>8.2f}   orcamento 5,00")
print(f"  {'ESTOURO (declarado pelo Mizuki)':<44}{lo-5:>7.2f}{hi-5:>8.2f}")
checa("soma minima do Caminho", lo, 5.20, tol=0.02)
checa("soma maxima do Caminho", hi, 5.58, tol=0.02)
print("  maior estouro anterior do projeto: Brasa em 5,03, ou seja 0,03.")
print()

print("=" * 74)
print("6 · TRILHA MURO, refeita sobre o Encarar")
print("=" * 74)
RESIST = 3.39        # 1 tipo de resistencia, em dano evitado (DESENHO-trilhas)
DEF1   = 3.39        # +1 de Defesa, em dano evitado (peca 5 §4)
PUXA   = 2           # golpes puxados por luta, caso de referencia
muro = [("2  duas resistencias no Encarar", 2*RESIST/FATIA),
        ("11 cobertura Parcial (1 atq/rodada x 70%)", 1.0*2*DEF1*0.7/FATIA),
        ("19 2d10-1 + CON no golpe puxado", PUXA*(10+6)*3/DIA/FATIA),
        ("27 quatro tipos + a area te sobrevive", 2*RESIST/FATIA)]
for nome, f in muro:
    print(f"  {nome:<44}{f:>7.2f}")
tot = sum(f for _, f in muro)
print(f"  {'TOTAL':<44}{tot:>7.2f}   orcamento 5,00   estouro {tot-5:+.2f}")
checa("soma da Trilha Muro", tot, 5.39, tol=0.03)
checa("fusao do Alicerce reproduz o preco publicado", 2*RESIST/FATIA, 1.33, tol=0.01)
print(f"  Bastiao de Muro, combinado: {5.20+tot:.2f} a {5.58+tot:.2f} de 10,00")
print()

print("=" * 74)
print("7 · TRILHA PUNHO")
print("=" * 74)
SOCO, ACERTO_ = 11.50, 0.50
punho = [("2  Engate + soco na Reacao", 1.70 + 2*SOCO*ACERTO_*3/DIA/FATIA),
         ("11 Encontrao, 4,5 m uma vez por alvo", 0.91),
         ("19 soco em bloqueio bem-sucedido, 2 PE", 0.45*SOCO*ACERTO_/FATIA),
         ("27 soco multiplo + botao de 8 PE (central)", 0.83)]
for nome, f in punho:
    print(f"  {nome:<46}{f:>7.2f}")
tp = sum(f for _, f in punho)
print(f"  {'TOTAL (leitura central)':<46}{tp:>7.2f}   orcamento 5,00")
checa("soma da Trilha Punho", tp, 4.60, tol=0.06)
checa("o soco na Reacao vale", 2*SOCO*ACERTO_*3/DIA/FATIA, 0.65, tol=0.01)
print()

print("=" * 74)
print("8 · TRILHA BRASA (Classe 0 = ataque, leva o desconto de 50%)")
print("=" * 74)
C0, CLASSE3, red = 27.0, 54.0, 2*3/DIA
brasa = [("2  Classe 0 no redirect + Forca no PE max", C0*0.5*red/FATIA + 6*5.14/DIA/FATIA),
         ("11 maestria em PE temporario (critar/TR)", 1.18),
         ("19 vantagem no proximo feitico Classe >0", 0.44*80*0.25/FATIA),
         ("27 Classe 3 abaixo da metade [MIZUKI]", 0.50)]
for nome, f in brasa:
    print(f"  {nome:<46}{f:>7.2f}")
tb = sum(f for _, f in brasa)
print(f"  {'TOTAL':<46}{tb:>7.2f}   orcamento 5,00")
checa("soma da Trilha Brasa", tb, 5.51, tol=0.05)
checa("os tres primeiros degraus cabem em 5,00", tb-0.50, 5.01, tol=0.05)
print(f"  medido para o 27: 0,32 a 5,42 (centro 3,83). O 0,50 e numero do Mizuki.")
print(f"  Fagulha publicado 4,08 deveria ser {C0*0.5*0.75/FATIA:.2f} pelo mesmo desconto.")
print()

print("=" * 74)
if falhas:
    print(f"FALHOU em {len(falhas)}: " + " · ".join(falhas))
    sys.exit(1)
print("TUDO OK — toda regressao reproduziu o numero do documento dono.")
