# RASCUNHO — a taxa de dano movido

*Este arquivo substitui o `RASCUNHO-corpo-de-pe.md`. **A conclusão mudou de forma no meio do trabalho**, e o nome velho descrevia a hipótese, não o resultado.*

> **A hipótese era construir uma segunda moeda, ao lado da fatia, pra medir sobrevivência.**
> **O resultado é que não precisa de moeda nova. Precisa de uma constante.**

---

## 1. O problema, que continua o mesmo

**Dano evitado conta `1` pra `1` com dano causado, e é por isso que redução, resistência e PV temporário têm preço.** *Mover dano de uma pessoa pra outra não evita nada — o grupo perde a mesma vida.* **O que muda é quem perde, e a régua de dano é cega pra isso.**

O mesmo buraco já tinha engolido o `Ninguém Cai` do Guia, o `Escudo de Osso` do Evocador e a Trilha `Muro` inteira. A reforma do Bastião só foi a primeira peça que não consegue existir sem ele.

---

## 2. A rota longa, e por que ela foi abandonada

A primeira tentativa modelou a luta inteira e mediu **quedas evitadas**: quatro pessoas contra o `Desastre` do nível 30, chefe concentrando no mais frágil, com atrito.

| puxa por rodada | rodadas | quem cai |
|---|---|---|
| `0` | `4,45` | três |
| `1` | `3,60` | duas |
| **`2`** | **`3,05`** | **uma** |
| `3` | `3,45` | duas — e uma é o Bastião |

**O modelo é bom e a regressão dele fecha:** sem ajuda nenhuma ele derruba `3` de `4` em `4,45` rodadas, e a peça 26 §4.2 publica, por outra rota, `2,70` pessoas derrubadas concentrando e os quatro em cinco rodadas.

**Mas a unidade estava errada.** *Contar queda evitada mede o desenho no caso em que ele deu certo, e não o trabalho que ele faz.* **Um Bastião que tanca a luta inteira sem que ninguém fosse cair mesmo assim fez o trabalho, e a unidade "queda" marcava zero.**

> ⚠ ***Decisão do Mizuki: parar de contar por queda.*** *Conte o trabalho direto — quantos golpes ele toma no lugar dos outros.*

**O modelo de luta não vira lixo.** *Ele continua sendo o que valida se a taxa produz um jogo que funciona, e é ele que mostrou que puxar `3` por rodada derruba o próprio Bastião.* **O que ele deixou de ser é a fonte do preço.**

---

## 3. A rota curta, que é a que ficou

**A unidade é o ponto de dano movido.** Um golpe que ia num aliado e foi pra você.

O caso de referência, escolhido pelo Mizuki: **o Bastião toma `2` golpes numa luta de `3` rodadas**, e o dia tem `3` lutas.

| nível | golpe do `Desastre` | por luta | por dia | por rodada do dia | % da vida dele por luta |
|---|---|---|---|---|---|
| `10` | `25` | `50` | `150` | `14,29` | `36%` |
| `20` | `49` | `98` | `294` | `28,00` | `35%` |
| `30` | `73` | `146` | `438` | `41,71` | `35%` |

E aí o preço em fatia depende de **um número só**:

> ## `1` ponto de dano movido `=` `0,30` ponto de dano causado

***Provisória, decidida, não medida*** — do mesmo jeito que o `5,08` da fatia e o `5,00` de orçamento por Caminho foram decididos.

---

## 4. Por que `0,30` e não outra coisa

**Duas rotas independentes caem quase no mesmo lugar**, que é o mesmo tipo de convergência que deu confiança no modelo de luta:

**Pela ponta do orçamento.** Se o nível 2 do Bastião deve custar metade do Caminho, porque **ele carrega treze níveis sozinho** antes do próximo degrau, a taxa que faz isso é `0,304`.

**Pela ponta da leitura.** `0,30` tem tradução em português: *um ponto de dano movido vale quase um terço de um ponto de dano causado.* Número redondo que dá pra explicar na mesa sem abrir planilha.

E o que as outras taxas comprariam, pra deixar registrado o que foi recusado:

| taxa | o nível 2 custa | o que isso quer dizer |
|---|---|---|
| `1,00` | `8,21` | dano movido igual a PV temporário — **impossível, passa o Caminho inteiro** |
| `0,43` | `3,52` | a razão entre as barras, `1 − 120/210` |
| **`0,30`** | **`2,46`** | **o escolhido** |
| `0,15` | `1,23` | degrau parelho com os outros três |

---

## 5. A taxa é plana, e isso é o achado que a fecha

Fixando em `0,30` e medindo contra a `Rotina` de cada faixa:

| nível | move por rodada | vale em dano | % da `Rotina` da faixa |
|---|---|---|---|
| `10` | `14,29` | `4,29` | `9,5%` |
| `20` | `28,00` | `8,40` | `11,1%` |
| `30` | `41,71` | `12,51` | `11,6%` |

**`9,5` · `11,1` · `11,6`.** *A mesma taxa serve os três níveis publicados.*

> **Então ela entra como constante e não como tabela.** *Sem faixa, sem exceção, sem "a partir do nível tal".* **É uma linha ao lado do `5,08`, e não uma peça nova.**

---

## 6. O que a taxa preça de imediato

Ela não nasceu pro Bastião. **Tudo isto estava sem preço pelo mesmo motivo e passa a ter:**

- o `Ninguém Cai` do Guia, nível 30
- o `Escudo de Osso` do Evocador, nível 15 — que é a `Interposição` com o corpo da invocação
- PV temporário em geral
- a Trilha `Muro` inteira
- o `Puxar Para Si` e o `Segurar` do Bastião velho, que **nunca foram medidos** em versão nenhuma do projeto

---

## 7. O que ela ainda não vê

**Nenhum destes derruba a taxa, mas todos mexem no caso de referência dos `2` golpes por luta.**

1. **O `2` por luta é escolha, não medição.** Saiu de julgamento de mesa. O modelo de luta da seção 2 sugere que `1` por rodada — `3` por luta — é o que o corpo aguenta, então `2` é conservador. **Vale conferir contra playtest antes de virar definitivo.**
2. **Ninguém cura e ninguém levanta ninguém** nos modelos rodados. A peça 26 §4.7 tem quatro composições medidas, três delas curando.
3. **O `Ainda de Pé` do nível 7 não entra**, e ele existe em toda ficha de Bastião dali pra frente.
4. **`Sequela` e `Cicatriz` não entram** — são o custo que sobrevive à luta, e a taxa está subestimando por isso.
5. **Um chefe só.** `Capanga`, `Ameaça`, `Catástrofe` e `Calamidade` têm número de ações diferente, e o número de ações decide quanto dá pra puxar.
6. **Dois modelos de luta no projeto.** A peça 26 roda **sem** atrito por decisão da `v0.205`; esta conta roda **com**. *O projeto precisa declarar qual manda em quê.*

---

## 8. Pra fechar isto como peça

- [ ] dono declarado da constante, e onde ela mora
- [ ] validador com **teste negativo** — uma montagem que a taxa tem de reprovar
- [ ] rodar os seis itens da seção 7
- [ ] repreçar `Ninguém Cai`, `Escudo de Osso`, `Puxar Para Si` e `Segurar` com ela, que é o que justifica ela existir
- [ ] decidir qual modelo de luta manda: com atrito ou sem
