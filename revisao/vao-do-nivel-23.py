"""O nível 23 já foi degrau de Caminho, e saiu na v0.70. Esta conta refaz o vão.

Fonte: `referencia-jjk-project/sistema/03-mecanica/RASCUNHO-trilhas.md`, Q2.
Ela publica dois pares medidos — o calendário antigo em `vão 5 · seca 24` e o
atual em `vão 8 · seca 31`, "as duas por causa do degrau do nível 23 que saiu".

O vão é a maior distância, em níveis, entre duas entregas seguidas de qualquer
tipo. O modelo abaixo tem de reproduzir os DOIS números publicados antes de
dizer qualquer coisa sobre um calendário novo. A seca é em missões e o modelo
dela não veio junto na cópia de referência; não é reproduzida aqui.
"""

TRILHA = (2, 11, 19, 27)

CALENDARIOS = {
    'antigo, até a v0.70      C 7·15·23·29':      (7, 15, 23, 29),
    'atual, da v0.70 em diante C 2·7·15·30':      (2, 7, 15, 30),
    'com o 23 de volta        C 2·7·15·23·30':    (2, 7, 15, 23, 30),
}
PUBLICADO = {'antigo, até a v0.70      C 7·15·23·29': 5,
             'atual, da v0.70 em diante C 2·7·15·30': 8}


def vao(caminho):
    todas = sorted(set(TRILHA) | set(caminho))
    saltos = [(b - a, a, b) for a, b in zip(todas, todas[1:])]
    return max(saltos), todas


print('Entregas de Trilha, fixas em todos os casos:', ' · '.join(map(str, TRILHA)))
print()
print(f'{"calendário":40s} {"maior vão":>10s}  onde')
for nome, cam in CALENDARIOS.items():
    (salto, a, b), todas = vao(cam)
    print(f'{nome:40s} {salto:10d}  entre o nível {a} e o {b}')
    print(f'{"":40s}            entregas: {" · ".join(map(str,todas))}')

print()
for nome, esperado in PUBLICADO.items():
    (salto, _, _), _ = vao(CALENDARIOS[nome])
    assert salto == esperado, (nome, salto, esperado)
    print(f'contra-teste: {nome.split()[0]:8s} reproduz o vão {esperado} publicado na Q2  OK')

(novo, a, b), _ = vao(CALENDARIOS['com o 23 de volta        C 2·7·15·23·30'])
print()
print(f'Repondo o degrau no 23, o maior vão volta a ser {novo} níveis, entre o {a} e o {b}.')
print('É o mesmo 5 que a Q2 escolheu o calendário misto para ter.')
print('O 8 de hoje é o buraco entre a entrega de Trilha do 19 e a do 27: sete níveis sem nada.')

# contra-teste da alternativa: e se o degrau novo fosse em outro nível?
print()
print('Contra-teste — e se o degrau extra fosse em outro lugar do buraco 19–27?')
for nv in (20, 21, 22, 23, 24, 25, 26):
    (salto, a, b), _ = vao(tuple(sorted(CALENDARIOS['atual, da v0.70 em diante C 2·7·15·30'] + (nv,))))
    marca = '  <- o menor vao possivel' if salto == novo else ''
    print(f'  degrau no {nv}: maior vão {salto} (entre {a} e {b}){marca}')
print('O 23 não é o único que fecha o buraco; 22, 23 e 24 empatam. A escolha entre eles é de sabor,')
print('e o 22 já é marco no sistema (peça 18), o que faz dele o mais cheio dos três.')
