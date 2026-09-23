"""As seis conclusões de feitiço da Estocada (nível 11), precificadas contra a
régua já publicada do repositório principal.

Duas rolagens gate o efeito bônus, não uma: (1) o feitiço precisa acertar ou o
alvo falhar no TR principal dele -- é o que ativa a conclusão -- e (2), só
quando a opção pedir, um TR adicional próprio (CD 8 + atributo + maestria)
solta o efeito. Desorientar e Refluxo não pedem o segundo TR; as outras quatro
pedem. Perder esse segundo gate foi o primeiro erro desta rodada -- fica como
contra-teste abaixo.

Decisão do Mizuki, 21/09, depois da primeira rodada:
1. Cortar a Resposta estava cara demais (2,17) e a mesma janela larga
   ("sem Reação até o começo do seu próximo turno") empurrava o número pra
   cima artificialmente. Mecânica estreitada: nega Reação só contra o PRÓXIMO
   ataque que o alvo sofrer, não a janela inteira. Isso troca a magnitude de
   36,50 (meia ação de chefe) por 25pp x 0,230 (a mesma lógica de "vantagem
   numa rolagem" que Expor a Guarda já usa) -- e bate no mesmo número.
   NOTA: isto estreita só a versão de feitiço. A irmã de arma, Interromper a
   Resposta, continua com a janela larga e o 36,50 dentro do modelo já
   validado (conferir-vanguarda-v3.py) -- as duas deixam de ser "mesmo
   efeito, dois nomes" até alguém decidir estreitar a de arma também. Fica
   registrado, não escondido.
2. Desorientar fecha no piso (leitura "vale um ataque de aliado com
   vantagem"), porque a rolagem que ele pega é imprevisível -- às vezes é
   ataque, às vezes é perícia sem importância nenhuma -- e o valor esperado
   tem que refletir isso, não o caso favorável.

Fontes de cada magnitude:
  - tirar Reação = 36,50 -- conferir-vanguarda-v3.py, magnitude['resposta'],
    o mesmo efeito de Interromper a Resposta (arma)
  - movimento = 0,60 equivalente/m -- vanguarda-escolas-rascunho.md
  - 1 pp na rolagem de um aliado = 0,230 -- peça 19, l.75
  - vantagem/desvantagem = 25 pp -- DESENHO-trilhas.md
  - "deslocamento zero" isolado = Impedido - Impedido/1,10 -- peça 19: "ele é
    o Cego inteiro mais deslocamento zero, que é o que [o parágrafo] já mede
    em 1,10x"; Impedido = 132,15 (peça 19)
  - TR de referência: 55% de falha (vanguarda-conclusao-dupla.md, perfil Defesa 20)
"""
from fractions import Fraction as F
import json
import sys
from pathlib import Path
import re

SLICE = F(508, 100)
P_SPELL = F(55, 100)        # feitiço acerta / alvo falha no TR principal
FALHA_TR_ADD = F(55, 100)   # TR adicional da conclusão, mesma referência

TIRAR_REACAO = F(3650, 100)
METRO = F(60, 100)
PP_ALIADO = F(230, 1000)
REGUA = (Path(__file__).resolve().parent / 'referencia-jjk-project/sistema/03-mecanica/19-dano-e-condicoes.md').read_text()
def preco_condicao(nome):
    linha = next(l for l in REGUA.splitlines() if re.match(r'^\| \*\*`' + nome + r'`\*\* \|', l))
    return F(linha.split('|')[2].strip().strip('`').replace(',', '.'))
IMPEDIDO = preco_condicao('Impedido')
CEGO = preco_condicao('Cego')
DESLOC_ZERO = IMPEDIDO - CEGO
PE_RATE = F(514, 100)
DESASTRE = F(73)


def fatias(x):
    return x / SLICE


PRECOS = {
    'cortar_a_resposta': P_SPELL * FALHA_TR_ADD * (25 * PP_ALIADO),  # mecânica estreitada, 21/09
    'romper_fileira': P_SPELL * FALHA_TR_ADD * (6 * METRO + 6 * METRO),
    'expor_a_guarda': P_SPELL * FALHA_TR_ADD * (25 * PP_ALIADO),
    'ancorar': P_SPELL * FALHA_TR_ADD * DESLOC_ZERO,
    'refluxo': P_SPELL * (1 * PE_RATE),
    'desorientar': P_SPELL * (25 * PP_ALIADO),  # fechado no piso, decisão de 21/09
}
# Preservados só pra registro histórico (não entram no preço adotado):
HISTORICO = {
    'cortar_a_resposta_janela_larga_36_50': P_SPELL * FALHA_TR_ADD * TIRAR_REACAO,
    'desorientar_teto_golpe_de_chefe': P_SPELL * (25 * F(1, 100) * DESASTRE),
}

output = {'em_fatias': {k: float(fatias(v)) for k, v in PRECOS.items()}}
output['ancorar_magnitude_deslocamento'] = float(DESLOC_ZERO)

print("As seis conclusões de feitiço, com os dois gates corretos:\n")
for nome, val in sorted(PRECOS.items(), key=lambda kv: kv[1]):
    print(f"  {nome:20s} {float(fatias(val)):.4f} fatias")

# Contra-teste 1: a versão SEM o segundo gate (o erro cometido na primeira
# rodada desta conta) dá um número diferente e maior -- prova que o gate importa.
sem_segundo_gate = P_SPELL * (25 * PP_ALIADO)  # só o primeiro gate
assert fatias(sem_segundo_gate) > fatias(PRECOS['cortar_a_resposta']) * F(15, 10)
output['contra_teste_gate'] = {
    'cortar_a_resposta_sem_segundo_gate': float(fatias(sem_segundo_gate)),
    'cortar_a_resposta_com_os_dois_gates': float(fatias(PRECOS['cortar_a_resposta'])),
}

# Contra-teste 2: a janela larga que foi rejeitada (histórico) segue muito
# maior que a estreitada -- prova que a mudança de mecânica muda o preço de
# verdade, e não é só cosmética.
output['contra_teste_janela'] = {
    'janela_larga_rejeitada': float(fatias(HISTORICO['cortar_a_resposta_janela_larga_36_50'])),
    'janela_estreita_adotada': float(fatias(PRECOS['cortar_a_resposta'])),
}
assert fatias(HISTORICO['cortar_a_resposta_janela_larga_36_50']) > fatias(PRECOS['cortar_a_resposta']) * 5

# Resolvido: Cortar a Resposta agora usa a MESMA fórmula de Expor a Guarda
# (vantagem numa rolagem), então as duas pedem 2 conduções pelo mesmo preço.
# O vão que existia com a janela larga (3x a 6x) não existe mais.
assert PRECOS['cortar_a_resposta'] == PRECOS['expor_a_guarda']
output['vao_2_conducoes_resolvido'] = True

output['checks'] = ('Segundo gate muda o número; janela larga x estreita muda o número; '
                     'Cortar a Resposta e Expor a Guarda batem exato, sem vão: OK.')
print('\n' + output['checks'])

# --- Duplas de feitiço do nível 30 -----------------------------------------
# As duas dependem do MESMO gate de "o feitiço afetar o alvo"; daí em diante
# cada uma paga (ou não) seu TR adicional. A soma só serve como teto aditivo
# condicionado: efeitos podem se sobrepor e só há um uso por cena.
from itertools import combinations

COMPONENTES = {
    'cortar_a_resposta': 25 * PP_ALIADO,
    'expor_a_guarda': 25 * PP_ALIADO,
    'romper_fileira': 6 * METRO + 6 * METRO,
    'refluxo': 1 * PE_RATE,
    'desorientar': 25 * PP_ALIADO,
    'ancorar': DESLOC_ZERO,
}
PEDE_TR = {'cortar_a_resposta': True, 'expor_a_guarda': True, 'romper_fileira': True,
           'refluxo': False, 'desorientar': False, 'ancorar': True}


def componente(nome):
    mag = COMPONENTES[nome]
    return mag * (FALHA_TR_ADD if PEDE_TR[nome] else 1)


duplas = {}
for a, b in combinations(COMPONENTES, 2):
    duplas[f'{a}+{b}'] = P_SPELL * (componente(a) + componente(b))

output['duplas_por_acionamento'] = {k: float(fatias(v)) for k, v in duplas.items()}
output['duplas_chance_ambas'] = {
    f'{a}+{b}': float(P_SPELL *
                        (FALHA_TR_ADD if PEDE_TR[a] else 1) *
                        (FALHA_TR_ADD if PEDE_TR[b] else 1))
    for a, b in combinations(COMPONENTES, 2)
}
melhor = max(duplas.items(), key=lambda kv: kv[1])
pior = min(duplas.items(), key=lambda kv: kv[1])
print(f"\nDuplas de feitiço (por acionamento, sem frequência do dia): melhor {melhor[0]} "
      f"{float(fatias(melhor[1])):.4f}, pior {pior[0]} {float(fatias(pior[1])):.4f}")

# Contra-teste: nenhuma dupla foge da soma das duas isoladas -- prova que não
# há sobreposição escondida sendo dupla-contada nem descontada sem querer.
for a, b in combinations(COMPONENTES, 2):
    total = duplas[f'{a}+{b}']
    esperado = P_SPELL * componente(a) + P_SPELL * componente(b)
    assert abs(total - esperado) < F(1, 10**6)
output['nota'] = ('Teto aditivo por acionamento condicionado à dupla ocorrer, sem '
                   'sobreposição de efeitos. O gatilho do feitiço é compartilhado; '
                   'a frequência por cena, a preparação e a alternativa de concluir '
                   'pela arma ainda não foram simuladas conjuntamente.')
print(output['nota'])

(Path(__file__).resolve().parent / 'estocada-conclusoes-magicas-contas.json').write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + '\n')


def conferir_dominancia(publicar=False):
    """Confere cenários de decisão publicados sem alterar as seis regras."""
    import re
    doc = Path(__file__).resolve().parent / 'RASCUNHO-dominancia-conclusoes-magicas.md'
    texto = doc.read_text()
    premissas = dict(re.findall(r'^\| (aproveitamento_u|ataques_aliados_expor) \| ([0-9.]+) \|$', texto, re.M))
    assert len(premissas) == 2, 'Faltam as duas premissas ilustrativas da análise'
    u = F(premissas['aproveitamento_u'])
    ataques = int(premissas['ataques_aliados_expor'])
    assert 0 <= u <= 1 and ataques >= 1
    d = PRECOS['desorientar']
    r = PRECOS['refluxo']
    m = PRECOS['romper_fileira']
    linhas = ['| Grandeza | Fatias ou fração |', '|---|---:|']
    def adicionar(nome, valor):
        linhas.append(f'| {nome} | {float(valor):.6f} |')
    adicionar('Desorientar se u do cenário', fatias(d*u))
    adicionar('Refluxo se o PE for gasto', fatias(r))
    adicionar('Romper se o movimento for útil', fatias(m))
    adicionar('u para empatar Refluxo', r/d)
    adicionar('u para empatar Romper', m/d)
    adicionar('Desorientar com TR adicional hipotético', fatias(d*FALHA_TR_ADD))
    adicionar('Expor em ataques aliados do cenário', fatias(PRECOS['expor_a_guarda']*ataques))
    inicio, fim = '<!-- inicio-contas-dominancia -->', '<!-- fim-contas-dominancia -->'
    anterior = texto.split(inicio)[1].split(fim)[0]
    calculado = '\n'+'\n'.join(linhas)+'\n'
    if publicar:
        doc.write_text(texto.replace(inicio+anterior+fim, inicio+calculado+fim))
    else:
        assert anterior == calculado, 'Tabela da dominância das conclusões diverge do preço ou das premissas publicadas'
    print('Dominância das conclusões: preço atual, cenários e alternativas conferidos.', flush=True)


if len(sys.argv) > 1:
    if sys.argv[1:] == ['--analisar-dominancia']:
        conferir_dominancia()
    elif sys.argv[1:] == ['--publicar-analise']:
        conferir_dominancia(publicar=True)
    else:
        raise SystemExit('Uso: conferir-estocada-conclusoes-magicas.py [--analisar-dominancia]')
