# -*- coding: utf-8 -*-
"""O que a rerrolagem forcada faz com o preco do nivel 2.
Bases: golpe do Desastre nv30 = 73 · acerto base 50% · 2 golpes puxados/luta
       3 lutas/dia · 10,5 rodadas/dia · fatia 5,08
       dano EVITADO 1 pra 1 · dano MOVIDO x 0,30
"""
FATIA, DIA, LUTAS, GOLPE, ACERTO, TAXA = 5.08, 10.5, 3, 73.0, 0.50, 0.30
PUXA = 2

print("="*74); print("1 · O QUE MUDA")
print("="*74)
print("  HOJE: o gatilho e 'acerta'. O acerto transfere SEM nova rolagem.")
print("        voce sabe que ia doer, e come o golpe inteiro. 100% do dano MOVE.")
print()
print("  COM RERROLAGEM: o gatilho continua 'acerta' — entao voce so gasta a")
print("        Reacao quando ja sabe que o golpe ia entrar. E aí o atacante")
print("        rola de novo, num 50/50 limpo.")
print()
por_uso_hoje  = GOLPE * TAXA
evit_novo     = GOLPE * (1-ACERTO)          # metade das vezes ERRA: dano evitado, 1 pra 1
mov_novo      = GOLPE * ACERTO * TAXA       # a outra metade ainda move
por_uso_novo  = evit_novo + mov_novo
print(f"  valor por uso, hoje:  {GOLPE:.0f} movido x {TAXA} = {por_uso_hoje:>6.2f}")
print(f"  valor por uso, novo:  {GOLPE*(1-ACERTO):.1f} EVITADO (1 pra 1)"
      f" + {GOLPE*ACERTO:.1f} movido x {TAXA} = {por_uso_novo:>6.2f}")
print(f"  razao: {por_uso_novo/por_uso_hoje:.2f}x")
print()

print("="*74); print("2 · O PRECO DO NIVEL 2")
print("="*74)
usos_dia = PUXA * LUTAS
for rot, v in (("hoje, sem rerrolagem", por_uso_hoje), ("com rerrolagem forcada", por_uso_novo)):
    dr = usos_dia*v/DIA
    print(f"  {rot:<28}{dr:>7.2f} de dano/rodada = {dr/FATIA:>5.2f} fatia")
print()
novo = usos_dia*por_uso_novo/DIA/FATIA
print(f"  o Caminho inteiro tem 5,00 de orcamento.")
print(f"  o nivel 2 sozinho passaria a custar {novo:.2f} — mais que o Caminho.")
print(f"  soma do Caminho: {novo + 2.31 + 0.62:.2f} (com 15 em 2,31 e 30 em 0,62)")
print()

print("="*74); print("3 · VERSOES COM PORTAO")
print("="*74)
for nome, usos_cena in (("1x por cena", 1), ("2x por cena", 2), ("sem teto (2 por luta)", PUXA)):
    extra = usos_cena*LUTAS*(por_uso_novo-por_uso_hoje)/DIA/FATIA
    print(f"  rerrolagem {nome:<24} custa +{extra:>5.2f} fatia  "
          f"-> nivel 2 em {2.46+extra:>5.2f}")
print()
print("  (o 'extra' e so a diferenca: o resto do nivel 2 continua valendo 2,46)")
print()

print("="*74); print("4 · O QUE ELA CONSERTA — e nao e pouco")
print("="*74)
print("  Na v anterior eu registrei como defeito: 'a sua Defesa para de valer")
print("  no degrau que te define', porque o acerto transferia sem rolagem.")
print("  Com rerrolagem a Defesa do Bastiao volta a importar — e ele e quem")
print("  investe nela. O defeito some.")
print()
print("  MAS: se ha rolagem, o Aparar com Corpo (nv15) passa a poder disparar")
print("  no golpe puxado — e o 19 do Muro existe justamente porque ele NAO podia.")
