# -*- coding: utf-8 -*-
FATIA, RODADAS, ACERTO = 5.08, 10.5, 0.50
PISO = 0.20
NV = 30
RED = NV + 3.5          # 33,5
BASE_USOS, BASE_PEGA, BASE_MAG = 2, ACERTO, RED

def p(usos, mag, pega):
    dr = usos * mag * pega / RODADAS
    return dr, dr / FATIA, usos / RODADAS

base_dr, base_f, base_tx = p(BASE_USOS, BASE_MAG, BASE_PEGA)

# candidatos: (rotulo, usos, magnitude, pega, o que o jogador sente)
cands = [
 ("usos 2 -> 3",                      3, RED,   ACERTO),
 ("usos 2 -> 4",                      4, RED,   ACERTO),
 ("usos 2 -> 6",                      6, RED,   ACERTO),
 ("gatilho: 'ataca' -> 'ACERTA'",     2, RED,   1.00),
 ("gatilho ACERTA + usos 2 -> 3",     3, RED,   1.00),
 ("gatilho ACERTA + usos 2 -> 4",     4, RED,   1.00),
 ("reducao dobra (2xnivel + 1d6)",    2, 2*NV+3.5, ACERTO),
 ("reducao dobra + gatilho ACERTA",   2, 2*NV+3.5, 1.00),
 ("pega 2 golpes do mesmo inimigo",   2, RED*2, ACERTO),
 ("pega 2 golpes + gatilho ACERTA",   2, RED*2, 1.00),
 ("pega a Acao inteira (3 golpes)",   2, RED*3, ACERTO),
 ("alcance 1,5 m -> 9 m, so isso",    2, RED,   ACERTO),
]

ALVO = 1.25
print(f"{'candidato':<36}{'dano/rod':>10}{'fatia':>8}{'delta':>8}{'taxa':>8}  {'':<4}")
print("-"*76)
print(f"{'[nivel 2 hoje, preco honesto]':<36}{base_dr:>10.2f}{base_f:>8.2f}{'—':>8}{base_tx:>8.1%}")
print("-"*76)
for nome, u, m, pg in cands:
    dr, f, tx = p(u, m, pg)
    d = f - base_f
    marca = "  <== fecha em ~1,25" if abs(d-ALVO) <= 0.12 else ("  piso" if tx < PISO else "")
    print(f"{nome:<36}{dr:>10.2f}{f:>8.2f}{d:>+8.2f}{tx:>8.1%}{marca}")

print()
print(f"orcamento do Caminho: 5,00 fatia   nivel 2 leva {base_f:.2f}")
print(f"sobra para 15 / 23 / 30: {5.0-base_f:.2f} fatia  ({(5.0-base_f)/3:.2f} por degrau se dividir igual)")
print()
print("=== dominancia contra o Escora (Trilha Muro, nv19, 1,33 fatia) ===")
print("O Escora hoje: usos a mais = metade da Constituicao, e qualquer um deles")
print("pode ser gasto num aliado a ate 9 m. Com Constituicao 6 sao +3 usos.")
esc_dr, esc_f, esc_tx = p(3, RED, 1.00)   # Escora herda o gatilho do Absorver: 'ao ser atingido'
print(f"os +3 usos do Escora, sozinhos: {esc_dr:.2f} dano/rodada = {esc_f:.2f} fatia  (preco publicado: 1,33)")
print()
print("O que o Escora vendia e a Interposicao ja entrega: gastar o uso NUM ALIADO.")
print("Sobra pro Escora so a quantidade — e se o nivel 15 do Caminho for 'mais usos',")
print("as duas pecas passam a vender a mesma coisa em niveis vizinhos.")
