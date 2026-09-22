# -*- coding: utf-8 -*-
"""Preco do nivel 2 fechado, nas tres reguas que o projeto usa.
Bases de dono:
  Provocar aprovado: 25 pp quando dispara, 12,5 pp medios/rodada, spread 1,67x
     filtro reprova em 3,0x .................................. DESENHO-caminhos.md
  vantagem / desvantagem = 25 pontos percentuais ............. peca 11
  acerto base = 50% .......................................... peca 1
  dano do inimigo por rodada, nv30: Desastre 219 · esquadrao 440 . peca 26 §4.1
  maestria 1/2/3/4 ........................................... peca 1 §2
  luta 3,5 rodadas · dia 10,5 rodadas · fatia 5,08 ........... peca 10, DESENHO-manhas
"""
PP_DISPARO, FALHA = 25.0, 0.50     # o alvo falha metade das vezes (teste disputado, base)
LUTA, DIA, FATIA = 3.5, 10.5, 5.08
LUTAS_DIA = 3
BASE_ACERTO = 0.50

def maestria(nv): return 1 if nv<=9 else 2 if nv<=17 else 3 if nv<=25 else 4

print("="*72)
print("1 · A REGUA EM QUE O PROVOCAR FOI APROVADO — pontos percentuais")
print("="*72)
acao = 12.5 * LUTA
print(f"  a acao Provocar, disponivel toda rodada: {12.5} pp/rodada"
      f" x {LUTA} = {acao:.2f} pp por cena")
print()
print(f"  {'nv':>4}{'maestria':>10}{'X = maestria':>15}{'X = todos (8)':>16}")
for nv in (2,10,18,30):
    m = maestria(nv)
    print(f"  {nv:>4}{m:>10}{m*PP_DISPARO*FALHA:>14.1f} pp{8*PP_DISPARO*FALHA:>15.1f} pp")
print()
print(f"  envelope aprovado por cena: {acao:.2f} pp")
print()

print("="*72)
print("2 · EM DANO — e aqui a intuicao inverte")
print("="*72)
print("  O bestiario orca o DANO TOTAL do encontro, nao o numero de corpos.")
print("  Entao provocar 'todos' pega sempre metade do total; provocar 'maestria'")
print("  pega so a fracao maestria/N — e N varia por encontro.\n")
print(f"  {'encontro (nv30)':<22}{'corpos':>8}{'dano/rod':>10}"
      f"{'todos':>12}{'maestria=4':>13}")
for nome, n, dano in (("Desastre sozinho",1,219.0), ("4 capangas",4,220.0),
                      ("esquadrao de 8",8,440.0)):
    # quem falha ataca outros com desvantagem: -25 pp sobre acerto base de 50% = metade do dano
    todos = dano * FALHA * (BASE_ACERTO/ (BASE_ACERTO*2))   # metade do dano dos que falharam
    mae   = dano * min(4/n,1) * FALHA * 0.5
    print(f"  {nome:<22}{n:>8}{dano:>10.0f}{dano*FALHA*0.5:>11.1f}{mae:>13.1f}")
print()
print("  'todos' e o ESTAVEL: sempre ~metade do dano do encontro.")
print("  'maestria' e o que oscila: identico contra chefe, quase nada contra turba.")
print()

print("="*72)
print("3 · EM FATIA — 1x por cena, 3 lutas por dia")
print("="*72)
for nome, n, dano in (("Desastre sozinho",1,219.0), ("esquadrao de 8",8,440.0)):
    for rot, alvos in (("todos", n), ("maestria=4", min(4,n))):
        evitado = dano * (alvos/n) * FALHA * 0.5
        dr = evitado * LUTAS_DIA / DIA
        print(f"  {nome:<20} {rot:<12} evita {evitado:>6.1f} por cena"
              f" -> {dr:>5.2f}/rodada = {dr/FATIA:>5.2f} fatia")
print()
print("  ATENCAO: isto e o lado 'o mestre ignora a isca'. Se ele MORDE, o dano")
print("  nao some — ele vem pro Bastiao com +25 pp. O projeto ja modelou isso")
print("  como spread (0,75x / 1,25x) e nao como ponto. Numero acima e teto.")
