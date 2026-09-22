# -*- coding: utf-8 -*-
"""A proposta do nivel 15 pendurada no Bloquear, e um cardapio pro 30.
Bases de dono:
  Bloquear = 2d10-1 no lugar do 10 da Defesa. media 10 = NEUTRO ... peca 23 §2
  a neutralidade sustenta o preco do Incapacitado ................ peca 19 §..., peca 23
  fatia 5,08 · dia 10,5 · 3 lutas/dia · luta 3,5 rodadas · golpe 73 · Bastiao 210 vida
  dano evitado 1 pra 1 · dano movido 0,30
  SOBRA depois do nivel 2: 2,54 fatia
"""
FATIA, DIA, LUTAS, RODADAS_LUTA, GOLPE = 5.08, 10.5, 3, 3.5, 73.0
TAXA, SOBRA, NV, VIDA = 0.30, 2.54, 30, 210
REDUZ = 4.5 + NV/2          # 1d8 + metade do nivel = 19,5 no nv30
FALHA = 0.50                # metade dos bloqueios falha (2d10-1 e neutro)

def evit(dia_total): return dia_total/DIA/FATIA
def mov(golpes_luta): return golpes_luta*GOLPE*LUTAS/DIA*TAXA/FATIA

print("="*74); print("1 · A PROPOSTA DO NIVEL 15, em tres leituras do teto")
print("="*74)
print(f"  reducao por falha no nv30: 1d8 + metade do nivel = {REDUZ:.1f}\n")
print(f"  {'quantos ataques ele bloqueia por rodada':<44}{'falhas/dia':>12}{'fatia':>8}")
for atq in (1, 2, 3):
    falhas_dia = atq * FALHA * RODADAS_LUTA * LUTAS
    print(f"  {atq} ataque(s) por rodada, SEM teto{'':<14}{falhas_dia:>12.1f}"
          f"{evit(falhas_dia*REDUZ):>8.2f}")
print()
for con in (2, 4, 6):
    teto = con//2 + 1
    # o teto so morde se for menor que as falhas naturais
    falhas_nat = 2 * FALHA * RODADAS_LUTA        # 2 ataques/rodada, por cena
    efetivo = min(teto, falhas_nat)
    print(f"  CON {con} -> teto {teto}/cena · falhas naturais {falhas_nat:.1f}/cena"
          f" -> valem {efetivo:.1f}  = {evit(efetivo*REDUZ*LUTAS):.2f} fatia"
          f"{'   teto NAO morde' if teto >= falhas_nat else '   teto morde'}")
print()
print(f"  orcamento do degrau, se dividir a sobra em tres: {SOBRA/3:.2f}")
print()

print("="*74); print("2 · TESTE DE BONUS AUTOMATICO — criterio da propria peca 23 §1")
print("="*74)
print('  "enumere as montagens legais e conte quantas ganham o bonus.')
print('   Perto de 100%, nao e bonus."\n')
print(f"  Bloquear e NEUTRO: media {10.0:.0f}, igual ao 10 parado. Rolar ou nao da na mesma.")
print(f"  Com premio na falha, bloquear passa a valer +{FALHA*REDUZ:.2f} de dano evitado")
print(f"  por ataque. Nenhum Bastiao deixa de bloquear nunca. Montagens que ganham: 100%.")
print()

print("="*74); print("3 · CARDAPIO PARA O NIVEL 30")
print("="*74)
cands = [
 ("o redirect deixa de custar Reacao: TODO ataque na area vem\n"
  "     pra voce, e voce escolhe quais NAO pegar", mov(2.0), "inverte o padrao"),
 ("2o redirect livre (uma Reacao a mais, so pro Encarar)", mov(1.0), "mais do mesmo"),
 ("aliado que cairia dentro da area fica com 1 de vida,\n"
  "     1x por cena, e voce leva o excedente", None, "colide com Ninguem Cai do Guia"),
 ("enquanto houver inimigo encarado, VOCE nao vai a 0: fica em 1", None, "sem regua"),
 ("quem esta na area nao pode atacar ninguem alem de voce", mov(3.0), "tira a agencia toda"),
 ("voce pode tomar a QUEDA de um aliado: ele fica de pe,\n"
  "     voce cai no lugar", None, "a unidade da Rota A, sem cambio"),
]
for nome, f, nota in cands:
    p = f"{f:>6.2f}" if f is not None else f"{'—':>6}"
    print(f"  {nome:<58}{p}   {nota}")
print()
print(f"  sobra depois do 15 e do 23 depende do 15. Se o 15 ficar em 1,26,")
print(f"  o 30 tem {SOBRA-1.26:.2f}.")
