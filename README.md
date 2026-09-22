# RPG — Classes: releitura de Bastião, Vanguarda e Estocada

Este repositório guarda uma **releitura de três classes** do Projeto M, o sistema de RPG de mesa de Jujutsu Kaisen que mora em [cupcake-mochi/JJK---Project](https://github.com/cupcake-mochi/JJK---Project). O trabalho aconteceu fora do repositório principal, entre 17 e 19 de setembro de 2026, e **nada daqui foi aplicado lá**. É proposta de trabalho, com número calculado, esperando decisão.

Se você chegou aqui sem conhecer o Projeto M: a seção *"O mínimo pra ler isto"* logo abaixo dá o vocabulário. Se conhece, pule pra *"As três frentes"*.

## O mínimo pra ler isto

O Projeto M é um sistema feito pra um servidor de guilda com vários mestres e personagem que passa de mesa em mesa. Por isso o filtro que decide quase tudo é: **dois mestres que nunca conversaram chegam ao mesmo número lendo a mesma regra?** Toda regra é medida contra isso.

Alguns termos que aparecem o tempo todo:

- **Caminho** é a classe (Bastião, Vanguarda, Guia, Emanador, Evocador). **Trilha** é a subclasse, escolhida no nível 2. A Estocada é uma Trilha da Vanguarda.
- **Fatia** é a unidade de orçamento: uma fatia vale **5,08 de dano por rodada no nível 30**. Toda habilidade é convertida pra isso — dano, condição, movimento, defesa. No repositório principal, um Caminho tem orçamento de **3 fatias** (níveis 2 · 15 · 30) e uma Trilha tem **5**. **Esta releitura sobe o Caminho pra 5 fatias, em quatro degraus — 2 · 15 · 23 · 30 —, com o ataque extra do 7 de graça.** A decisão está no `bastiao-reforma/` (17/09) e foi confirmada pelo Mizuki em 21/09 pros cinco Caminhos.
- **Dano movido** é a régua nova que o Bastião precisou: *1 ponto de dano movido de um aliado pra você vale 0,30 de dano causado*. Provisória, decidida, não medida — como o 5,08.
- **PE** é ponto de energia. Feitiço, Kata e várias habilidades gastam PE. Na régua de orçamento, **1 PE vale 5,14 de dano equivalente**.
- **Maestria** é o bônus de nível: 1 nos níveis 2–9, 2 nos 10–17, 3 nos 18–25, 4 nos 26–30. Muita coisa escala por ela.
- **Manha** é o que a Escola de Arma dá: um efeito ligado à categoria de arma que você escolheu.
- **TR** é Teste de Resistência. **CD** de habilidade é sempre 8 + atributo + maestria.
- **Dia de referência**, pra toda conta: três combates de três ou quatro turnos, 10,5 rodadas no total.

## Estado: proposta, não regra

Tudo aqui é *versão de trabalho*. Os documentos dizem isso neles mesmos, repetidamente. O JJK---Project, na v0.263, ainda tem o texto antigo: Brasa, Fagulha, treze Manhas, Não Acabou, Traçado.

A revisão feita em 20/09 (pasta `revisao/`) achou cinco coisas que **bloqueavam** levar isto pro repositório principal. Em 21/09, com o zip da reforma do Bastião e a transcrição da conversa da Sequência, três delas fecharam: a régua de 5 fatias e o nível 23 estavam decididos e escritos no zip; o texto-base da Sequência existe e está em `vanguarda-sequencia-conversa-18-09.md`; e Não Pega é do Bastião, como o manual diz. O que sobra está na seção *"O que a revisão achou"*.

## As três frentes

### Bastião — o Caminho e as três Trilhas, refeitos e medidos

A primeira frente, de 17/09, e a única fechada de ponta a ponta: texto, preço e nome. Mora em duas camadas.

**`bastiao-reforma/`** é o zip que saiu da conversa de 17/09 — o documento principal, a régua nova de dano movido, um validador que reproduz cada número (`TUDO OK`) e os scripts de cada rodada. O Bastião deixou de ser um evento (uma Reação que intercepta) e virou um **estado**: Olhos Em Mim, uma área de 6 m em que você provoca quem entra e puxa pra você, com a Reação, qualquer golpe que acerte um aliado — sem nova rolagem, crítico e condição inclusos. *"Você não intercepta golpe. Você fica impossível de ignorar."* As três Trilhas viraram três respostas em cima do mesmo estado: Muro come e fica mais duro, Punho come e devolve, Combatente Amaldiçoado come e vira energia.

| Peça | Fatias | Observação |
|---|---:|---|
| Caminho | 5,20 a 5,58 | estouro declarado pelo Mizuki: *"tanque tancando bem não é o perigo"* |
| Muro | 5,39 | faixa 4,79 a 6,46, toda no Guarda-Costas |
| Punho | 3,60 a 4,27 | escala corrigida em 21/09 (com acerto); a que sobra mais espaço |
| Combatente Amaldiçoado | 5,51 | o nível 27 está em 0,50 por decisão; medido 0,32 a 5,42 |

**Os dois arquivos da raiz, de 18/09, fecham a fila do zip.** `bastiao-nomes-aprovados.md` dá os dezoito nomes (Encarar → Olhos Em Mim, Brasa → Combatente Amaldiçoado, e os onze que o zip deixou sem nome), cada um com a mecânica reescrita. `bastiao-correcao-fagulha.md` corrige o preço histórico de Fagulha de 4,08 pra **2,05**, com acerto — escala confirmada em 21/09 e estendida pra Trocação Franca em `bastiao-correcao-escala.md`. O README do `bastiao-reforma/` tem o mapa nome a nome e o que o zip decide pro sistema inteiro.

~~Uma tensão de escala ficou aberta.~~ **Fechada em 21/09: com acerto, nas três** — Fagulha 2,05, Trocação Franca 0,85 (era 1,70), Retaliação 2,10. Cru levava o Combatente Amaldiçoado a 7,03. Registro em `bastiao-correcao-escala.md`.

### Vanguarda — o Caminho reconstruído

A frente grande. O Caminho foi refeito em volta de uma mecânica nova, a **Sequência de Combate**: você *abre* com um golpe que perde Xd4 de dano, *conduz* pagando PE por tentativa (metade da maestria + 1), e *conclui* com um efeito forte — derrubar, desarmar, prender, tirar reação. Errar uma condução encerra tudo; a sequência também morre se ficar dois turnos sem retomar.

O orçamento fechou assim (em fatias, no nível 30):

| Peça | Reserva | O cenário de referência mediu |
|---|---:|---:|
| Sequência de Combate | 2,00 | 1,39 |
| Escola de Arma, reduzida a quatro Manhas ou Versado | 0,75 | 0,11 a 0,44 |
| Não Cede, regra original mantida | 1,00 | 0,82 |
| Persistência (nível 23): salvar a sequência depois de um erro | 0,25 | 0,21 |
| Conclusão Dupla (nível 30): duas conclusões num golpe | 1,00 | 0,84 |
| **Total** | **5,00** | |

Toda reserva tem margem sobre o medido, e os documentos são honestos sobre isso: *"preço provisório de trabalho, não teto demonstrado"*. Dois cenários de estresse passam de cinco (alvo com Defesa 14; luta de doze turnos) e ficaram registrados.

O caminho até aqui teve idas e voltas, e os arquivos guardam todas: primeiro custo de −2 de dano e 1 PE, depois Xd4 e maestria/2+1 PE; primeiro teto de duas conduções, depois sem teto mas erro encerra; Persistência primeiro era um uso por cena, depois virou metade da maestria pra baixo + 1 por descanso.

**O registro vigente é `vanguarda-orcamento.md`.** Os outros documentos marcam no cabeçalho se são históricos. O texto de regra das seis conduções e das sete conclusões está em `vanguarda-sequencia-conversa-18-09.md`, a conversa que as gerou; `vanguarda-sequencia-consolidada.md` junta tudo que os documentos e o código dizem sobre Abrir, Conduzir e Concluir, com a fonte de cada frase e as decisões de 21/09 (a Sequência entra no nível 2; terreno difícil conta pra Fixar; a duração escrita substitui o TR de fim de turno).

**Decidido em 21/09: o preço conta o PE gasto bruto, sem descontar.** O benefício bruto de 3,45, menos 0,32 de abertura, menos 1,75 de PE cobrado a 5,14 por ponto dava 1,39 líquido; sem descontar o PE, a mesma Sequência rende 3,13. A escolha nunca muda quanto PE a Sequência custa em mesa — só se esse gasto é subtraído do preço registrado. **A Vanguarda de distância mede 5,07 fatias no bruto adotado; o perfil corpo a corpo mede só 1,34, e essa diferença entre armas continua aberta.** Conta em `conferir-vanguarda-pe.py` / `vanguarda-pe-contas.json`, decisão registrada em `vanguarda-orcamento.md`.

**⚠ Achado de 21/09, noite: esses 5,07 e 1,34 são de uma Vanguarda que nunca conjura.** A régua do repositório principal diz que ela conjura em 7 das 10,5 rodadas no nível 30, e sem Compasso essas rodadas não têm ataque. Nessa base o Caminho mede **1,09** (distância) e **0,88** (corpo a corpo) pra Batedor e Executor, e **4,57** / **1,22** pra Estocada — a Sequência quase só existe com Compasso. Contra qual Vanguarda preçar o Caminho está pendente de decisão; o bruto não muda. Quadro em `vanguarda-completo.md`, conta em `conferir-estocada-rotina.py`.

### Estocada — quatro entregas fechadas, preço aberto

As quatro habilidades da Trilha fecharam como mecânica:

- **Compasso (nível 2)** ganha o atributo escolhido (Essência ou Inteligência) no PE máximo, além de conjurar na padrão e atacar na bônus.
- **Traçado (11) morreu** e virou seis **conclusões mágicas**: preparar a Sequência com arma e fechar com feitiço.
- **Bote (19)** mantido: feitiço de condição sem dano libera o ataque extra na bônus.
- **Ferrão (27)** agora só dispara depois de uma conclusão mágica que afete o alvo.

Mas o preço total **não** fechou, e o motivo é o achado mais importante da pasta: o preço zero antigo do Compasso se apoiava numa regra em que conjurar já dava um golpe de brinde. Desde a v0.147 do repositório principal o ataque extra exige a Ação de Atacar. Então Compasso e Bote hoje são *permissões de atacar depois de conjurar* — e isso tem preço. Só Compasso+Bote, num Refino 6, dá 4,46 fatias por rodada elegível. A Trilha não cabe em cinco sem conta nova.

**O registro vigente é `estocada-auditoria.md`.**

## Mapa dos arquivos

Os 50 arquivos da releitura ficam na raiz, com o nome dizendo a frente. Cada `conferir-*.py` tem um `*-contas.json` ao lado com a saída completa. Os marcados *21/09* saíram da sessão de revisão daquele dia; o marcado *22/09* veio da branch que tinha ficado pra trás.

| Arquivo | Frente | Estado | O que é |
|---|---|---|---|
| `bastiao-reforma/` | Bastião | **vigente**, fonte | o zip de 17/09: texto, preço e régua do Bastião inteiro; README próprio com o mapa de nomes |
| `bastiao-completo.md` | Bastião | **vigente** | o Bastião num lugar só: chassi, as cinco entregas do Caminho e as três Trilhas, com nome e preço finais |
| `bastiao-nomes-aprovados.md` | Bastião | vigente | os dezoito nomes e a mecânica de cada um |
| `bastiao-correcao-fagulha.md` | Bastião | vigente | a conta corrigida de Fagulha |
| `bastiao-correcao-escala.md` | Bastião | vigente, *21/09* | a escala com acerto estendida pra Trocação Franca e Retaliação; por que cru quebrava o Combatente Amaldiçoado |
| `conferir-fagulha.py` | Bastião | — | enumera 160 mil combinações de dado pra conferir Fagulha |
| `conferir-escala-bastiao.py` | Bastião | — | *21/09*, dano cru contra dano com acerto nas três entregas que a escala decide |
| `regua-do-caminho.md` | os cinco Caminhos | **vigente**, *22/09* | por que o Caminho vai a 5 fatias e por que o degrau é no 23 — o vão da escada, não o orçamento; mais a lista de porte com arquivo e linha |
| `vanguarda-sequencia-conversa-18-09.md` | Vanguarda | fonte, *21/09* | a conversa que gerou a Sequência: o texto-base das conduções e conclusões |
| `vanguarda-sequencia-consolidada.md` | Vanguarda | *21/09* | tudo sobre Abrir, Conduzir e Concluir, com a fonte de cada frase e as decisões de 21/09 |
| `vanguarda-orcamento.md` | Vanguarda | **vigente** | o registro das cinco fatias e das regras que sustentam o preço |
| `vanguarda-completo.md` | Vanguarda, Estocada | **vigente**, *21/09* | o Caminho e a Trilha num lugar só, com o achado da Vanguarda que conjura 7 de 10,5 |
| `vanguarda-conclusao-dupla.md` | Vanguarda | vigente | texto e conta do nível 30; regras atuais da Sequência |
| `vanguarda-nv23.md` | Vanguarda | vigente | Persistência, nível 23, versão fechada |
| `vanguarda-nao-cede.md` | Vanguarda | vigente | Não Cede mantido, reserva de 1,00 |
| `vanguarda-escolas-rascunho.md` | Vanguarda | vigente (regras); números históricos | a Escola de Arma reduzida a quatro Manhas + Versado |
| `vanguarda-precificacao-v2.md` | Vanguarda | histórico | a auditoria com os custos Xd4 e maestria/2+1 — **ainda publica o teto de duas conduções como vigente** |
| `vanguarda-precificacao-inicial.md` | Vanguarda | histórico | a primeira auditoria, com −2 de dano e 1 PE |
| `vanguarda-nv23-proposta.md` | Vanguarda | histórico | Persistência quando era um uso por cena |
| `conferir-vanguarda.py` · `-v2.py` · `-v3.py` | Vanguarda | — | as três gerações do modelo; **a v3 importa a v2** e roda regressão contra ela |
| `conferir-escolas-vanguarda.py` | Vanguarda | — | acréscimo marginal de cada Manha |
| `conferir-nao-cede.py` | Vanguarda | — | sensibilidade de Não Cede |
| `conferir-vanguarda-pe.py` | Vanguarda | — | *21/09*, o preço líquido contra o bruto nos dois perfis de arma |
| `conferir-vanguarda-nv23.py` · `-nv23-usos.py` | Vanguarda | — | Persistência com um uso por cena, e depois com contador por maestria |
| `estocada-auditoria.md` | Estocada | **vigente** | por que o preço total não fecha, e o que falta |
| `estocada-compasso.md` | Estocada | vigente | Compasso com atributo no PE |
| `excecao-atributo-no-pe.md` | Estocada, Bastião | vigente, *21/09* | exceção declarada contra a peça 1, pra Compasso e Retaliação |
| `estocada-conclusoes-feiticos.md` | Estocada | vigente | as seis conclusões mágicas |
| `estocada-bote.md` · `estocada-ferrao.md` | Estocada | vigente | níveis 19 e 27 |
| `conferir-estocada-auditoria.py` | Estocada | — | Ferrão e Compasso+Bote por enumeração de estados |
| `conferir-estocada-compasso-pe.py` | Estocada | — | só a parcela de PE do Compasso |
| `conferir-estocada-conclusoes-magicas.py` | Estocada | — | *21/09*, preço das seis conclusões mágicas do nível 11 |
| `conferir-estocada-rotina.py` | Vanguarda, Estocada | — | *21/09*, o Caminho e a Estocada numa Vanguarda que conjura 7 de 10,5 rodadas; duas implementações que têm de concordar |
| `vanguarda-nao-acabou-comparacao.json` | Vanguarda | histórico | comparação da antiga Não Acabou, sem script próprio |

## Rodar os scripts

Python 3, sem dependência externa. Rode da raiz:

```bash
for v in conferir-*.py; do python3 "$v"; done
```

Cada um imprime a tabela dele e termina com uma linha de checagem (`OK` ou uma afirmação do que foi conferido). Os **quatorze** rodam limpos e reproduzem cada número dos documentos — conferido em 22/09/2026, junto do `conferir-dano-movido.py` e dos 22 scripts de conta do `bastiao-reforma/`. Não há validador de regressão entre os `.md` e os scripts; os números dos documentos foram copiados da saída à mão.

Os três scripts de `revisao/` rodam de dentro da própria pasta e não entram nesse laço — `nivel-2.py`, `vao-do-nivel-23.py` e `orcamento-3-ou-5.py`. Os dois últimos leem os `*-contas.json` da raiz por caminho relativo.

`conferir-vanguarda-v3.py` carrega `conferir-vanguarda-v2.py` por caminho relativo; os dois precisam estar na mesma pasta. O mesmo vale pros de nível 23 e de Escolas, que carregam a v3.

## O que a revisão achou

Em 20/09/2026 dois agentes revisaram a pasta contra o repositório principal na v0.261. Os relatórios completos estão em `revisao/`; os achados mais importantes foram conferidos à mão depois. Eram cinco bloqueios; o estado em 21/09:

1. ~~O Caminho tem 3 fatias no repositório, não 5, e não tem nível 23.~~ **Resolvido:** a decisão estava no zip do Bastião — 5 fatias, quatro degraus em 2 · 15 · 23 · 30 — e o Mizuki confirmou que vale pros cinco Caminhos. **O motivo está em `regua-do-caminho.md`**, e não é o orçamento: é o vão da escada, que foi de 5 pra 8 níveis quando o degrau do 23 saiu na v0.70. Esse arquivo também avisa que a mudança **reverte uma decisão registrada** do repositório principal (*"o vão fica, e é preço aceito e não defeito"*), e traz a lista de porte com arquivo e linha — cinco donos mais dois que só descrevem.
2. ~~O texto das conduções e conclusões não está em arquivo nenhum.~~ **Resolvido:** está em `vanguarda-sequencia-conversa-18-09.md`. Três regras daquela conversa morreram em 19/09 (erro conserva prazo; teto de duas; prazo de um turno) e o consolidado marca quais.
3. ~~Compasso somando atributo no PE máximo contraria uma regra que tem motivo escrito na peça 1.~~ **Resolvido em 21/09: exceção declarada**, cobrindo também a Retaliação do Bastião, que faz a mesma coisa (`excecao-atributo-no-pe.md`).
4. ~~O alvo morre no meio da Sequência.~~ **Resolvido pelo texto-base:** *"abrir uma sequência contra outro alvo substitui a anterior"*. Falta só deixar explícito no texto de regra.
5. ~~Não Pega: peça 6 diz Vanguarda, manual diz Bastião.~~ **Resolvido a favor do manual:** o zip põe Não Pega no nível 7 do Bastião, de graça, junto de Ainda de Pé. A peça 6 §3.1 envelhece no porte.

E o que vale corrigir antes: ~~a escala de Fagulha (achado 12, agora com a tensão interna do zip somada)~~ — **resolvido em 21/09, com acerto pras três** (`bastiao-correcao-escala.md`); Conclusão Dupla "por cena" deveria ser "por descanso curto" pela regra do próprio repositório; no nível 2 a Sequência perde dinheiro em toda rota (conta em `revisao/nivel-2.py`) — e o Mizuki pôs a Sequência no nível 2; Desorientar domina as outras conclusões mágicas; a v2 ainda publica regra velha sem aviso.

~~Na triagem de nomes, cinco morreram no validador do repositório (Condução, Conduzir, Precisão, Guarda, Impacto) e seis precisam de outro nome por sentido (Abrir/Abertura, Fechar a Rota, Golpe de Impacto, Derrubada, Desvio, Abrir Caminho).~~ **Fechado em 21/09**, ver `vanguarda-sequencia-consolidada.md` §12: Sequência de Condução, Ritmo, Postura Firme, Empuxo, Mover Alvo, Ponto Fraco, Rasteira, Romper Fileira. Fechar a Rota e as duas "Resposta" ficam mantidos por decisão. Só falta a etapa 1 (Abrir/Abertura). Os dezoito do Bastião passaram limpos.

`revisao/cruzamento-constantes.md` confere as 30 constantes que os scripts usam contra o documento dono: 26 batem com citação literal.

## O que está aberto

Decisões do Mizuki, primeiro — nenhuma é conta:

1. ~~A fatia cobra PE ou não?~~ **Resolvido em 21/09: conta bruto, sem descontar.** A Vanguarda de distância mede 5,07 fatias; o perfil corpo a corpo mede 1,34, e essa diferença entre armas fica como pendência separada (ver a seção da Vanguarda).
2. ~~A escala: dano cru ou com acerto?~~ **Resolvido em 21/09: com acerto.** Fagulha 2,05, Trocação Franca 0,85 (caiu de 1,70), Retaliação 2,10 sem mudar. Critério: cru fazia o Combatente Amaldiçoado passar de 7,00 fatias.
3. ~~Persistência precisa de nível.~~ **Já estava escrito, só disperso.** Sequência + Escola no 2 (2,75), Não Cede no 15 (1,00, já dito em `vanguarda-nao-cede.md`: "na progressão antiga, a habilidade entra no nível 15"), Persistência no 23 (0,25), Conclusão Dupla no 30 (1,00). Soma 5,00 exato, sem margem.
4. ~~Nomes da Vanguarda.~~ **Fechado em 21/09**, oito de nove trocas decididas (`vanguarda-sequencia-consolidada.md` §12). Falta só o nome da etapa 1 (Abrir/Abertura).
5. ~~Compasso com atributo no PE contra a peça 1.~~ **Resolvido em 21/09: exceção declarada**, ideia do próprio Mizuki — o bônus não é fixo, cresce junto do atributo pelas aptidões da peça 11.

Depois, trabalho:

6. Escrever o `RASCUNHO-sequencia-de-combate.md` — texto de regra, com as mudanças de 19/09 e as respostas de 21/09 por cima da conversa.
7. Preço total da Estocada, e as duplas mágicas da Conclusão Dupla. **Medido em 21/09** (`conferir-estocada-rotina.py`; uma primeira versão da mesma tarde, que dizia "Compasso nunca vence a arma pura", estava errada e foi desfeita). Numa Vanguarda que conjura 7 de 10,5 rodadas: Compasso 5,35 (distância) / 2,13 (corpo a corpo); conclusões mágicas e Ferrão 0,00, porque o ataque de bônus já conclui de arma por mais; Bote até 3,43 / 2,05. A Trilha mede 5,35 a 8,78 no perfil de distância. Depende da decisão sobre a Vanguarda de referência (ver a seção da Vanguarda). As seis conclusões mágicas do nível 11 já fecharam (Cortar a Resposta 0,34, Desorientar 0,62). Pendência aberta: sincronizar Interromper a Resposta (arma) com a janela estreitada de Cortar a Resposta.
8. A fila do próprio zip do Bastião: a linha de playtest, a linha na peça 19, fechar a régua de dano movido como peça, repreçar as quatro entregas que dependem dela.
9. Levar pro JJK---Project, seguindo o procedimento de lá (validadores, CHANGELOG, mensagem de commit). Toca o `DESENHO-caminhos.md`, a peça 6 §3.1, a peça 19 e o manual.

E duas pontas pequenas que apareceram ao conferir a pasta em 22/09, as duas do mesmo tipo — número sem dono declarado:

10. **A Escola de Arma tem dois números publicados que discordam.** A reserva na tabela da Vanguarda diz *"0,11 a 0,44"*, que sai do `conferir-escolas-vanguarda.py` — Precisão 0,1095 e Versado 0,4445 no cenário de referência. O `revisao/orcamento-3-ou-5.py` mede o Versado em **0,5149**, de 1,7770 − 1,2621, e o 1,7770 está publicado em `vanguarda-conclusao-dupla.md` linha 75. Os dois cabem na reserva de 0,75, então nada quebra — mas são dois modelos discordando em 0,07 sem ninguém dizer qual é o dono.
11. **Dois valores moram dentro de um validador.** A linha 278 do `conferir-estocada-rotina.py` traz `1.2621357356808118` e `3.0101` escritos à mão. Os donos deles são `perfis/distancia/etapas/sequencia/acumulado/{L,Br}` no `vanguarda-pe-contas.json` — inflar os dois no JSON em 10% **não acende** a checagem. O resto do script lê do dono direito: perturbar o 5,07, o 1,34, o Não Cede, o PE por nível, a maior Classe, o nível ou o custo do feitiço faz ele falhar como devia.

## As outras pastas

- **`bastiao-reforma/`** — a fonte do Bastião: o zip de 17/09, com README de reconciliação contra os arquivos de 18/09 da raiz.
- **`referencia-jjk-project/`** — cópia somente-leitura de 22 arquivos do JJK---Project na v0.263, os que os documentos daqui citam como fonte. Tem um README próprio dizendo o que é cada um e por que está lá. Se discordar do repositório principal, o principal vence.
- **`revisao/`** — os dois relatórios de 20/09 e três scripts: o `nivel-2.py`, mais o `vao-do-nivel-23.py` e o `orcamento-3-ou-5.py`, que vieram junto do `regua-do-caminho.md`. Não fazem parte da releitura; são revisão dela. Os achados 1, 2, 4 e 5 fecharam em 21/09; os relatórios não foram editados, o estado está acima.

## Histórico deste repositório

Cinco commits, de propósito:

1. A pasta exatamente como foi entregue em 20/09/2026, mais um `.gitignore`.
2. Só a troca dos links: os documentos apontavam uns pros outros e pro repositório principal por caminho absoluto de uma máquina; viraram links relativos. Nenhuma palavra de texto mudou — o `git diff` desse commit só tem linhas com link.
3. Este README, a pasta de referência e a pasta de revisão.
4. O `bastiao-reforma/`, a conversa e o consolidado da Sequência, e as decisões de 21/09 refletidas neste README.
5. A noite de 21/09 — a decisão de PE bruto, a escala com acerto, a exceção de atributo, os dois consolidados e o achado da Vanguarda que conjura — mais o `regua-do-caminho.md` e os dois scripts que vieram com ele.

O quinto junta duas pontas. Uma é a noite de 21/09, que ficou fora do git por um dia. A outra é a branch **`claude/jjk-classes-review-g21rh1`**, que saiu do commit 3 às 19:53 daquele dia, fechou o mesmo item 1 por outro caminho e nunca voltou. Ela não foi mesclada — mesclar apagaria o `bastiao-reforma/` e a conversa da Sequência, que entraram depois que ela saiu. Os três arquivos dela que o `main` não tinha foram trazidos à mão, e o `regua-do-caminho.md` abre com o aviso do que envelheceu no texto dele.

## Licença e escopo

Mesmo escopo do JJK---Project: material de fã, sem fins comerciais, não afiliado à Shueisha, à MAPPA nem a Gege Akutami. Jujutsu Kaisen e seus personagens pertencem aos detentores originais.
