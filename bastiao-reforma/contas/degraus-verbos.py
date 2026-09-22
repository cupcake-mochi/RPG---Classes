# -*- coding: utf-8 -*-
"""Cardapio para aguentar / prender / o do meio. Bases de dono:
  fatia 5,08 · dia 10,5 rodadas · 3 lutas/dia · golpe do Desastre nv30 = 73
  dano EVITADO conta 1 pra 1 (reducao, resistencia, PV temporario)
  dano MOVIDO conta 0,30 (taxa desta reforma)
  Alicerce, 1 tipo de resistencia = 3,39 dano/rodada ......... DESENHO-trilhas
  caso de referencia: o Bastiao puxa 2 golpes por luta
  SOBRA para 15/23/30 = 2,54 fatia
"""
FATIA, DIA, LUTAS, GOLPE = 5.08, 10.5, 3, 73.0
TAXA_MOVIDO, SOBRA, NV = 0.30, 2.54, 30
PUXADOS_LUTA = 2

def evitado(por_dia):      return por_dia / DIA / FATIA          # 1 pra 1
def movido(golpes_luta):   return golpes_luta*GOLPE*LUTAS/DIA*TAXA_MOVIDO/FATIA

print("="*76); print("AGUENTAR — regua de dano evitado, 1 pra 1, SEM o desconto de 0,30")
print("="*76)
ag = [
 ("reducao nivel+1d6 (33,5), 1 uso por dia",        evitado(1*33.5)),
 ("reducao nivel+1d6, 2 usos por dia",              evitado(2*33.5)),
 ("reducao nivel+1d6 em TODO golpe que voce puxou", evitado(PUXADOS_LUTA*33.5*LUTAS)),
 ("reducao = sua Constituicao (6) em todo golpe puxado", evitado(PUXADOS_LUTA*6*LUTAS)),
 ("reducao = maestria x 1d6 (14) em todo golpe puxado",  evitado(PUXADOS_LUTA*14*LUTAS)),
 ("resistencia a 1 tipo, sempre ligada",            3.39/FATIA),
 ("PV temporario = metade do nivel, ao entrar no Encarar", evitado(15*LUTAS)),
 ("PV temporario = seu nivel, ao entrar no Encarar",      evitado(30*LUTAS)),
]
for n,f in ag: print(f"  {n:<52}{f:>6.2f}{'   CABE' if f<=1.0 else ''}")
print()

print("="*76); print("PRENDER — controle nao tem conversao... exceto quando ele MOVE dano")
print("="*76)
pr = [
 ("Segurar como esta no livro (Reacao, agarra ou derruba)", None),
 ("quem te acerta fica Agarrado, sem rolagem",              None),
 ("quem voce agarrou nao ataca OUTRA pessoa (= redirect)",  movido(1.0)),
 ("quem voce provocou nao sai da sua area",                 None),
 ("agarrar deixa de custar Reacao e vira Acao Livre",       None),
]
for n,f in pr:
    print(f"  {n:<54}" + (f"{f:>6.2f}" if f is not None else f"{'sem regua':>10}"))
print()
print("  So a terceira tem preco, e por um motivo: impedir alguem de atacar outro")
print("  e mover dano por outro caminho. As outras sao posicionamento puro,")
print("  que continua sendo a lacuna aberta do projeto.")
print()

print("="*76); print("O DO MEIO — crescer o Encarar, com portao")
print("="*76)
me = [
 ("2o redirect, so contra quem voce provocou", movido(1.0)),
 ("2o redirect, 1x por cena",                  movido(1.0)),
 ("2o redirect, abaixo de metade da vida",     movido(0.7)),
 ("o redirect passa a pegar area",             movido(0.8)),
 ("o Provocar redispara quando alguem entra",  0.0),
 ("aura 6 m -> 9 m",                           0.0),
]
for n,f in me: print(f"  {n:<52}{f:>6.2f}")
print()

print("="*76); print("QUATRO MONTAGENS QUE FECHAM EM 2,54")
print("="*76)
mont = [
 ("I  · os tres verbos, redirect no meio",
  [("15 aguentar: reducao = Constituicao no golpe puxado", evitado(PUXADOS_LUTA*6*LUTAS)),
   ("23 encarar: 2o redirect so contra provocado",         movido(1.0)),
   ("30 prender: agarrado nao ataca outra pessoa",         movido(1.0))]),
 ("II · aguentar forte, prender de graca no fim",
  [("15 aguentar: reducao nivel+1d6, 2 usos por dia",      evitado(2*33.5)),
   ("23 encarar: Provocar redispara + aura 9 m",           0.0),
   ("30 prender: agarrado nao ataca outra pessoa",         movido(1.0))]),
 ("III· PV temporario como o aguentar",
  [("15 aguentar: PV temp = metade do nivel ao entrar",    evitado(15*LUTAS)),
   ("23 encarar: 2o redirect abaixo de metade da vida",    movido(0.7)),
   ("30 prender: agarrado nao ataca outra pessoa",         movido(1.0))]),
 ("IV · resistencia como o aguentar",
  [("15 aguentar: resistencia a 1 tipo, sempre",           3.39/FATIA),
   ("23 encarar: 2o redirect 1x por cena",                 movido(1.0)),
   ("30 prender: agarrado nao ataca outra pessoa",         movido(1.0))]),
]
for letra, linhas in mont:
    tot = sum(f for _,f in linhas)
    print(f"  {letra}")
    for n,f in linhas: print(f"     {n:<50}{f:>6.2f}")
    print(f"     {'TOTAL':<50}{tot:>6.2f}   sobra {SOBRA-tot:+.2f}\n")
