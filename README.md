# RPG — Classes: releitura de Bastião, Vanguarda e Estocada

Este repositório guarda uma **releitura de três classes** do Projeto M, o sistema de RPG de mesa de Jujutsu Kaisen que mora em [cupcake-mochi/JJK---Project](https://github.com/cupcake-mochi/JJK---Project). O trabalho aconteceu fora do repositório principal, nos dias 18 e 19 de setembro de 2026, e **nada daqui foi aplicado lá**. É proposta de trabalho, com número calculado, esperando decisão.

Se você chegou aqui sem conhecer o Projeto M: a seção *"O mínimo pra ler isto"* logo abaixo dá o vocabulário. Se conhece, pule pra *"As três frentes"*.

## O mínimo pra ler isto

O Projeto M é um sistema feito pra um servidor de guilda com vários mestres e personagem que passa de mesa em mesa. Por isso o filtro que decide quase tudo é: **dois mestres que nunca conversaram chegam ao mesmo número lendo a mesma regra?** Toda regra é medida contra isso.

Alguns termos que aparecem o tempo todo:

- **Caminho** é a classe (Bastião, Vanguarda, Guia, Emanador, Evocador). **Trilha** é a subclasse, escolhida no nível 2. A Estocada é uma Trilha da Vanguarda.
- **Fatia** é a unidade de orçamento: uma fatia vale **5,08 de dano por rodada no nível 30**. Toda habilidade é convertida pra isso — dano, condição, movimento, defesa. No repositório principal, um Caminho tem orçamento de **3 fatias** e uma Trilha tem **5**.
- **PE** é ponto de energia. Feitiço, Kata e várias habilidades gastam PE. Na régua de orçamento, **1 PE vale 5,14 de dano equivalente**.
- **Maestria** é o bônus de nível: 1 nos níveis 2–9, 2 nos 10–17, 3 nos 18–25, 4 nos 26–30. Muita coisa escala por ela.
- **Manha** é o que a Escola de Arma dá: um efeito ligado à categoria de arma que você escolheu.
- **TR** é Teste de Resistência. **CD** de habilidade é sempre 8 + atributo + maestria.
- **Dia de referência**, pra toda conta: três combates de três ou quatro turnos, 10,5 rodadas no total.

## Estado: proposta, não regra

Tudo aqui é *versão de trabalho*. Os documentos dizem isso neles mesmos, repetidamente. O JJK---Project, na v0.263, ainda tem o texto antigo: Brasa, Fagulha, treze Manhas, Não Acabou, Traçado.

E a revisão feita em 20/09 (pasta `revisao/`) achou coisa que **bloqueia** levar isto pro repositório principal do jeito que está. O mais grave: a releitura da Vanguarda distribui **5 fatias** e cria um **nível 23**, mas o repositório principal dá **3 fatias** ao Caminho e não tem degrau no 23. Se a conversa que gerou isto decidiu mudar a régua, a decisão não ficou escrita. Detalhe na seção *"O que a revisão achou"*.

## As três frentes

### Bastião — só nomes e uma conta

A menor das três. Dois arquivos.

- **`bastiao-nomes-aprovados.md`** — a rodada de nomes fechou. A Trilha *Brasa* virou **Combatente Amaldiçoado**; a habilidade central *Encarar* virou **Olhos Em Mim**; dezoito nomes no total, cada um com a mecânica reescrita por extenso. Atenção: a mecânica reformada do Bastião (a área de Provocar, Retaliação com Força no PE) **não está neste repositório nem no principal** — só nesta tabela, que a restitui de segunda mão.
- **`bastiao-correcao-fagulha.md`** — a tabela histórica dava 4,08 fatias pra Fagulha; a correção diz 2,05, porque faltava aplicar o acerto do feitiço. **A revisão contesta a correção** (achado 12): a régua de Trilhas preça dano *cru*, sem acerto, e só a parcela de vantagem estava errada. Na régua crua, Fagulha dá **3,53**. Os três números estão documentados; a decisão é do autor.

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

**O registro vigente é `vanguarda-orcamento.md`.** Os outros documentos marcam no cabeçalho se são históricos.

### Estocada — quatro entregas fechadas, preço aberto

As quatro habilidades da Trilha fecharam como mecânica:

- **Compasso (nível 2)** ganha o atributo escolhido (Essência ou Inteligência) no PE máximo, além de conjurar na padrão e atacar na bônus.
- **Traçado (11) morreu** e virou seis **conclusões mágicas**: preparar a Sequência com arma e fechar com feitiço.
- **Bote (19)** mantido: feitiço de condição sem dano libera o ataque extra na bônus.
- **Ferrão (27)** agora só dispara depois de uma conclusão mágica que afete o alvo.

Mas o preço total **não** fechou, e o motivo é o achado mais importante da pasta: o preço zero antigo do Compasso se apoiava numa regra em que conjurar já dava um golpe de brinde. Desde a v0.147 do repositório principal o ataque extra exige a Ação de Atacar. Então Compasso e Bote hoje são *permissões de atacar depois de conjurar* — e isso tem preço. Só Compasso+Bote, num Refino 6, dá 4,46 fatias por rodada elegível. A Trilha não cabe em cinco sem conta nova.

**O registro vigente é `estocada-auditoria.md`.**

## Mapa dos arquivos

Os 35 arquivos da releitura ficam na raiz, com o nome dizendo a frente. Cada `conferir-*.py` tem um `*-contas.json` ao lado com a saída completa.

| Arquivo | Frente | Estado | O que é |
|---|---|---|---|
| `bastiao-nomes-aprovados.md` | Bastião | vigente | os dezoito nomes e a mecânica de cada um |
| `bastiao-correcao-fagulha.md` | Bastião | vigente, contestado | a conta corrigida de Fagulha |
| `conferir-fagulha.py` | Bastião | — | enumera 160 mil combinações de dado pra conferir Fagulha |
| `vanguarda-orcamento.md` | Vanguarda | **vigente** | o registro das cinco fatias e das regras que sustentam o preço |
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
| `conferir-vanguarda-nv23.py` · `-nv23-usos.py` | Vanguarda | — | Persistência com um uso por cena, e depois com contador por maestria |
| `estocada-auditoria.md` | Estocada | **vigente** | por que o preço total não fecha, e o que falta |
| `estocada-compasso.md` | Estocada | vigente | Compasso com atributo no PE |
| `estocada-conclusoes-feiticos.md` | Estocada | vigente | as seis conclusões mágicas |
| `estocada-bote.md` · `estocada-ferrao.md` | Estocada | vigente | níveis 19 e 27 |
| `conferir-estocada-auditoria.py` | Estocada | — | Ferrão e Compasso+Bote por enumeração de estados |
| `conferir-estocada-compasso-pe.py` | Estocada | — | só a parcela de PE do Compasso |
| `vanguarda-nao-acabou-comparacao.json` | Vanguarda | histórico | comparação da antiga Não Acabou, sem script próprio |

## Rodar os scripts

Python 3, sem dependência externa. Rode da raiz:

```bash
for v in conferir-*.py; do python3 "$v"; done
```

Cada um imprime a tabela dele e termina com uma linha de checagem (`OK` ou uma afirmação do que foi conferido). Os dez rodam limpos e reproduzem cada número dos documentos — conferido em 20/09/2026. Não há validador de regressão entre os `.md` e os scripts; os números dos documentos foram copiados da saída à mão.

`conferir-vanguarda-v3.py` carrega `conferir-vanguarda-v2.py` por caminho relativo; os dois precisam estar na mesma pasta. O mesmo vale pros de nível 23 e de Escolas, que carregam a v3.

## O que a revisão achou

Em 20/09/2026 dois agentes revisaram a pasta contra o repositório principal na v0.261. Os relatórios completos estão em `revisao/`; os achados mais importantes foram conferidos à mão depois. Resumindo o que **bloqueia** o porte:

1. **O Caminho tem 3 fatias no repositório, não 5.** E não tem nível 23. Toda a distribuição da Vanguarda depende de uma régua que ninguém escreveu.
2. **O texto das seis conduções e das sete conclusões de arma não está em arquivo nenhum.** Os documentos só têm o preço. Requisito, efeito, duração — isso vive na conversa que gerou a pasta.
3. **Compasso somando atributo no PE máximo contraria uma regra que tem motivo escrito** na peça 1: *"se um atributo somasse PE, ele viraria o atributo obrigatório de todo conjurador pela porta dos fundos"*.
4. **O alvo morre no meio da Sequência e o texto não diz o que acontece.** Dois mestres travam de jeito oposto.
5. **O repositório principal se contradiz sobre Não Pega** — a peça 6 dá pra Vanguarda, o manual põe no Bastião — e o porte tropeça nisso.

E o que vale corrigir antes: a correção de Fagulha trocou a régua (achado 12); Conclusão Dupla "por cena" deveria ser "por descanso curto" pela regra do próprio repositório; no nível 2 a Sequência perde dinheiro em toda rota (conta em `revisao/nivel-2.py`); Desorientar domina as outras conclusões mágicas; a v2 ainda publica regra velha sem aviso.

Na triagem de nomes, **cinco morreram** no validador do repositório (Condução, Conduzir, Precisão, Guarda, Impacto — as três últimas já são Melhoria ou Tema no manual, com o mesmo efeito e número diferente) e **seis precisam de outro nome** por sentido (Abrir/Abertura, Fechar a Rota, Golpe de Impacto, Derrubada, Desvio, Abrir Caminho). Os dezoito do Bastião passaram limpos.

`revisao/cruzamento-constantes.md` confere as 30 constantes que os scripts usam contra o documento dono: 26 batem com citação literal.

## O que está aberto

Na ordem em que um trava o seguinte:

1. **3 ou 5 fatias, com ou sem nível 23.** É montante de tudo.
2. **Recuperar o texto-base das conduções e conclusões** e botar em arquivo.
3. **Fagulha: 2,05 ou 3,53.** Depende de confirmar que a régua é crua.
4. Nomes.
5. Preço total da Estocada, e as duplas mágicas da Conclusão Dupla.
6. Em que nível cada pedaço da Sequência entra — hoje não está definido, e a Escola de Arma reformada só dispara na Abertura.
7. Levar pro JJK---Project, seguindo o procedimento de lá (validadores, CHANGELOG, mensagem de commit).

## As outras duas pastas

- **`referencia-jjk-project/`** — cópia somente-leitura de 22 arquivos do JJK---Project na v0.263, os que os documentos daqui citam como fonte. Tem um README próprio dizendo o que é cada um e por que está lá. Se discordar do repositório principal, o principal vence.
- **`revisao/`** — os dois relatórios de 20/09 e o script de nível 2. Não fazem parte da releitura; são revisão dela.

## Histórico deste repositório

Três commits, de propósito:

1. A pasta exatamente como foi entregue em 20/09/2026, mais um `.gitignore`.
2. Só a troca dos links: os documentos apontavam uns pros outros e pro repositório principal por caminho absoluto de uma máquina; viraram links relativos. Nenhuma palavra de texto mudou — o `git diff` desse commit só tem linhas com link.
3. Este README, a pasta de referência e a pasta de revisão.

## Licença e escopo

Mesmo escopo do JJK---Project: material de fã, sem fins comerciais, não afiliado à Shueisha, à MAPPA nem a Gege Akutami. Jujutsu Kaisen e seus personagens pertencem aos detentores originais.
