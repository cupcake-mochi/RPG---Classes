# -*- coding: utf-8 -*-
"""Trilha Muro, refeita sobre o Encarar. Bases de dono:
  resistencia: 1 tipo = 3,39 dano evitado = 0,67 fatia (DESENHO-trilhas §resistencia)
  Aterro publicado = 0,71 · Escora = 1,33 · Cupula = 1,50 · Alicerce = 1,33
  orcamento da Trilha = 5,00 · fatia 5,08 · dia 10,5 · 3 lutas · luta 3,5 rodadas
  golpe do Desastre nv30 = 73 · 2 golpes puxados por luta · dano movido x 0,30
  2d10-1: media 10,00 · media condicionada a falhar 7,00
"""
FATIA, DIA, LUTAS, RODADAS, GOLPE = 5.08, 10.5, 3, 3.5, 73.0
RESIST, ORC, PUXA, CON = 3.39, 5.00, 2, 6
def evit(dia_total): return dia_total/DIA/FATIA

print("="*76); print("1 · A FUSAO DO ALICERCE NO ENCARAR — quanto custa?")
print("="*76)
print(f"  2 tipos x {RESIST} = {2*RESIST:.2f} de dano evitado = {2*RESIST/FATIA:.2f} fatia")
print(f"  o preco publicado do Alicerce e 1,33. Bate exato.")
print()
print("  >>> Entao o 'deslocamento pela metade' NUNCA foi preçado. Ele valia 0,00.")
print("      Fundir no Encarar e tirar o custo de movimento sai de GRACA na regua —")
print("      e e um ganho real na mesa. Mesma forma do 'alcance de graça' de antes.")
print()

print("="*76); print("2 · A SUA IDEIA DO 19 — a RD vale tambem no golpe puxado")
print("="*76)
print("  Hoje o Aparar com Corpo nunca pega golpe puxado: o acerto transfere")
print("  sem rolagem, entao nao ha Bloquear pra falhar.\n")
opts = [("rola o 2d10-1 assim mesmo (media 10) + CON", 10+CON),
        ("rola o 2d10-1 assim mesmo, sem CON",          10),
        ("recebe a media do Aparar (7 + CON = 13)",     7+CON),
        ("recebe so a Constituicao",                    CON)]
print(f"  {'variante':<46}{'magnitude':>11}{'fatia':>8}")
for nome, m in opts:
    print(f"  {nome:<46}{m:>11.1f}{evit(PUXA*m*LUTAS):>8.2f}")
print(f"\n  a vaga do Escora valia 1,33.")
print()

print("="*76); print("3 · OPCOES PARA O 11 (hoje Aterro, 0,71)")
print("="*76)
onze = [("a area do Encarar inteira vira terreno dificil", 0.71, "o Aterro apontando pra aura"),
        ("+ voce nao pode ser movido a forca, de jeito nenhum", 0.30, "absoluto, sem regua"),
        ("um 3o tipo de resistencia",                 RESIST/FATIA, "regua fechada"),
        ("aliados na area nao sofrem deslocamento forcado", 0.30, "sem regua"),
        ("quem termina o turno na area fica Lento",   None, "controle, sem regua")]
for n,f,nota in onze:
    p = f"{f:>6.2f}" if f is not None else f"{'—':>6}"
    print(f"  {n:<52}{p}   {nota}")
print()

print("="*76); print("4 · OPCOES PARA O 27 (hoje Cupula, 1,50)")
print("="*76)
vinte7 = [("aliados na area dividem UM dos seus tipos", 1.00, "estimado: metade do valor, 4 corpos"),
          ("aliados na area dividem TODOS os seus tipos", 2.00, "estimado"),
          ("sobe para 4 tipos, troca no descanso curto", 2*RESIST/FATIA, "regua fechada: +2 tipos"),
          ("a aura fica de pe com voce caido/agarrado/apagado", 0.00, "nunca foi precificado"),
          ("a RD do 19 passa a valer pra quem esta na area", None, "precisa medir")]
for n,f,nota in vinte7:
    p = f"{f:>6.2f}" if f is not None else f"{'—':>6}"
    print(f"  {n:<52}{p}   {nota}")
print()

print("="*76); print("5 · TRES FECHAMENTOS EM 5,00")
print("="*76)
m = [("I", [("2  resistencia a 2 tipos, dentro do Encarar", 1.33),
            ("11 a aura vira terreno dificil + nao te movem", 1.01),
            ("19 a RD vale no golpe puxado (2d10-1 + CON)", evit(PUXA*(10+CON)*LUTAS)),
            ("27 aliados na area dividem um dos tipos",     1.00)]),
     ("II",[("2  resistencia a 2 tipos, dentro do Encarar", 1.33),
            ("11 um 3o tipo de resistencia",                RESIST/FATIA),
            ("19 a RD vale no golpe puxado (7 + CON)",      evit(PUXA*(7+CON)*LUTAS)),
            ("27 aliados dividem um tipo + a aura sobrevive a voce", 1.00)]),
     ("III",[("2  resistencia a 2 tipos, dentro do Encarar", 1.33),
            ("11 a aura vira terreno dificil",              0.71),
            ("19 a RD vale no golpe puxado (so a CON)",     evit(PUXA*CON*LUTAS)),
            ("27 sobe para 4 tipos + aliados dividem um",   2*RESIST/FATIA)])]
for letra, linhas in m:
    tot = sum(f for _,f in linhas)
    print(f"  {letra}")
    for n,f in linhas: print(f"     {n:<50}{f:>6.2f}")
    print(f"     {'TOTAL':<50}{tot:>6.2f}   sobra {ORC-tot:+.2f}\n")
