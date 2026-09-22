# -*- coding: utf-8 -*-
"""Quantas vezes o Bastiao falha um Bloquear por combate, e variantes do nivel 15.
Bloquear = 2d10-1, sem teto por rodada, sem custo de acao (peca 23 §2).
"""
from itertools import product
FATIA, DIA, LUTAS, RODADAS, GOLPE = 5.08, 10.5, 3, 3.5, 73.0
MAG = 4.5 + 15                      # 1d8 + metade do nivel, nv30
def evit(dia_total): return dia_total/DIA/FATIA

print("="*74); print("1 · A DISCORDANCIA — quantas falhas por combate")
print("="*74)
print("  Bloquear nao custa acao, nao tem teto por rodada e nao gasta Reacao.")
print("  Entao o Bastiao bloqueia TODO ataque mirado nele. E o Provocar existe")
print("  justamente para que ataques sejam mirados nele.\n")
print(f"  {'ataques mirados nele/rodada':<34}{'falhas/cena':>13}{'com 1x/rodada':>15}")
for atq in (1,2,3):
    falhas = atq*0.5*RODADAS
    # com teto de 1 por rodada: prob de ao menos uma falha na rodada
    p_ao_menos_uma = 1 - 0.5**atq
    usos = p_ao_menos_uma*RODADAS
    print(f"  {atq:<34}{falhas:>13.2f}{usos:>15.2f}")
print()
print("  Voce disse: 'dificilmente mais de uma vez por combate'.")
print("  Isso exige ~0,6 ataque bloqueavel mirado nele por rodada — um chefe")
print("  que quase nunca bate nele. Mas o degrau 2 puxa golpe E provoca.")
print()

print("="*74); print("2 · O PRECO DE '1d8 + metade do nivel, 1x POR RODADA'")
print("="*74)
for atq in (1,2,3):
    usos = (1-0.5**atq)*RODADAS
    print(f"  {atq} ataque(s)/rodada -> {usos:.2f} usos por cena"
          f" -> {evit(usos*MAG*LUTAS):>5.2f} fatia")
print(f"\n  se a SUA leitura estiver certa (1 uso por combate): "
      f"{evit(1*MAG*LUTAS):.2f} fatia — cabe")
print(f"  se a MINHA estiver certa (3 ataques/rodada):        "
      f"{evit((1-0.5**3)*RODADAS*MAG*LUTAS):.2f} fatia — nao cabe")
print()

print("="*74); print("3 · A VARIANTE QUE NAO DEPENDE DE QUEM ESTA CERTO")
print("="*74)
# 2d10-1 contra um alvo T tal que a base seja 50/50. Pego T = 11 (P(2d10-1 >= 11) ~ 50%)
dist = {}
for a,b in product(range(1,11), repeat=2):
    v = a+b-1
    dist[v] = dist.get(v,0)+1
tot = sum(dist.values())
T = 11
falha = sum(c for v,c in dist.items() if v < T)/tot
for margem in (3,5,7):
    quase = sum(c for v,c in dist.items() if T-margem <= v < T)/tot
    print(f"  falha por {margem} ou menos: {quase:>6.1%} de todos os bloqueios"
          f"  = {quase/falha:>5.1%} das falhas")
print(f"  falha total: {falha:.1%}")
print()
quase5 = sum(c for v,c in dist.items() if T-5 <= v < T)/tot
for atq in (1,2,3):
    usos = atq*quase5*RODADAS
    print(f"  'falhou por 5 ou menos', {atq} ataque(s)/rodada -> {usos:.2f} usos/cena"
          f" -> {evit(usos*MAG*LUTAS):>5.2f} fatia")
print()
print("="*74); print("4 · A OUTRA VARIANTE — a reducao E o que voce rolou")
print("="*74)
esp_falha = sum(v*c for v,c in dist.items() if v < T)/sum(c for v,c in dist.items() if v < T)
print(f"  media do 2d10-1 quando ele FALHA: {esp_falha:.2f}")
print(f"  reduzir nisso, sem teto, com 3 ataques/rodada:"
      f" {evit(3*falha*RODADAS*esp_falha*LUTAS):.2f} fatia")
print(f"  mas nao escala: {esp_falha:.1f} contra um golpe de {GOLPE:.0f} no nv30"
      f" = {esp_falha/GOLPE:.0%} do golpe")
