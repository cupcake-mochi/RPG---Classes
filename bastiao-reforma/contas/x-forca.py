# -*- coding: utf-8 -*-
"""X = Forca contra X = Maestria, na regua em que o Provocar foi aprovado.
Bases: Provocar = 25 pp quando dispara, alvo falha 50% (teste disputado, base)
       envelope aprovado = 12,5 pp/rodada x 3,5 rodadas = 43,75 pp por cena
       atributo: escala 0 a 6, teto 6 · 9 pontos na criacao, +1 por marco
       maestria: 1 (nv2-9) · 2 (10-17) · 3 (18-25) · 4 (26-30)
"""
PP, FALHA, ENVELOPE = 25.0, 0.50, 43.75
def pp(n): return n*PP*FALHA

print(f"  {'X':>14}{'alvos':>7}{'pp por cena':>14}{'% do envelope':>16}")
print("  " + "-"*49)
for rot, n in (("Maestria nv2",1),("Maestria nv30",4)):
    print(f"  {rot:>14}{n:>7}{pp(n):>13.1f} {pp(n)/ENVELOPE:>15.0%}")
print("  " + "-"*49)
for f in (2,3,4,5,6):
    print(f"  {'Forca '+str(f):>14}{f:>7}{pp(f):>13.1f} {pp(f)/ENVELOPE:>15.0%}")
print("  " + "-"*49)
print(f"  {'todos (8)':>14}{8:>7}{pp(8):>13.1f} {pp(8)/ENVELOPE:>15.0%}")
print()
print("  Forca tem TETO 6 e chega nele cedo; Maestria so chega em 4, no nv26.")
print("  Entao Forca nao e 'Maestria maior': e outra curva, que satura.")
print()
print("  QUANTOS EIXOS a Forca ja carrega neste Caminho:")
for i, e in enumerate(["acerto corpo a corpo","dano corpo a corpo","Atletismo (pericia fixa)",
                       "Intimidacao (trocado neste degrau)","Provocar (trocado neste degrau)",
                       "numero de alvos do Encarar (proposto)"], 1):
    print(f"    {i}. {e}")
