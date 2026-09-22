# -*- coding: utf-8 -*-
"""
ROTA A — primeira derivacao da regua de 'corpo de pe'.
Tudo de documento dono, com a COLUNA nomeada:

  peca 26 §4.7, tabela 'o que a CURA do grupo faz':
     luta contra o Desastre nv30 = 3,00 rodadas · o chefe entrega 657 nas tres
     => o grupo derruba 945 de vida em 3,00 rodadas = 315 por rodada
     => UM personagem entrega 78,75 por rodada contra o chefe
     e a peca escreve isso: "um atacante que para de bater abre mao de 78,75"
  peca 1 §5.5, a maquina de 0 de vida:
     janela de 3 rodadas · cura de 1 levanta · Sequela em toda queda
     segunda queda = Cicatriz permanente
  peca 26 §4.7: curar gasta a acao que causaria dano
  DESENHO-manhas: fatia = 5,08 de dano por rodada, no nv30
  reforma: o dia tem 10,5 rodadas de luta (3 lutas x 3,5)
"""
SAIDA_PJ   = 78.75     # o que UM PJ entrega por rodada contra o chefe, nv30
ROTINA     = 108.0     # o que ele entrega contra alvo padrao
LUTA       = 3.00      # rodadas, contra o Desastre nv30
DIA        = 10.5
FATIA      = 5.08

print("="*72)
print("1 · O QUE UMA QUEDA CUSTA — em dano, no nivel 30")
print("="*72)
# cai no meio da luta (a peca 1 §5.5 diz: "voce cai, em media, no meio dele")
queda_em = LUTA / 2
sobra    = LUTA - queda_em

a = SAIDA_PJ * 1.0          # uma rodada dele no chao antes de alguem chegar
b = SAIDA_PJ * 1.0          # o turno de quem larga de bater pra levantar
c = SAIDA_PJ * sobra        # se ninguem levanta: o resto da luta inteiro

print(f"  a pessoa fica UMA rodada no chao        {a:>7.2f}")
print(f"  quem levanta ela abre mao da rodada     {b:>7.2f}")
print(f"  --------------------------------------  {'-'*7}")
print(f"  queda socorrida                         {a+b:>7.2f}")
print(f"  queda NAO socorrida ({sobra:.2f} rodadas)      {c:>7.2f}"
      f"   + estagio 4 de dano de alma")
print()

print("="*72)
print("2 · CONVERTENDO PRA REGUA DA FATIA")
print("="*72)
for rot, custo in (("socorrida", a+b), ("nao socorrida", c)):
    por_rodada_luta = custo / LUTA
    por_rodada_dia  = custo / DIA
    print(f"  queda {rot:<14} {custo:>7.2f} de dano")
    print(f"     diluida na LUTA  ({LUTA:.2f} rodadas): {por_rodada_luta:>6.2f}/rodada"
          f" = {por_rodada_luta/FATIA:>5.2f} fatia")
    print(f"     diluida no DIA  ({DIA:.1f} rodadas): {por_rodada_dia:>6.2f}/rodada"
          f" = {por_rodada_dia/FATIA:>5.2f} fatia")
print()
print("  O denominador certo e o DIA, porque e nele que a fatia ja mora:")
print("  a conta de 'quantas vezes por dia' do projeto divide por 10,5.")
print()

print("="*72)
print("3 · A LUTA REFEITA COM O NUMERO CERTO (eu tinha usado 108 e nao 78,75)")
print("="*72)
GOLPE, ACERTO, ACOES = 73.0, 0.50, 3
VIDA = {"Bastiao":210.0, "Vanguarda":150.0, "Guia":150.0, "Emanador":120.0}

def roda(redirects, passo=0.05):
    pjs, chefe, t, perdido = dict(VIDA), 945.0, 0.0, 0.0
    while chefe > 0 and t < 12:
        vivos = [k for k,v in pjs.items() if v > 0]
        if not vivos: break
        chefe   -= len(vivos) * SAIDA_PJ * passo
        perdido += (4 - len(vivos)) * SAIDA_PJ * passo      # saida que o grupo PERDEU
        if chefe <= 0: break
        alvo = min(vivos, key=lambda k: pjs[k])
        for i in range(ACOES):
            d = GOLPE * ACERTO * passo
            if i < redirects and pjs["Bastiao"] > 0 and alvo != "Bastiao":
                pjs["Bastiao"] -= d
            else:
                pjs[alvo] -= d
        t += passo
    return t, sum(1 for v in pjs.values() if v <= 0), perdido, pjs

print(f"  {'puxa':>5}{'rodadas':>9}{'caidos':>8}{'saida perdida':>15}"
      f"{'poupado':>10}{'/dia':>8}{'fatias':>8}")
base = roda(0)[2]
for n in (0,1,2,3):
    t, c, perdido, pjs = roda(n)
    poupado = base - perdido
    print(f"  {n:>5}{t:>9.2f}{c:>8}{perdido:>15.1f}{poupado:>+10.1f}"
          f"{poupado/DIA:>+8.2f}{poupado/DIA/FATIA:>+8.2f}")
print()
print("  'saida perdida' = dano que o grupo deixou de entregar por ter gente no chao.")
print("  Sem contar o turno de quem socorre, nem Sequela, nem Cicatriz.")
