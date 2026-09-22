# -*- coding: utf-8 -*-
"""
Nivel 15 do Bastiao — precos em fatia.
Bases lidas de documento dono, nunca escritas de intuicao:

  fatia                 5,08 dano/rodada, medida no nv30   -> DESENHO-manhas.md
  Rotina nv30           108,00 dano/rodada                 -> DESENHO-manhas.md
  rodadas de luta/dia   10,5  (3 lutas x 3,5)              -> reforma / peca 10
  taxa de acerto        50%                                -> peca 1
  1 PE por rodada       5,14 de dano por rodada            -> peca 26 §6.5 (v0.205)
  maestria              1/2/3/4 por faixa de 8 niveis      -> peca 1 §2
  Bastiao               7 vida/nivel, 4 PE/nivel           -> peca 6
  golpe do Desastre     73 (8d8+37), 3 acoes, 219/rodada   -> peca 26 §4.4
  piso de taxa          20%    filtro de dominancia 3,0x   -> LISTA-gatilhos
  orcamento do Caminho  5 fatias (2 / 15 / 23 / 30)        -> reforma
"""

FATIA      = 5.08
ROTINA30   = 108.00
RODADAS    = 10.5
ACERTO     = 0.50
PE_RODADA  = 5.14
PISO_TAXA  = 0.20
ORCAMENTO  = 5.0
GOLPE_CHEFE= 73.0
ACOES_CHEFE= 3

def maestria(nv):
    return 1 if nv <= 9 else 2 if nv <= 17 else 3 if nv <= 25 else 4

def reducao(nv):        # nivel + 1d6, esperanca
    return nv + 3.5

def em_fatia(dano_rodada):
    return dano_rodada / FATIA

def preco(usos_dia, magnitude, pega=1.0):
    """usos por dia x magnitude evitada x fracao que de fato acontece, diluido no dia"""
    dr = usos_dia * magnitude * pega / RODADAS
    return dr, em_fatia(dr), usos_dia / RODADAS

print("=" * 74)
print("0 · REGRESSAO — as duas contas que ja existem tem que reproduzir")
print("=" * 74)
nv = 30
r = reducao(nv)
print(f"reducao no nv30 = {nv} + 1d6 = {r}")

# Absorver antigo: gatilho "ao ser atingido" -> nenhum uso se perde
dr, f, tx = preco(6, r, pega=1.0)
print(f"Absorver antigo (6 usos = Constituicao, gatilho AO SER ATINGIDO):")
print(f"   {dr:.2f} dano/rodada = {f:.2f} fatia   (reforma diz 3,77)   taxa {tx:.1%}")

# Interposicao, leitura do reforma: 2 usos, sem fator de erro
dr, f, tx = preco(2, r, pega=1.0)
print(f"Interposicao (2 usos), leitura do reforma — sem descontar o erro:")
print(f"   {dr:.2f} dano/rodada = {f:.2f} fatia   (reforma diz 1,26)   taxa {tx:.1%}")
print()

print("=" * 74)
print("1 · O ACHADO — o gatilho da Interposicao e ANTES da rolagem")
print("=" * 74)
print("O Absorver dispara 'ao ser atingido': nenhum uso cai em erro.")
print("A Interposicao dispara 'um inimigo ataca um aliado', e o alvo troca")
print("antes do dado — senao a rolagem teria sido contra a Defesa do aliado.")
print(f"Entao metade dos usos cai num ataque que erra, e a reducao nao acontece.")
print()
dr_a, f_a, tx = preco(2, r, pega=1.0)
dr_b, f_b, _  = preco(2, r, pega=ACERTO)
print(f"   sem o fator de erro : {dr_a:5.2f} dano/rodada = {f_a:.2f} fatia")
print(f"   COM o fator de erro : {dr_b:5.2f} dano/rodada = {f_b:.2f} fatia")
print(f"   sobra do Caminho: {ORCAMENTO - f_a:.2f} fatia -> {ORCAMENTO - f_b:.2f} fatia")
print(f"   taxa dos 2 usos gratis: {tx:.1%}   piso do projeto: {PISO_TAXA:.0%}")
print()

print("=" * 74)
print("2 · A PORTA DE PE — quanto ela vale, e se alguem paga")
print("=" * 74)
for nv in (2, 10, 18, 26, 30):
    m = maestria(nv)
    pe_total = 4 * nv
    ganho  = reducao(nv) * ACERTO          # dano evitado esperado por uso
    custo  = m * PE_RODADA                 # PE gasto naquela rodada, em dano
    usos_pe = pe_total // m
    print(f"nv{nv:>2}  maestria {m}  PE total {pe_total:>3}  |  uso extra custa {m} PE = "
          f"{custo:5.2f} de dano  e evita {ganho:5.2f}  -> troca {ganho/custo:.2f}x"
          f"   (PE pagaria ate {usos_pe:.0f} usos/dia)")
print()
print("Troca abaixo de 1,00 quer dizer que pagar PE e prejuizo no livro-caixa:")
print("o Bastiao larga mais dano do que evita. O contador de 2 nao e o teto —")
print("o teto e a troca ficar ruim.")
print()

print("=" * 74)
print("3 · CANDIDATOS PARA O NIVEL 15 — todos no nv30, ancora 'o golpe e meu'")
print("=" * 74)
nv = 30; r = reducao(nv); base = preco(2, r, ACERTO)[1]

cands = [
    ("A  dobra os usos: 2 -> 4",            preco(4, r, ACERTO)),
    ("B  dobra a reducao: 2xnivel + 1d6",   preco(2, 2*nv + 3.5, ACERTO)),
    ("C  pega DOIS golpes do mesmo inimigo",preco(2, r*2, ACERTO)),
    ("D  pega a ACAO inteira (3 golpes)",   preco(2, r*3, ACERTO)),
    ("E  alcance 1,5 m -> 9 m (so isso)",   preco(2, r, ACERTO)),
    ("F  declara DEPOIS da rolagem",        preco(2, r, 1.0)),
]
print(f"{'candidato':<40}{'dano/rod':>10}{'fatia':>8}{'delta':>8}{'taxa':>8}")
for nome, (dr, f, tx) in cands:
    print(f"{nome:<40}{dr:>10.2f}{f:>8.2f}{f-base:>+8.2f}{tx:>8.1%}")
print()
print(f"base (Interposicao do nv2, com o fator de erro) = {base:.2f} fatia")
print(f"referencia de orcamento do reforma para o nv15  = ~1,25 fatia")
print(f"sobra depois do nv2, para 15 / 23 / 30          = {ORCAMENTO - base:.2f} fatia")
