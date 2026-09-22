# LEIA PRIMEIRO — retomando a reforma do Bastião

*Cole este arquivo inteiro numa conversa nova, junto com os outros três do zip. Ele foi escrito para alguém que não tem o repositório montado nem as conversas anteriores.*

---

## O que é o projeto

**Projeto-M** é um sistema de RPG de mesa de Jujutsu Kaisen, escrito em português, mantido em `github.com/cupcake-mochi/JJK---Project`. Estava na versão `v0.239` quando este trabalho foi feito. Quem toca o projeto é o **Mizuki** (Gustavo Henrique), e ele é o dono de toda decisão de número.

O sistema tem **cinco Caminhos** — Bastião, Vanguarda, Guia, Emanador, Evocador — e **três Trilhas em cada um**. O Caminho entrega nos níveis `2 · 7 · 15 · 23 · 30`, a Trilha nos níveis `2 · 11 · 19 · 27`.

**O que foi feito nesta reforma: o Bastião inteiro — o Caminho e as três Trilhas (`Muro`, `Punho`, `Brasa`).** Os outros quatro Caminhos continuam intocados.

---

## Leia nesta ordem

1. **`reforma-caminhos-continuidade.md`** — o documento principal. Tem tudo: o problema que abriu a reforma, a pesquisa, as decisões com o porquê de cada uma, o texto das entregas, os preços, e a lista do que ficou aberto.
2. **`RASCUNHO-dano-movido.md`** — a régua nova que essa reforma precisou construir, e por que ela virou uma constante em vez de uma segunda moeda.
3. **`conferir-dano-movido.py`** — roda com `python3` e não precisa de nada instalado. Reproduz todo número citado, com regressão contra os documentos do repositório. **Se ele sair `TUDO OK`, os números do documento estão íntegros.**
4. **`contas/`** — os scripts de trabalho, um por rodada de decisão. Estão aí para conferência, não para rodar em sequência.

---

## As constantes, caso o repositório não esteja à mão

| base | valor | dono |
|---|---|---|
| `fatia` — a unidade de orçamento | `5,08` de dano por rodada, medida no nível 30 | `DESENHO-manhas.md` |
| orçamento de um Caminho | `5,00` fatias, em `4` degraus pagos | reforma |
| orçamento de uma Trilha | `5,00` fatias, em `4` entregas | reforma |
| `Rotina` no nível 30 — contra alvo padrão | `108,00` por rodada | peça 5 §2 |
| **saída por personagem contra CHEFE** | **`78,75` por rodada** | peça 26 §4.7 |
| rodadas de luta por dia | `10,5` — `3` lutas × `3,5` | peça 10 §4 |
| taxa de acerto base | `50%` | peça 1 |
| `1` PE | `5,14` de dano | peça 26 §6.5 |
| maestria | `1`/`2`/`3`/`4` por faixa de oito níveis | peça 1 §2 |
| `Desastre` nível 30 | `945` de vida, `219` por rodada em `3` ações, golpe de `73` | peça 26 §4.1 e §4.4 |
| vida por nível | Bastião `7` · Vanguarda e Guia `5` · Emanador e Evocador `4` | peça 6 |
| golpe simples no nível 30 | `11,50` **bruto** — aplique `50%` quando precisar acertar | peça 5 §4 |
| golpe desarmado no nível 30 | `11,50` bruto | peça 14 §5.0.6 |
| `1` tipo de resistência | `3,39` de dano evitado | `DESENHO-trilhas.md` |
| `+1` de Defesa | `3,39` de dano evitado · `1` ponto move `5` pontos percentuais | peça 5 §4 e peça 26 |
| desvantagem em um ataque do alvo | `18,00` permanente | `DESENHO-manhas.md` |
| posicionamento, por `1,5 m` | `0,90` permanente | peça 5 §4 |
| dano por Classe de feitiço | `18` por Classe: `18 · 36 · 54 · 72 · 90 · 108 · 126` | `manual/matematica/bf2.py` |
| Classe 0 no nível 30 | `27` de dano, `0` PE, não gasta ação | `DESENHO-trilhas.md` |
| `Bloquear` | `2d10−1` no lugar do `10` da Defesa — **neutro por construção** | peça 23 §2 |
| `2d10−1` | média `10,00` · média condicionada a ter falhado `7,00` | conta |

### A constante nova, que esta reforma criou

> ## `1` ponto de dano **movido** `=` `0,30` ponto de dano **causado**

**Provisória, decidida, não medida** — do mesmo jeito que o `5,08` e o `5,00` foram decididos.

Ela existe porque o Bastião é feito de **mover dano de uma pessoa para outra**, e a régua de dano é cega para isso: o grupo perde a mesma vida, só muda quem perde. *Dano **evitado** — redução, resistência, PV temporário — continua contando `1` pra `1`.*

**Ela não serve só ao Bastião.** Com ela passam a ter preço o `Ninguém Cai` do Guia, o `Escudo de Osso` do Evocador, PV temporário em geral, e o `Puxar Para Si` e o `Segurar` do Bastião velho — que **nunca foram medidos em versão nenhuma do projeto**.

---

## O estado: o que está fechado

O Bastião inteiro. **Caminho `5,20`–`5,58` · `Muro` `5,40` · `Punho` `4,60` · `Brasa` `5,51`**, contra `5,00` de orçamento cada.

**Os estouros são decisão declarada do Mizuki, não descuido.** O argumento dele está registrado: *tanque tancando bem não é o perigo, porque existe como lidar com tanque; dano fora da curva acaba a rodada de qualquer jeito.* E isso tem respaldo medido de antes — o `DESENHO-trilhas` registra que **um grupo de `Muro` não encurta luta nenhuma, ele estica**.

*Contexto para calibrar o que é muito: o maior estouro que o projeto tinha aceito antes desta reforma era a `Brasa` publicada, em `5,03` — ou seja `0,03`.*

---

## O que está aberto, na ordem

1. **Onze nomes.** Quatro no `Muro`, o `19` e o `27` do `Punho`, e os quatro da `Brasa`. *`Engate` e `Encontrão` ficam.* **Todo nome novo passa pelo `conferir-nomes.py`, que roda de `sistema/03-mecanica/`, e depois por checagem à mão de colisão de sentido — que o script não pega.**
2. **Uma correção em material publicado.** O `Fagulha` da `Brasa` está publicado em `4,08` e deveria ser `~2,00`: *o projeto conta o golpe simples a `50%` de acerto e o Classe 0 cheio*, e o Mizuki confirmou nesta conversa que **Classe 0 resolve por rolagem de acerto** — para virar Teste de Resistência precisaria da Melhoria de TR, que é Média, e um Classe 0 não tem orçamento para ela. **Metade do estouro histórico da `Brasa` é conta errada, não decisão.**
3. **Uma linha de playtest que resolve três discordâncias de uma vez.** *Quantos ataques são mirados no Bastião por rodada, e quantas vezes ele falha um `Bloquear`.* Ela decide o preço do `Aparar com Corpo`, do `19` do `Punho` e do `27` da `Brasa` — **os três lugares onde a leitura de mesa do Mizuki e a simulação discordam.** O playtest já está rodando; é um risquinho na ficha.
4. **Uma linha na peça 19.** Ela preçou a condição `Incapacitado` contando que perder o `Bloquear` vale zero, porque `Bloquear` é neutro. **Para o Bastião deixou de valer zero:** com o `Aparar com Corpo` na falha e o `19` do `Punho` no sucesso, **os dois resultados do `Bloquear` passaram a render**, e não sobrou nenhum que valha nada.
5. **Fechar a taxa de dano movido como peça** — dono declarado, validador com teste negativo, e os seis refinos listados na seção 7 do `RASCUNHO-dano-movido.md`.
6. **Repreçar com ela** o `Ninguém Cai`, o `Escudo de Osso`, o `Puxar Para Si` e o `Segurar`.
7. **Os outros quatro Caminhos** — Vanguarda, Guia, Emanador, Evocador — e o possível sexto, "Ágil" (agilidade, assassino, monge), que não existe no material atual e não tem nome.
8. **A recalibragem do Bestiário.** Ele calibra vida de chefe contra os `27,7%` antigos de ficha que são Caminho mais Trilha; com `5 + 5` fatias isso vai a `32,4%`.

### Dois bugs achados de caminho, que não são deste trabalho

- **O `conferir-nomes.py` devolve `Encaixe` como `LIVRE`**, e `Encaixe` é a Manha da Manopla, listada na peça 17 linha 118 e publicada no capítulo 8 do livro. *A ferramenta que existe para não repetir nome está deixando passar nome repetido.*
- **O `PROMPT-PROXIMA-CONVERSA.md` da raiz está parado na `v0.206`** e aponta para um trabalho que não é mais o da vez. *Quem retomar por ele pega o projeto errado.*

---

## Como o Mizuki quer trabalhar

**Ele é o dono de toda decisão de número.** Traga opções com o preço e o trade-off de cada uma já calculados, e pergunte. Rodadas curtas, uma decisão por vez, nunca uma proposta grande pronta.

**Não pergunte o que a conta responde.** Rode a conta. Todo número citado vem de script rodado, nunca de estimativa de cabeça — e quando não houver régua, diga *declarado, não medido*, em vez de inventar um valor.

**Quando ele decidir um número contra o medido, registre os dois.** O `0,50` do nível 27 da `Brasa` é dele; o medido é `0,32` a `5,42`. Os dois estão no documento, lado a lado, com o motivo da largura.

**Ordem para propor mecânica nova:** sensação → gatilho → o que substitui ou compete → regra → caso padrão e exceção → conta → teste de dominância e de bônus automático → o porquê.

### Quatro armadilhas que custaram caro nesta reforma

**Confira a COLUNA antes de usar o número.** A `Rotina` de `108` é contra alvo padrão; o `78,75` é contra chefe. Usar o primeiro no lugar do segundo fez uma luta durar `2,2` rodadas em vez de `4,45` e produziu a conclusão de que *"mover dano vale zero"* — que era o oposto da verdade.

**Compare os dois lados na mesma base.** Medir a entrada do `Encarar` **com** treino contra um envelope **sem** treino inflou um preço em `40%`. Quando um bônus é do personagem e não do degrau, ele move os dois lados e a razão não muda.

**Esse número já inclui o que eu estou somando nele?** O projeto conta o golpe simples a `50%` de acerto e o Classe 0 cheio. Foi isso que deixou o `Fagulha` publicado com o dobro do preço real.

**Gatilho antes da rolagem cobra o fator de erro; gatilho depois, não.** Foi o que separou o `Absorver` da `Interposição` e cortou o preço dela pela metade — e é o que faz o `Aparar com Corpo` render `7,00` enquanto o `19` do `Muro` rende `10,00`, com o mesmo dado.

### E duas regras de desenho que saíram desta reforma

**Nunca deixe magnitude e contador de usos crescerem juntos.** Trava um, deixa o outro subir. Foi isso que explodiu o `Corpo Duro` velho em `3,77` fatia sozinho.

**Evento não vira identidade; estado vira.** Foi o achado que reescreveu o Caminho inteiro. Uma regra de roteamento diz quem leva o dano e não diz nada sobre quem o personagem é — e a capa do Bastião estava escrita na primeira linha dele desde sempre, *"o corpo é a resposta: aguentar, encarar, prender"*, com **encarar** sem mecânica nenhuma em nenhum dos cinco Caminhos.

---

## Como ele escreve, e como quer que você escreva

Português brasileiro, informal, direto. **Nada de norma culta antiga nem português de Portugal.** Sem gírias de RPG e sem tom performático, mesmo falando de RPG.

**No chat:** uma ideia por parágrafo, frase curta, número sempre com a unidade por extenso. Não escreva resumo em prosa por cima de tabela que o script já imprimiu.

**No documento:** negrito abrindo com a regra e a razão logo depois, falando com o leitor por *você*, parêntese para exceção curta. Seções de tamanhos diferentes, sem simetria forçada.

**Na pesquisa:** precisão vale mais que velocidade. Nome ou termo que ele citar é âncora literal — busque o termo exato antes de generalizar. Vá a fundo, cruze fontes, e cheque se a informação mudou de status depois: retcon, revelação posterior, correção.

---

## Por onde começar

**O trabalho mais barato e mais travante é o item 1: os onze nomes.** Eles bloqueiam a peça virar texto de manual, e cada um leva uma rodada do `conferir-nomes.py` mais uma leitura à mão.

**O mais valioso é o item 5**, fechar a taxa de dano movido — porque ela destrava o item 6, e o item 6 são quatro entregas que estão sem preço há versões.

Pergunte ao Mizuki por qual ele quer começar. Não escolha por ele.
