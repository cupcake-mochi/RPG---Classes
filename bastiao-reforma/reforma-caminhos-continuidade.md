# Reforma de identidade dos Caminhos — prompt de continuidade

*Segunda versão. Substitui a de antes por inteiro — o nível 2 do Bastião foi reaberto, medido de novo e trocado de forma. Escrito pra retomar em outra sessão sem reexplicar.*

> **Estado do repositório quando isto foi escrito:** `v0.239`, de 14/09/2026. Lido via zip, não montado.
> ⚠ **O `PROMPT-PROXIMA-CONVERSA.md` da raiz está parado na `v0.206`** e aponta pro exemplo guiado de invocação, que não é mais o trabalho da vez. Ele também diz que `04-playtest/` está vazia, e o `README` diz que o playtest começou na `v0.215`. **Quem retomar por ele pega o projeto errado.**

---

## O problema que abriu isso

Jogadores reclamaram que os Caminhos dão benefícios pequenos e sem identidade forte. A única exceção é a rota Yumi, dentro da Trilha Batedor do Vanguarda.

Por que a Yumi funciona: ela tem uma imagem única contada em prosa, um mecanismo só que escala nos quatro níveis em vez de trocar de ideia a cada grau, uma decisão com custo real todo turno, e o nome contando a mesma história que a mecânica.

**E nesta conversa apareceu um quinto motivo, que é o que estava faltando:** a Yumi é uma **postura**, não um evento. Você não se moveu, você firmou o corpo, você é o cara de cima da árvore. Dá pra descrever na mesa sem abrir a ficha.

---

## Onde os números moram

- Repositório: `github.com/cupcake-mochi/JJK---Project`.
- **`fatia`** é a unidade de orçamento: `5,08` de dano por rodada, medida no nível 30.
- Peça oficial: `sistema/03-mecanica/06-caminhos-e-trilhas.md`. Rascunhos ativos: `DESENHO-caminhos.md` e `DESENHO-trilhas.md`, na raiz.
- `manual/matematica/pac7.py` e `v7.py` validam **só** a economia de feitiço. Não tocam em Caminho nem Trilha.

### Bases que esta conversa usou, com o dono de cada uma

| base | valor | dono |
|---|---|---|
| fatia | `5,08` de dano por rodada, nv30 | `DESENHO-manhas.md` |
| Rotina, nv30 | `108` de dano por rodada | peça 5 §2 |
| **o que UM personagem entrega contra o chefe do nv30** | **`78,75` por rodada** | peça 26 §4.7 |
| rodadas de luta por dia | `10,5` — `3` lutas × `3,5` | peça 10 §4 |
| taxa de acerto | `50%` | peça 1 |
| `1` PE por rodada | `5,14` de dano por rodada | peça 26 §6.5 |
| golpe do `Desastre`, nv26–30 | `73`, em `3` ações, `219` por rodada | peça 26 §4.4 |
| vida do `Desastre`, nv30 | `945` | peça 26 §4.1 |
| golpe simples, nv30 | `11,50` bruto | peça 5 §4 |
| desvantagem no próximo ataque do alvo | `18,00` permanente | `DESENHO-manhas.md` |

> ⚠ **O `78,75` e a `Rotina` de `108` não são a mesma coisa, e trocar um pelo outro estraga a conta.** *A `Rotina` é contra alvo padrão; o `78,75` é contra o chefe, que tem Defesa de chefe.* **Esta conversa rodou a luta com `108` primeiro e chegou em "mover dano vale zero"** — com o `78,75` a mesma luta dá `3` pessoas caídas e a conclusão vira do avesso. *É a lição nº 2 na sua forma mais cara: o número existia no documento certo, na tabela certa, e na coluna errada.*

---

## Os dois achados de conta que reabriram o nível 2

### 1 · O preço estava contado em dobro

O `Absorver` velho dispara **ao ser atingido** — nenhum uso cai em ataque que erra. A `Interposição` que a versão anterior deste documento fechou dispara **quando um inimigo ataca**, antes do dado, porque a troca de alvo tem de acontecer antes ou a rolagem teria sido contra a Defesa do aliado.

Metade dos ataques erra, então metade dos usos não reduz nada.

```
2 usos × 33,5 de dano evitado × 50% ÷ 10,5 rodadas
  = 3,19 de dano por rodada = 0,63 fatia, e não 1,26
```

**Os dois números da versão anterior reproduzem exato** — o `Absorver` em `3,77` e a `Interposição` em `1,26` —, e é por isso que dá pra confiar que o `0,63` é o certo: a mesma conta, com o fator que faltava.

### 2 · A porta de PE nunca compensa

Pagar Maestria em PE pra usar de novo, medido contra o câmbio de `1` PE `= 5,14` de dano:

| nível | custa | de dano largado | evita | troca |
|---|---|---|---|---|
| 2 | `1` PE | `5,14` | `2,75` | `0,54 ×` |
| 18 | `3` PE | `15,42` | `10,75` | `0,70 ×` |
| 30 | `4` PE | `20,56` | `16,75` | `0,81 ×` |

**Nenhum nível chega em `1,00`.** Pelo livro-caixa ninguém aperta esse botão nunca, e ela tinha sido vendida como a decisão com custo real do degrau.

*Fica em aberto se isso é defeito ou desenho: pagar caro de propósito pra alguém específico não cair é coerente, desde que esteja escrito em vez de suposto.*

---

## O que a pesquisa derrubou

**A `Interposição` é uma regra de roteamento, e regra de roteamento não vira identidade.** Ela decide quem leva o dano e não diz nada sobre quem o personagem é.

Levantamento, com o que cada saída custa:

| quem | como resolve "eu tomo o golpe" | o que custa |
|---|---|---|
| **D&D 2024, Bárbaro** | não resolve — a Fúria é aguentar, não interceptar | o tanque do 5e é emergente, não existe na régua |
| **D&D 4e, Defensor** | `Marcado`, com penalidade pra quem ignora | o mestre pode ignorar, e a força varia de mesa pra mesa |
| **PF2e, Champion** | Reação com gatilho em **dano causado**, sem contador de dia | magnitude pequena porque a frequência é alta |
| **o Bastião de antes** | Reação com gatilho em ataque, `2` usos no dia | metade queima em erro, e não tem rider |

**Três coisas do Champion batem no que a conta já tinha pedido sozinha:** o gatilho é dano causado e não ataque; a resistência é `2` mais o nível, contra o `nível + 1d6` daqui; e ele tem rider, que é um golpe de volta.

**E a capa do Champion não está na Reação — está no juramento com anátema.** A Reação é mecânica. A capa é a coisa que você não pode fazer.

> **A Fúria também não faz duas coisas.** *Contado na fonte:* resistência a três tipos, dano da Fúria, vantagem em testes **e** salvaguardas de Força, a proibição de conjurar, um relógio de manutenção com três saídas, e um contador que recarrega no descanso curto. **Três benefícios, uma restrição, um relógio e um contador — e o Bárbaro de nível 1 ainda leva Defesa sem Armadura e Maestria em Arma por cima.**
>
> **O que faz a Fúria ler como peça só não é ter uma parte. É todas as partes dizerem a mesma frase.**

**E a reclamação tem nome e dez anos de fórum em cima.** O RPGBOT escreveu *The Tank Fallacy*: RPG de mesa não tem taunt nem aggro, e o objetivo do Defensor é proteger os aliados e não simplesmente sobreviver. No RPG PUB a conclusão é mais dura — o papel quase não existe porque as mecânicas de que ele depende vêm de jogo eletrônico e não conectam com a ficção.

*Fontes:* `rpgbot.net/the-tank-fallacy/` · `rpgpub.com/threads/tanks-in-ttrpgs-why-so-much-fuss.11345/` · `2e.aonprd.com/Causes.aspx` · `pf2.d20pfsrd.com/class/champion/`

---

## A capa já estava escrita, e ninguém tinha pegado

O livro abre o Bastião assim:

> **O corpo é a resposta: aguentar, encarar, prender.**

Os degraus antigos batiam nisso — o `Corpo Duro` era **aguentar**, o `Segurar` era **prender**.

**A `Interposição` não é nenhum dos três.** Ela é *proteger*, um quarto verbo que ninguém declarou. A reforma tinha trocado o que o Bastião é sem ninguém marcar.

E **encarar não tem mecânica nenhuma, em degrau nenhum, em nenhum dos cinco Caminhos.**

> ⚠ **Pior: `Intimidação` era perícia FIXA do Bastião, entrava na ficha na criação, e nenhum degrau do Caminho ou das três Trilhas dele tocava nela.** *(Ela foi trocada por `Provocar` no fim desta conversa — ver o chassi acima.)* *Conferido por grep na peça 6, no `DESENHO-caminhos` e no `DESENHO-trilhas`: zero ocorrências.*

**O gancho da obra existe e é de wiki, então ainda não serve pra documento:** energia amaldiçoada forte gera pressão física que mete medo em quem sente, e isso é descrito como intimidação. *Precisa achar o capítulo antes de virar linha de regra.*

**E ele não pode ser a base da aura, por decisão do Mizuki:** nem todo mundo tem energia neste sistema. Um Bastião Sem Técnica ou de Restrição Celestial ficaria sem a coisa que define o Caminho dele. **A aura é presença física — corpo, tamanho, cara —, e é isso que o fórum descreve como tanque de verdade na mesa: grande, resistente, e parecendo assustador.** *Serve pra Maki tanto quanto pro feiticeiro.*

---

## A decisão desta conversa

**O nível 2 do Bastião deixa de ser um evento e vira um estado.** A âncora de redirecionamento duro sobrevive inteira — o que muda é a forma.

> **"Eu sou o problema agora."** Você não intercepta golpe. Você fica impossível de ignorar, e ignorar custa caro.

**As quatro escolhas do Mizuki, fechadas:**

1. **O encarado sente.** Uma aura de presença, com cuidado pra não virar o `Provocar` com número maior.
2. **Área em volta, tirando aliados** — e não um alvo por vez.
3. **Manter não custa nada.** O custo é o dano que você come, e cobrar um segundo custo é cobrar duas vezes pela mesma coisa.
4. **Entra com Ação Bônus.**

**Tamanho proposto, ainda não batido: `6 m`.** *É o raio do Domínio Simples, é o que o `Passo` fecha, e é maior que os `4,5 m` do `Aterro` — então a Trilha `Muro` aprofunda dentro da área do Caminho em vez de empatar com ela.*

### A trava que qualquer redação vai bater

**`Provocar` já existe como Ação Bônus pra todo mundo:** teste contra o Teste de Resistência de Espírito, e numa falha o alvo ataca qualquer um que não seja você com desvantagem e você com vantagem.

Então o Bastião não pode ser `Provocar` com número maior — isso é o teste do bônus automático virado do avesso. **O que ele precisa é da coisa que o `Provocar` não faz: não ser disputado, e ser estado em vez de uma rodada.**

### A ideia que sustenta tudo

**Não escreve teto nenhum. Você aceita quantos golpes quiser por rodada, e a conta te mata se exagerar.**

O limitador não é contador, não é PE, não é uso por dia. **É a barra de vida, em tempo real, na mesa, com todo mundo vendo.** É o que faz "o corpo é a resposta" parar de ser frase de abertura: o corpo vira o **recurso**.

*O 4e usa Marca com penalidade, o Pathfinder usa slot de Reação, o 5e não usa nada. **Nenhum dos três põe o recurso na barra de vida.***

---

## O que a conta trava

**O teto tem de ficar do lado do Bastião, nunca do lado do inimigo.** Um estado que puxa tudo mata ele mais rápido do que não fazer nada: quatro capangas puxados ao mesmo tempo, no nível 30, entregam `110` por rodada contra `210` de vida — `1,9` rodada.

**E a curva de quanto puxar não é monotônica.** Luta de quatro pessoas contra o `Desastre` do nível 30, com o chefe concentrando no mais frágil:

| puxa por rodada | rodadas | quem cai |
|---|---|---|
| `0` | `4,45` | três pessoas |
| `1` | `3,60` | duas |
| **`2`** | **`3,05`** | **uma** |
| `3` | `3,45` | duas — **e uma delas é o Bastião** |

**O pico é `2`, e passar dele te devolve pro mesmo lugar por outro motivo.** Então a decisão com custo real todo turno já existe no desenho sem ninguém escrever regra pra ela: toda rodada o jogador olha a própria vida e decide quanto da luta é dele.

> *O modelo reproduz um número que ele não foi ajustado pra dar:* **sem nenhuma ajuda, ele derruba `3` de `4` em `4,45` rodadas**, e a peça 26 §4.2 publica *"ele derruba `2,70` pessoas se concentrar"* e *"com atrito, os quatro em cinco rodadas"*. **Duas rotas independentes no mesmo lugar.**

---

## A camada de Trilha, decidida em princípio

**O Champion tem uma Reação só, e a causa escolhida decide o rider.** Isso mapeia direto nas três Trilhas do Bastião:

- **Muro** — você come e fica mais duro
- **Punho** — você come e devolve na hora
- **Brasa** — você come e aquilo vira energia

**Mesmo estado embaixo, três respostas em cima.** Resolve a reforma das três Trilhas junto com o Caminho em vez de depois.

---

## O preço, e a constante que saiu disso

**Mover dano não tinha conversão em fatia, e a reforma inteira do Bastião é feita de mover dano.**

A primeira tentativa construiu uma segunda moeda — contar **quedas evitadas**. **Foi abandonada por decisão do Mizuki, e por um motivo bom:** *contar queda mede o desenho no caso em que ele deu certo, e não o trabalho que ele faz.* **Um Bastião que tanca a luta inteira sem que ninguém fosse cair mesmo assim fez o trabalho, e a unidade "queda" marcava zero.**

**O que ficou no lugar é uma constante, e não uma moeda:**

> ## `1` ponto de dano movido `=` `0,30` ponto de dano causado

***Provisória, decidida, não medida*** — igual o `5,08` da fatia e o `5,00` por Caminho foram decididos.

**Caso de referência:** o Bastião toma `2` golpes numa luta de `3` rodadas, `3` lutas por dia. No nível 30 são `146` por luta, `438` por dia, `41,71` por rodada do dia.

**E ela é plana.** Contra a `Rotina` de cada faixa, o degrau vale `9,5%` no nível 10, `11,1%` no 20 e `11,6%` no 30. *Entra como constante, sem tabela por faixa.*

> **Ela não nasceu pro Bastião.** *Passam a ter preço também:* o `Ninguém Cai` do Guia, o `Escudo de Osso` do Evocador, PV temporário, a Trilha `Muro` inteira, e o `Puxar Para Si` e o `Segurar` do Bastião velho — **que nunca foram medidos em versão nenhuma do projeto.**

**O rascunho dela é o `RASCUNHO-dano-movido.md`**, que substitui o `RASCUNHO-corpo-de-pe.md`. O modelo de luta que a primeira rota construiu **não virou lixo**: ele continua sendo o que valida se a taxa produz um jogo que funciona, e foi ele que mostrou que puxar `3` golpes por rodada derruba o próprio Bastião.

---

## O nível 2, fechado

> **Nível 2.** Você rola **`Intimidação` e `Provocar` com Força** em vez de Essência, sempre. E você ganha o `Encarar`.
>
> **`Encarar`.** **Ação Bônus.** Uma área de **`6 m` em volta de você**, que dura até o fim da cena. Você pode cancelar como ação livre no seu turno.
>
> **Ao entrar, você provoca os alvos no ambiente.** Role `Provocar` uma vez, contra o Teste de Resistência de Espírito de até **metade da sua Força, arredondando para baixo, mais `1`** inimigos dentro da área. Quem falhar sofre o efeito da ação `Provocar`, **até o começo do seu próximo turno**. **Uma vez por cena.**
>
> Enquanto o `Encarar` estiver de pé:
>
> **Quando um ataque com rolagem acerta um aliado dentro da área**, você pode gastar a sua **Reação**: aquele golpe passa a ser contra você. **O acerto vale contra você sem nova rolagem**, e tudo o que ele faria no aliado acontece em você — **inclusive crítico e condição**. **Você leva o golpe inteiro.**

**Preço: `2,46` fatia**, de um orçamento de Caminho de `5,00`. **Sobra `2,54` pros níveis 15, 23 e 30.**

*O `2,46` preça o degrau **inteiro**, e não uma cláusula dele: o caso de referência é "`2` golpes tancados por luta", que é o trabalho total da peça — o que veio da Reação e o que veio do `Provocar` estão os dois dentro.*

**O `X` fechou em `metade da Força + 1`.** *O `+ 1` é decisão do Mizuki, pra que o Bastião pegue pelo menos `2` alvos já na criação.*

### Por que cada linha está ali

**`Intimidação` com Força** resolve uma colisão: a peça 1 §5.5 já dá **vantagem** em `Intimidação` pela `Cicatriz`, e vantagem não empilha. *Dar vantagem no Caminho apagaria o lado bom da `Cicatriz` pro personagem que mais coleciona cicatriz.* **Trocar o atributo soma com ela em vez de anular**, e é maior na prática — tira o Bastião de um modificador perto de `0` e põe em `5` ou `6`.

**`Provocar` com Força** pelo mesmo motivo, e porque sem isso o Bastião falharia sempre: `Provocar` é perícia de **Essência** e os naturais dele são Força e Constituição. *Não excede a base do projeto — restaura ela.* **Precedente literal:** a `Empunhadura` do Arremate e o `Compasso` da Estocada já trocam atributo assim, os dois no nível 2.

> ⚠ **A peça 7 define `Provocar` e `Intimidação` como opostos** — *uma faz recuar, a outra faz avançar* — e já tinha marcado a tensão como pergunta aberta. **Dar atributo nas duas é mais brando que dar vantagem nas duas**, porque não diz que você é bom nas duas coisas, diz que as duas saem do corpo. *Mas agora tem um degrau encostando nessa pergunta.*

**`6 m` em volta de você**, e não *a partir de você*. *A preposição resolve sozinha se a área anda com o Bastião:* o `Chão` do Perímetro usa *a partir de* e **precisou** da cláusula *"e ela anda com você"*; o `Aterro` do Muro usa *em volta de* e nunca precisou.

**O gatilho é `acerta`, não `ataca`.** *Gatilho antes da rolagem queima metade dos usos em ataque que erra — foi o que separou o `Absorver` da `Interposição` e cortou o preço dela pela metade.*

**Sem exceção de área escrita.** *A peça 1 §7 diz que o manual resolve feitiço de três jeitos — Acerto, Teste de Resistência e Automático — e que Explosão nunca crita, porque não tem rolagem.* **Então "ataque com rolagem" já exclui área sozinho.** *(Confirmado pra Explosão; falta conferir Cone, Linha e Onda.)*

**Sem redução.** *Isso deixa a Trilha ser a dona do rider*, que é a estrutura do Champion, **e deixa a redução como o crescimento óbvio do nível 15** — mesmo mecanismo crescendo, e não ideia nova.

### O `X`, e por que ele é metade

Na régua em que o `Provocar` foi aprovado — pontos percentuais por cena. **O envelope aprovado é `43,75` pp**, que é a ação `Provocar` usada toda rodada da luta.

| Força | alvos | pp na entrada | do envelope |
|---|---|---|---|
| `2`–`3` | `2` | `25` | `57%` |
| `4`–`5` | `3` | `37,5` | `86%` |
| `6` | `4` | `50` | `114%` |

**Força cheia foi recusada.** *Ela chegava a `171%` do envelope, e pior: Força de Bastião já nasce em `3` ou `4`* — com os nove pontos da criação — **então o degrau entregaria quase tudo na primeira sessão e não teria o que crescer nos treze níveis seguintes.**

> **Metade é o padrão da casa, e ele é unânime:** *pactos permanentes usam `metade da Essência`; as marcas de Expansão usam `metade da Inteligência + metade da maestria`; o `Escora` usa `metade da Constituição`; o `Aprumo` e o `Acelerar` usam metade também.* **O projeto nunca usa atributo cheio como contador.**

**O teto de `4` alvos só chega com Força `6`**, que é estado de fim de campanha — e cai no mesmo `114%` onde `Maestria` cairia no nível 30. *A rampa passou a ser de investimento e não de calendário: cresce quando o jogador escolhe, não quando o nível vira.*

**E isso tira Constituição do limbo.** *Se Força governasse o número de alvos inteiro, ela destravaria quatro coisas no mesmo Caminho — ataque, `Intimidação`, `Provocar` e alvos — e Constituição viraria lixo numa classe de `7` de vida por nível.* **Do jeito que ficou, Força é com quem você encara e Constituição é a barra que o `Encarar` gasta.**

> ⚠ **Com Força `0` ou `1` a conta dá `1` alvo, não zero** — o `+ 1` é o piso. *O texto diz **até**, então com menos inimigos na área do que a conta permite você provoca quantos houver.*

### O que o degrau ainda deve

**O `Escora` quebrou.** *O que ele vendia era gastar um uso num aliado a `9 m`, e o `Encarar` dá isso de graça no nível 2.* **Sobrou nada pra ele** — entra na fila de reescrita das Trilhas.

**Bônus automático, declarado e não escondido.** *Puxar uma vez por rodada custa metade da vida e ele ainda sai de pé*, então no nível 2 contra um inimigo só, puxar sempre é quase de graça. **A decisão só morde com mais de um inimigo, em luta longa, ou a partir do nível 7, quando o `Não Pega` passa a disputar a mesma Reação.**

**Quem entra na área depois nunca é provocado.** *O reforço que chega na rodada `3` está dentro da aura e imune a essa metade.* **É decisão, não descuido** — a aura ainda redireciona golpe dele.

**O `Provocar` não força.** *Ele dá uma escolha ao inimigo: atacar outro com desvantagem, ou atacar você com vantagem.* **É a única parte do degrau onde o mestre ainda joga**, e isso é propriedade boa: o redirecionamento da Reação é duro e igual em toda mesa, e o `Provocar` é onde a agência volta.

### Os nomes

**`Encarar` passou na triagem como `LIVRE`.** *Fecha o laço:* o verbo estava na linha de abertura do Caminho — *"o corpo é a resposta: aguentar, encarar, prender"* — **sem mecânica nenhuma em nenhum dos cinco Caminhos.** Agora ele é a mecânica.

*Também passaram, e ficam disponíveis:* `Desvio` · `Peito` · `Resgate` · `Baque` · `Entrada` · `Fisgada` · `Avanço` · `Atravessar`.

---

---

## O Caminho fechado

**Vida `7`/nível · PE `4`/nível · Força · Constituição · Atletismo · `Provocar` · as treze categorias de arma.**

> ⚠ ***Mudança no chassi, e ela toca material publicado:*** **a perícia fixa `Intimidação` foi trocada por `Provocar`.** *O livro traz `Atletismo · Intimidação`.*
>
> **A razão sai da peça 7, que define as duas como opostas:** *`Provocar` é forçar a vir para cima de você; `Intimidação` faz recuar.* **A fantasia do Caminho é *vem pra cima de mim*, então `Provocar` é a perícia dele e `Intimidação` nunca foi.**
>
> ***A troca de atributo do nível 2 continua valendo para as duas.*** *O Bastião pode pegar `Intimidação` entre as cinco livres, e intimidar com o corpo continua sendo a ficção certa — a peça 7 diz que elas são opostas no **efeito**, não que a mesma pessoa não possa ter as duas.* **E manter as duas resolve de graça o achado da `Cicatriz`: ela dá **vantagem** em `Intimidação`, vantagem não empilha, e atributo empilha.**
>
> **O treino não encarece o degrau, e a conta confirma:** *perícia treinada soma maestria, o que sobe o sucesso de `50%` para `70%` no nível 30.* **Mas isso move os DOIS lados da comparação** — se o Bastião é treinado, a ação `Provocar` dele também melhora. *Envelope com treino: `25 × 0,70 × 3,5 = 61,25` pp. Entrada com Força `6`: `4 × 25 × 0,70 = 70` pp.* **Razão `114%`, idêntica à de antes.**
>
> ***Decisão do Mizuki: é peso externo já esperado, e o preço do degrau não muda.*** *É irmão do erro do `78,75` contra o `108` — comparar duas coisas medidas em bases diferentes.*

### Nível 15 — `Aparar com Corpo`

> **Quando o seu `Bloquear` falha, você reduz o dano daquele golpe no que os dados mostraram, mais a sua Constituição.** **Uma vez por rodada.**
>
> Só os dados do `Bloquear` entram. Destreza e proteção ficam de fora.

**`2,12` a `2,50` fatia**, na régua de dano evitado, que conta `1` pra `1`.

**Por que só os dados.** *Se a redução fosse o `Bloquear` inteiro, com Destreza e proteção, custaria de `3,90` a `5,20` — passa o Caminho todo em qualquer faixa.* **E quem investisse nos modificadores falharia menos E reduziria mais quando falhasse: os dois bônus na mesma direção, que é a armadilha que derrubou o `Corpo Duro`.**

**Por que teto de `1×` por rodada, e o achado que veio dele.** *Com o teto você fica com a **melhor** falha da rodada, não com uma qualquer* — a média sobe de `7,00` para `7,98`. **O teto deixa de ser corte de frequência e vira escolha**, e isso caiu da grade, ninguém desenhou.

> ⚠ **A auto-limitação enfraqueceu, e foi troca consciente.** *Só a rolagem dava razão de `1:10` entre a pior e a melhor; com Constituição cheia dá `1:2,3`.* **Somar Constituição põe um piso garantido de `6` e o dado passa a decidir menos** — *decisão do Mizuki, ciente do número.*

**Golpe puxado pelo `Encarar` não se bloqueia**, porque o acerto transfere sem nova rolagem. *Então este degrau só dispara em ataque **mirado nele** — e o que mira ataque nele é o `Provocar` do nível 2.* **As duas metades do `Encarar` se alimentam por aqui, e isso apareceu na conta em vez de no desenho.**

> ⚠ **Dívida na peça 19.** *Ela preçou `"você não pode Bloquear"` do `Incapacitado` em zero, porque `Bloquear` é neutro por construção.* **Para o Bastião deixou de ser zero.** *Precisa de uma linha lá dizendo que a condição tem exceção para este Caminho.*

### Nível 23

> **O `Provocar` do `Encarar` dispara de novo** toda vez que um inimigo entra na área **por vontade própria**. E a área passa a ser de **`9 m`**.

**`0,00` fatia** — ele se move na régua de pontos percentuais, que é onde o `Provocar` vive.

*O `"por vontade própria"` é do Mizuki e tampa um buraco real:* **sem ele, um inimigo empurrado para dentro da área — pelo `Encontrão` do `Punho`, por exemplo — dispararia o `Provocar` de graça.**

E ele fecha o furo declarado do nível 2: *o reforço que chega na rodada `3` deixa de ser imune à metade provocadora do degrau.*

### Nível 30 — `Passa Pra Mim`

> **Ação Livre. `1×` por cena.** Quando um aliado dentro da sua área chegaria a `0` de vida, ele fica com `1`, e **você leva o dano excedente**.
>
> **Se o excedente derrubar você, você cai.**

**`0,62` fatia.** Excedente médio de `36,5` no nível 30, que é `17%` da vida do Bastião de uma vez, fora de turno.

**Ação Livre e não Reação, por decisão do Mizuki, e está certo:** *a Reação é o gargalo do Caminho inteiro, e pôr o capstone nela faria ele competir com a coisa que define a classe.*

**Não colide com o `Ninguém Cai` do Guia, mas quase colidiu no nome.** *Lá o excedente é **anulado**; aqui ele **vem para você**.* **`Último a Cair` foi recusado justamente por não dizer isso** — ele empatava com o `Ninguém Cai` na frase e no gatilho, e ainda ficava treze níveis depois do `Ainda de Pé`, no mesmo Caminho. **`Passa Pra Mim` nomeia a transferência, que é a única coisa que separa os dois.**

### O livro-caixa

| degrau | fatia | régua |
|---|---|---|
| `2` · `Encarar` | `2,46` | dano movido `× 0,30` |
| `7` · ataque extra `+` `Não Pega` `+` `Ainda de Pé` | `0,00` | grátis, correção de base |
| `15` · `Aparar com Corpo` | `2,12`–`2,50` | dano evitado `1` pra `1` |
| `23` · redispara `+` aura `9 m` | `0,00` | pontos percentuais |
| `30` · `Passa Pra Mim` | `0,62` | dano movido `× 0,30` |
| **total** | **`5,20`–`5,58`** | de `5,00` |

> ⚠⚠ ***O Caminho estoura de `0,20` a `0,58`, e isso é decisão declarada do Mizuki, não descuido.*** *O maior estouro que o projeto já tinha aceito era a `Brasa` publicada em `5,03` — **`0,03`**.* **Este é de sete a dezenove vezes maior. Quem vier depois precisa saber que a régua foi esticada de propósito, e exatamente onde.**

**A faixa do nível 15 não é imprecisão de conta — é uma discordância de leitura de mesa.** *O Mizuki lê `~1` falha de `Bloquear` por combate; a simulação lê `2` a `3` ataques mirados nele por rodada, o que dá `3` usos por cena com o teto.* **Instrumentação pedida ao playtest: um risquinho na ficha contando quantas vezes por combate o Bastião falhou um `Bloquear`.**

**Este Caminho é o primeiro do projeto a pagar em três réguas.** *É consequência direta de ele ser o único que faz o dano acontecer em outro lugar em vez de acontecer mais.*

**Calendário combinado com a Trilha:** `2 · 7 · 11 · 15 · 19 · 23 · 27 · 30`, vãos de `5 · 4 · 4 · 4 · 4 · 4 · 3`.

---

## Trilha `Muro` — refeita sobre o `Encarar`

**Ela era a única das três Trilhas do Bastião com as quatro entregas preçadas**, em `4,87` de `5,00`. *O `Encarar` quebrou duas das quatro.*

> ⚠ **O `Escora` do nível 19 morreu inteiro.** *Ele vendia duas coisas — mais usos do `Absorver`, e poder gastar num aliado a `9 m`.* **O `Encarar` dá a segunda de graça no nível 2, e o `Absorver` não existe mais.** *Não sobrou nada para consertar, e ele era `1,33` — `27%` da Trilha.*

> ⚠ **A `Cúpula` do 27 apontava para coisas que mudaram de dono**, porque dizia *"o `Alicerce` passa a segurar quatro tipos"* e *"todo aliado dentro do seu espaço"*. **Com a fusão, o espaço do `Muro` deixou de existir como coisa separada — passou a ser a aura do `Encarar`.**

### As quatro, como ficaram

> **Nível 2.** Dois tipos de dano à sua escolha caem pela metade contra você, **enquanto o `Encarar` estiver de pé**. *Mesma Ação Bônus — não são duas posturas.* Os tipos se escolhem no fim de cada descanso longo.

> **Nível 11.** Um aliado **adjacente a você** tem **cobertura `Parcial`** — `+2` de Defesa e `+2` no Teste de Resistência Físico, pela peça 19 §5 — **desde que o atacante esteja também adjacente a você, ou esteja à distância.**

> **Nível 19.** Quando você puxa um golpe com o `Encarar`, **role `2d10−1`. O resultado, mais a sua Constituição, é reduzido do dano.** *O golpe acerta de qualquer jeito:* **isto não é uma defesa, é o quanto você aparou.**

> **Nível 27.** Sobe para **quatro tipos**, trocados a cada **descanso curto**. E a área **fica de pé enquanto você estiver caído, agarrado ou apagado**.

### O livro-caixa da Trilha

| nível | entrega | fatia |
|---|---|---|
| `2` | duas resistências, dentro do `Encarar` | `1,33` |
| `11` | cobertura `Parcial`, adjacente, com portão | `0,93` |
| `19` | `2d10−1` `+` Constituição como redução no golpe puxado | `1,80` |
| `27` | quatro tipos `+` a área te sobrevive | `1,33` |
| **total** | | **`5,39`** de `5,00` |

**Faixa honesta: `4,79` a `6,46`, e a largura inteira é o `11`.** *As outras três são números fechados.*

### O que cada preço tem atrás dele

**A fusão do `Alicerce` no `Encarar` saiu de graça, e isso é um aviso.** *`2` tipos × `3,39` = `6,78` de dano evitado = `1,33` fatia, que é exatamente o preço publicado do `Alicerce`.* **Então o `"deslocamento pela metade"` nunca foi preçado — ele valia `0,00`.** *Tirar o custo de movimento não custa nada no papel e é ganho real na mesa, mesma forma do alcance da aura.* ⚠ **E era a única coisa que fazia o nome `Muro` ser verdade.**

**O `19` é a melhor peça das duas listas**, e ela só existe por causa desta reforma: *rolar o `Bloquear` num golpe que **não dava** para bloquear só faz sentido porque o `Encarar` transfere sem rolagem.* **Não dá para copiar para outro sistema.**

*Ele custa `1,80` porque a média do `2d10−1` sem condicional é `10,00`, e não os `7,00` do `Aparar com Corpo`* — **lá a condicional de ter falhado já desconta `30%`; aqui não existe falha para descontar.**

**O portão do `11` é do Mizuki e é o que separa `0,33` de `2,67`.** *Sem ele, um inimigo corpo a corpo dá cobertura ao aliado só por estar do outro lado.* **Com ele, você tem de estar entre — vira posicionamento de verdade, e a entrega cai de aura para corpo, que é mais `Muro`.**

> ⚠ **A cobertura não tem preço no projeto**, por decisão da `v0.94` — *"cobertura não tem preço neste sistema"*. **O `0,93` é derivado do câmbio de Defesa da peça 5 (`+1` de Defesa = `3,39`), não da peça 19.** *E o `+2` no Teste de Resistência Físico entra de graça, porque conversão de TR nunca foi fechada — o `DESENHO-manhas` marca três Manhas com `"o TR não está no preço"`.*

### O estouro combinado, e por que ele foi aceito

**Um Bastião de `Muro` carrega `10,59` a `10,97` onde a régua prevê `10,00`** — de `6%` a `10%`.

***Decisão do Mizuki:*** *tanque tancando bem não é o perigo, porque existe como lidar com tanque; dano fora da curva acaba a rodada de qualquer jeito.*

> **E isso tem respaldo medido, de antes desta conversa.** *O `DESENHO-trilhas` registra que **um grupo de `Muro` não encurta luta nenhuma — ele estica**, e que o `+38,3%` da planilha era teto e não valor, porque supunha que as fatias viram dano.* **A matriz diz que não viram: o `Muro` põe `0,00` na coluna de ação e na de alvo.**

> ⚠ **O que vale olhar no playtest não é o número, é o tédio.** *O `Muro` era a única das três Trilhas com coluna de defesa — `4,16` de `4,87`.* **Agora é quase tudo defesa, dentro de um Caminho que também virou quase tudo defesa: seis peças de mitigação e nenhuma que mude o que acontece na sala.** *A `Brasa` e o `Punho` têm botão; ele tem parede.*

### Quatro nomes em aberto

**`Alicerce` pode sobreviver no `2`** se a resistência continuar sendo uma coisa nomeada. **`Aterro`, `Escora` e `Cúpula` não servem mais** — o `11` virou cobertura, o `19` virou outra coisa, e o `27` mudou de dono.

*Lembrete do método: nome composto é permitido e abre o espaço — `Puxar Para Si`, `Ainda de Pé`, `Mão na Roda` já são assim.*

---

## Trilha `Punho` — o rider que não pede Reação nova

**Ela não quebrou com o `Encarar`**, e o motivo é limpo: *o `Muro` perdia duas entregas porque vendia redirecionamento e proteção de aliado; o `Punho` vende **empurrar e derrubar**, e o `Encarar` não toca em nenhum dos dois.* **As quatro sobreviveram; duas cresceram por escolha e não por conserto.**

> **A história que precisa ser conhecida antes de mexer:** *ela estava publicada em `6,09` e foi repreçada para `4,94` na `v0.103`.* **O estouro de `22%` não era escolha, era erro:** o `Derrubado` do nível 11 estava contado como permanente, `8,66`, quando o texto escreve **dois portões** — acertar desarmado (`75%`) e o alvo falhar o TR de Vigor (`45%`), que juntos dão `33,8%`.
>
> *E um segundo erro, mais instrutivo:* **o `Engate` publicava `1,13`, que é `11,50 × 0,50`, quando o certo é `11,50 × 0,75 = 8,63`.** ***Dado grande demais vezes gatilho pequeno demais dá um número que parece bom*** — é assim que uma conta errada sobrevive a uma revisão.
>
> **É por causa dessa repreçagem que o maior estouro aceito do projeto passou a ser a `Brasa`, em `5,03`.**

### As quatro

> **Nível 2 · `Engate`.** Quando você acerta um ataque na sua ação de atacar, você pode dar um golpe desarmado como **ação bônus**.
>
> E **quando você puxa um golpe com o `Encarar`**, você pode dar um golpe desarmado em quem atacou, **se ele estiver ao seu alcance**.

> **Nível 11 · `Encontrão`.** Quando você acerta desarmado, o alvo é empurrado até **`4,5 m`** na direção que você escolher — **uma vez por alvo, por rodada**.
>
> E `1×` por rodada, um alvo que você acertou faz um Teste de Resistência de Vigor; falhando, fica `Derrubado`.

> **Nível 19 · [sem nome].** **`1×` por rodada.** Quando você tem **sucesso** num `Bloquear`, gaste **`2` PE** e dê um golpe desarmado contra quem atacou, como **Ação Livre**, se ele estiver ao seu alcance.

> **Nível 27 · [sem nome].** **Ação Padrão.** Dê um golpe desarmado contra até **a sua Força** criaturas dentro da área do `Encarar`, um em cada, com rolagem própria.
>
> Conta como **Ação de Atacar** para todos os efeitos, mas **não permite o ataque extra do nível 7**.
>
> Gastando **`8` PE**, o `Encontrão` dispara em **cada** alvo que você acertar, em vez de uma vez só — cada um faz o próprio Teste de Resistência de Vigor. ***O empurrão sai em todos de qualquer jeito, sem PE: o que os `8` PE compram é só o `Derrubado`.***

### O livro-caixa

| nível | entrega | fatia |
|---|---|---|
| `2` | `Engate` `+` soco na Reação | `2,35` |
| `11` | `Encontrão`, `4,5 m` uma vez por alvo | `0,91` |
| `19` | soco em bloqueio bem-sucedido, `2` PE | `0,51` |
| `27` | soco múltiplo `+` botão de `8` PE | `0,68`–`1,35` |
| **total** | | **`4,45`–`5,12`** de `5,00` |

**É a única das três listas que não estoura na leitura central.** *O Caminho estoura `0,20` a `0,58`, o `Muro` estoura `0,40`, e aqui sobra entre `0,55` e falta `0,12`.*

### Por que cada preço é o que é

**O soco na Reação (`+0,65`) não pede Reação nova — ele pendura valor na Reação que o Caminho já gasta.** *É a estrutura do Champion do Pathfinder, e é a única forma de rider que não briga com o `Encarar`.* ⚠ **Cláusula obrigatória nos níveis 2 e 19: `"se ele estiver ao seu alcance"`** — quem atacou o aliado pode estar a `18 m`, e sem isso o soco vira teletransporte.

**O `27` se autobalanceia sem teto escrito.** *Com `1` ou `2` alvos ele é **pior** que a Ação de Atacar normal, porque você abre mão do ataque extra do nível 7 — o jogador simplesmente não usa.* **O ganho só existe de `3` alvos para cima, então contra chefe sozinho, que é onde capstone quebra jogo, ele vale zero.**

**O botão de `8` PE é caro de sentir e barato de preçar**, que é o melhor tipo: *com `6` alvos são `3` acertos esperados, e o `Derrubado` sai de `0,45` para `0,68` queda* — **meio alvo a mais no chão por uso, porque os `45%` do TR de Vigor comem quase tudo.**

> ⚠ **O empurrão do `4,5 m` não sai como o Mizuki esperava.** *Ele cortou o encadeamento em um alvo — três acertos empurravam `9 m`, agora é um empurrão de `4,5 m`.* **Mas no `27` cada alvo já levava um soco só, então o teto não morde lá e os `4,5 m` sobem o empurrão em `50%`: de `1,06` para `1,59` fatia por uso.** *Decisão registrada de olhos abertos; e esse `1,59` não entra em conta nenhuma, porque posicionamento não tem conversão.*

**E o `Derrubado` por alvo foi recusado.** *Ele levava o `Encontrão` de `0,91` para `1,95` em rodada normal e `3,10` numa rodada de `27`, e a Trilha para `5,38`–`6,32`* — **maior que o estouro publicado que já foi derrubado uma vez, pelo mesmo motivo.** *Virou o botão de PE do `27`, que compra a mesma coisa só onde ela importa.*

### O laço com o Caminho

**Você espalha soco dentro da área, empurra todo mundo para fora, e o nível 23 só reprovoca quem entra por vontade própria.** *Eles têm de voltar andando — e aí são provocados de novo.*

**E o `Punho` é o único lugar do Bastião que gasta PE.** *O Caminho novo não gasta nenhum: `Encarar` `0`, `Aparar com Corpo` `0`, nível 23 `0`, `Passa Pra Mim` `0`* — **a porta de PE saiu junto com a `Interposição` velha e ninguém pôs nada no lugar.** *O `19` e o `27` fazem um recurso parado voltar a existir.*

> ⚠ **O câmbio de `1` PE `= 5,14` de dano não vale para este Caminho.** *Ele supõe PE competindo com alguma coisa, e o Bastião tem o menor pool do sistema justamente porque não era para gastar.* **PE parado tem custo de oportunidade perto de zero.** *Foi por isso que os `2` PE do `19` e os `8` do `27` passam, mesmo com o câmbio dizendo que são prejuízo.*

---

## Trilha `Brasa` — refeita, e ela vinha com uma conta errada embutida

**Ela não quebrou com o `Encarar`** — não vende redirecionamento, proteção de aliado nem empurrão. *Já estava estourada por outro motivo, e o Mizuki já tinha batido esse martelo na `v0.81`:* **`7,06` a `9,42` de `5,00`, com a frase *"você tá inflando demais essa habilidade, garanto para você, pode passar"*.**

> ### ⚠ O achado que muda um número publicado
>
> **O projeto conta o golpe simples a `50%` de acerto e o Classe 0 CHEIO.** *`11,50 × 0,50 = 5,75` de um lado; `27,00` sem desconto nenhum do outro.*
>
> ***Decisão do Mizuki, nesta conversa: Classe 0 resolve por rolagem de acerto.*** *Para virar Teste de Resistência ele precisaria da Melhoria de TR, que é **Média** — e um Classe 0 não tem orçamento para pagar.*
>
> **Então o mesmo desconto vale, e o `Fagulha` publicado em `4,08` deveria ser `~2,04`.** *Metade do estouro histórico da `Brasa` é conta errada, e não a decisão da `v0.81`.* **Isso precisa de uma passada separada na peça, porque toca material publicado.**

**A constante que manda nesta Trilha:** *um Classe 0 causa `27` no nível 30, custa `0` PE e não gasta ação.* **"Ganha um Classe 0 toda rodada" vale `5,31` fatias, e uma Trilha inteira tem `5,00`.**

**E a escala de Classe saiu do `bf2.py`**, busca exaustiva de todos os perfis legais: **`18` por Classe**, de `18` no Classe 1 a `126` no Classe 7. *Eu tinha estimado Classe 3 em `40` por interpolação; o real é `54`, e isso era um fator de `1,35×` escondido.*

### As quatro

> **Nível 2.** Quando você puxa um golpe com o `Encarar`, você pode lançar um feitiço de **Classe 0** contra quem atacou. E o seu **PE máximo** sobe em **Força**.

> **Nível 11.** Ao **critar** num ataque da sua Ação de Atacar, ou ao **passar** num Teste de Resistência Físico, você recebe a sua **maestria em PE temporário**. *Não acumulativo.*

> **Nível 19.** Ao ter **sucesso** num `Bloquear`, o seu próximo feitiço de **Classe acima de `0`** é rolado com **vantagem**, ou o alvo faz o Teste de Resistência dele com **desvantagem**. *O Classe 0 não consome a carga.*

> **Nível 27.** Enquanto estiver com **metade da vida ou menos**, a sua **Ação de Atacar** passa a vir acompanhada de um feitiço de **metade da sua maior Classe**, desde que seja de dano e que você cumpra os requisitos dele.

### O livro-caixa

| nível | entrega | fatia |
|---|---|---|
| `2` | Classe 0 no redirect `+` `Força` no PE máximo | `2,10` |
| `11` | maestria em PE temporário | `1,18` |
| `19` | vantagem no próximo feitiço de Classe `> 0` | `1,73` |
| `27` | Classe 3 abaixo da metade da vida | **`0,50`** |
| **total** | | **`5,51`** de `5,00` |

> ⚠⚠ ***O `0,50` do nível 27 é número do Mizuki, não medido.*** **O medido é `0,32` a `5,42`, com centro em `3,83`** — e a largura inteira é real, não é imprecisão de conta.
>
> **Por que ele oscila tanto:** *o gatilho é um **limiar**, e o limiar cai perto da borda do intervalo.* No caso base o Bastião cruza a metade da vida na rodada `2,88` de `3,5`, o `Ainda de Pé` do nível 7 cura `19,5` e empurra para `3,41`, **e sobram `0,09` rodada abaixo — `3%` da luta.** *Com `+25%` de dano recebido, o tempo abaixo é multiplicado por **catorze**.*
>
> | dano recebido/rodada | cruza em | com a cura | % da luta abaixo |
> |---|---|---|---|
> | `36,5` — só o golpe puxado | `2,88` | `3,41` | `3%` |
> | `54,8` | `1,92` | `2,27` | `35%` |
> | `73,0` | `1,44` | `1,71` | `51%` |
>
> **O `0,50` corresponde à leitura de que o Bastião quase não fica abaixo da metade**, que é o caso base *sem nenhum ataque mirado nele além do que ele puxa. O `Provocar` do nível 2 existe para trazer exatamente esses ataques.* **É a terceira vez nesta reforma que a mesma discordância de frequência aparece** — as outras duas são o `Aparar com Corpo` e o `19` do `Punho`. *Uma linha de playtest resolve as três de uma vez.*

**Os três primeiros degraus somam `5,01`** — a Trilha inteira cabendo em `5,00` pela primeira vez na história desta peça. *Todo o estouro mora no `27`.*

### O que foi recusado, e por quê

**Vantagem no Classe 0 do nível 2** (`+1,52`): tirada pelo Mizuki. **Ganhar PE por uso** em vez de subir o PE máximo (`3,47` contra `0,58`): virou aumento de pool, que é `6` PE por dia e não `6` por uso.

**O `11` dizia "acertar" e era para ser "critar".** *Com acerto custava `4,05`; com crítico custa `1,18`* — **crítico é `5%` em dois ataques, e o que manda no preço passou a ser a frequência de Teste de Resistência Físico, que ninguém mediu.**

**O `27` na Ação Bônus pagando `9` PE foi descartado:** *`54` de dano por `46` de dano largado é margem de `17%`, e ainda gasta a ação bônus.* **Na régua, o jogador que fizer a conta nunca aperta.**

## O que falta, nesta ordem

1. **Onze nomes.** *Quatro no `Muro`, o `19` e o `27` do `Punho`, e os quatro da `Brasa`.* **`Engate` e `Encontrão` ficam.**
2. **A passada de correção no `Fagulha` publicado** — `4,08` deveria ser `~2,04`, porque o Classe 0 resolve por acerto e nunca levou o desconto. *Toca material publicado.*
3. **Uma linha de playtest que resolve três discordâncias de uma vez:** *quantos ataques são mirados no Bastião por rodada, e quantas vezes ele falha um `Bloquear`.* **Ela decide o `Aparar com Corpo`, o `19` do `Punho` e o `27` da `Brasa`.**
4. **A linha na peça 19** sobre o `Incapacitado` deixar de valer zero para o Bastião.
5. **Fechar a taxa de dano movido como peça** — dono, validador com teste negativo, e os seis itens da seção 7 do rascunho.
6. **Repreçar com ela** o `Ninguém Cai`, o `Escudo de Osso`, o `Puxar Para Si` e o `Segurar`.
7. **Os outros quatro Caminhos** — Vanguarda, Guia, Emanador, Evocador — e o possível 6º, "Ágil".
8. **A recalibragem do Bestiário** contra a proporção nova de `32,4%`.

## Bugs achados de caminho, que não são deste trabalho

1. ⚠ **O `conferir-nomes.py` devolve `Encaixe` como `LIVRE`.** *`Encaixe` é a Manha da Manopla, listada na peça 17 linha 118 e publicada no capítulo 8 do livro.* **É falha de triagem: a coisa que o projeto usa pra não repetir nome está deixando passar nome repetido.**
2. ⚠ **O `PROMPT-PROXIMA-CONVERSA.md` está na `v0.206`** e contradiz o `README` sobre o playtest ter começado.

---

## Método pra seguir sem reexplicar

- **Ordem pra propor mecânica nova:** sensação → gatilho → o que substitui ou compete → regra → caso padrão mais exceção → conta → teste de dominância e de bônus automático → o porquê.
- **Antes da conta, confira a COLUNA.** O `78,75` contra o `108` custou uma conclusão inteira nesta conversa.
- **Preço de reação com uso limitado:** nunca deixar magnitude e contador de usos crescerem juntos. Trava um, deixa o outro subir.
- **Gatilho antes da rolagem cobra o fator de erro; gatilho depois, não.** Foi o que separou o `Absorver` da `Interposição`.
- **Nome novo passa pelo `conferir-nomes.py`** e ainda precisa de checagem à mão de colisão de sentido, que o script não pega — e que, como o item 1 acima mostra, às vezes ele não pega nem a colisão literal.
- **Antes de medir, confira a UNIDADE.** *Contar queda evitada media o desenho só no caso em que ele deu certo; contar golpe tancado mede o trabalho.* **A conta estava certa e a unidade estava errada, e isso custou duas rodadas.**
- **Compare os dois lados na mesma base.** *O `78,75` contra o `108` custou uma conclusão inteira; o treino em `Provocar` quase custou um preço inflado em `40%`, porque eu media a entrada com treino contra um envelope sem.* **Quando um bônus é do personagem e não do degrau, ele move os dois lados e a razão não muda.**
- **Antes de pendurar um degrau numa peça de fora, leia a peça.** *O `Bloquear` é **neutro por construção** — `2d10−1`, média `10`, exatamente o `10` parado que ele substitui — e tem validador dedicado porque o preço do `Incapacitado` depende disso.* **Qualquer coisa pendurada nele cobra em outro lugar.**
- **Nome composto é permitido e abre o espaço de nomes.** *`Puxar Para Si`, `Ainda de Pé`, `Mão na Roda`, `Não Cede` já são assim.* **E a triagem não pega colisão de sentido: `Último a Cair` passou `LIVRE` empatando com o `Ninguém Cai` do Guia na frase e no gatilho.**
- **Rodadas de luta por dia = `10,5`.** É a constante que converte "quantas vezes por dia" em "dano por rodada".
