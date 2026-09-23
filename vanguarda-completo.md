# Vanguarda — Caminho e a Trilha Estocada, completo

Consolidado em 21/09/2026. Junta a conversa de origem de 18/09 (`vanguarda-sequencia-conversa-18-09.md`), os ajustes de 19/09, o consolidado com fonte por frase (`vanguarda-sequencia-consolidada.md`) e as seis decisões de 21/09 (PE, escala, níveis, nomes, exceção de atributo). O texto corrido de regra da Sequência está em [`RASCUNHO-sequencia-de-combate.md`](RASCUNHO-sequencia-de-combate.md). **A Estocada permanece aprovada no estado atual. Batedor e Executor não têm releitura vigente neste documento.**

O Caminho foi refeito em volta de uma mecânica central, a **Sequência de Condução**: você abre um golpe que perde dano, conduz pagando PE por tentativa, e conclui com um efeito forte. Errar uma condução encerra a sequência; ela também morre se ficar dois turnos sem retomar.

**Vida 5/nível · PE 5/nível.** Orçamento do Caminho: **5,00 fatias**, em quatro degraus — **2 · 15 · 23 · 30** —, com o ataque extra do 7 de graça. Vale pros cinco Caminhos do repositório principal, decisão do Mizuki de 21/09; substitui a régua velha de `DESENHO-caminhos.md` (3 fatias, 2 · 15 · 30), que nunca tinha sido aplicada a nenhum dos cinco.

## A contabilidade adotada: PE bruto

**Decisão de 21/09: o preço da Vanguarda conta o PE gasto bruto, sem descontar.** O câmbio de PE do repositório principal (1 PE = 5,14 de dano equivalente, peça 5 §4) não é subtraído do benefício de cada peça pra decidir se ela cabe no orçamento. Isso nunca muda quanto PE a Sequência custa em mesa — Conduzir sempre paga metade da maestria mais 1, nos dois jeitos de contar. A escolha só decide o que entra na conta do orçamento.

**A Vanguarda de distância fecha em 5,07 fatias.** A folga é parecida com a que o Bastião já tem publicada (5,20 a 5,58). **O perfil corpo a corpo mede só 1,34** — a diferença entre armas continua aberta, não resolvida por esta decisão. Contando o PE gasto (líquido), a assimetria é bem mais dura: a Sequência inteira vale zero pra quem usa espada, porque a política ótima simplesmente não abre sequência quando cada Condução custa PE e o retorno de Ponto Fraco não paga o câmbio.

Conta em `conferir-vanguarda-pe.py` / `vanguarda-pe-contas.json`.

## A Vanguarda de referência não conjura — achado de 21/09, noite, encerrado em 22/09

**Fechado pelo Mizuki em 22/09: a questão sai da fila.** *"Pode fazer sentido no papel, mas na lógica não vai funcionar assim"* — o terreno muda quando as Trilhas forem reescritas. Os números abaixo ficam como medição; o que morre é a pergunta de contra qual ficha preçar.

**Os 5,07 e os 1,34 acima foram medidos numa Vanguarda que ataca de arma nas 10,5 rodadas do dia e nunca conjura.** A régua do repositório principal não trabalha com essa ficha. O `conferir-orcamento.py` (bloco 1) calcula conjurações por dia = PE do Caminho × nível ÷ custo do maior feitiço — no nível 30, 150 ÷ 21 = **7 de 10,5 rodadas** —, e a peça 6 publica *"Vanguarda conjura 67% das rodadas no nível 30"* e preça o ataque extra do nível 7 só nas rodadas que sobram. Nas rodadas em que conjura, a Vanguarda sem Compasso não tem ataque de arma nenhum (desde a v0.147 o ataque extra exige a Ação de Atacar).

Medido nessa base (`conferir-estocada-rotina.py`, com o próprio v3 e as rodadas de conjuração no lugar; o PE da Condução continua bruto):

| Caminho completo | Vanguarda que nunca conjura | **Vanguarda que conjura 7 de 10,5** |
|---|---:|---:|
| Distância, sem Compasso (ficha favorecida por Batedor) | 5,07 | **1,09** |
| Distância, com Compasso (contrafactual com benefícios de Batedor) | 5,07 | **4,57** |
| Corpo a corpo, sem Compasso | 1,34 | **0,88** |
| Corpo a corpo, com Compasso | 1,34 | **1,22** |

**Sem Compasso, a Sequência quase não cabe**: só sobram 3,5 rodadas de arma no dia, espalhadas em três lutas, e o prazo de T+2 vence nas rodadas de conjuração. Sequência + Escola + Persistência + Conclusão Dupla somam 0,27 no perfil antigo de distância; quase todo o 1,09 é o Não Cede (0,82), que não depende de ataque. **Com Compasso no contrafactual**, o ataque de bônus devolve 3,48 ao Caminho, fora os 3,01 de dano cru dele. Essa segunda linha não é uma ficha de Estocada legal: retém Mirar, vantagem e deslocamento do Batedor, e Mirar disputaria a ação bônus. Ver os perfis corrigidos na [revalidação](RASCUNHO-revalidacao-estocada.md).

Isto **não reabre** a decisão de PE bruto — ela continua valendo nas duas colunas. A outra pergunta, contra qual Vanguarda o Caminho é preçado, foi encerrada em 22/09 sem ser respondida.

## Nomes fechados em 21/09

Triagem rodada no `conferir-nomes.py` do repositório principal (`sistema/03-mecanica/`). Cinco nomes mortos por colisão direta, quatro trocados por colisão de sentido:

| Nome antigo | **Nome novo** | Motivo |
|---|---|---|
| Sequência de Combate | **Sequência de Condução** | "Condução" é ofício no repositório principal (dirigir carro/moto/van); nomear a Sequência inteira com ele desambigua. A etapa 2 continua "Conduzir"/"uma condução" — nunca colidia sozinha |
| Precisão (Manha) | **Ritmo** | Precisão já é Melhoria no manual (+2 no acerto), mesmo efeito, número diferente |
| Guarda (Manha) | **Postura Firme** | Guarda já é Melhoria no manual (+2 Defesa), mesmo efeito, número diferente |
| Impacto (Manha) | **Empuxo** | Impacto é Tema (tipo de dano) no manual |
| Desvio (Manha) | **Mover Alvo** | sentido invertido: a Manha desloca o alvo, "desviar" no hobby é o defensor esquivando |
| Golpe de Impacto (conclusão) | **Ponto Fraco** | Impacto é Tema no manual |
| Derrubada (conclusão) | **Rasteira** | a uma letra de Derrubado (condição) e Derrubar (opção de ataque do manual) |
| Abrir Caminho (conclusão de feitiço) | **Romper Fileira** | "Caminho" é a classe inteira — 53 arquivos do repositório principal usam o termo |

**Mantidos, colisão aceita de propósito:** **Fechar a Rota** (condução) — "Rota" é termo definido do Batedor (Rota de arma, Rota: Yumi/Besta/Arma de Fogo), mas o Mizuki manteve. **Interromper a Resposta** (conclusão de arma, só à distância) e **Cortar a Resposta** (conclusão de feitiço) — nomes mantidos para catálogos diferentes (arma × feitiço). Hoje as janelas também diferem: Interromper dura até o próximo turno; Cortar afeta apenas o próximo ataque. A [comparação das janelas](RASCUNHO-comparacao-resposta.md) foi concluída; o Mizuki decidiu mantê-las diferentes em 22/09.

**Nome da etapa 1 fechado em 22/09/2026: Golpe Inicial.** Escolhido pelo Mizuki após triagem no validador do projeto principal. A mudança é de nome; custos, requisitos e efeitos permanecem iguais.

## O Caminho

### Nível 2 — Sequência de Condução + Escola de Arma

Reserva conjunta: **2,75 fatia** (Sequência 2,00 + Escola 0,75). Entram juntas no nível 2 por decisão do Mizuki de 21/09.

#### A Sequência — forma geral

Três etapas: **Golpe Inicial → Conduzir → Concluir.** Uma única sequência ativa por vez, contra um único inimigo. Cada etapa usa um ataque que você já tem — a Sequência não concede ataque nem ação. No máximo uma Condução **ou** uma Conclusão por turno; abrir e conduzir/concluir no mesmo turno, com ataques diferentes, pode.

**Golpe Inicial.** Antes de rolar um ataque, declare que está abrindo uma sequência. O golpe que abriu perde **Xd4 do dano total, mínimo zero**, sendo X metade da maestria arredondada pra cima — 1d4 nas maestrias 1 e 2, 2d4 nas 3 e 4. A redução é rolada uma vez, quando o ataque acerta, descontada depois dos modificadores do atacante e antes da mitigação do alvo; não dobra no crítico. Acertar abre mesmo que o dano termine em zero. Não custa PE. Não pode abrir no turno em que concluiu, nem reabrir uma sequência ainda ativa no mesmo alvo. **Dar o Golpe Inicial contra outro alvo substitui a sequência anterior.**

**Conduzir.** Cada tentativa custa **metade da maestria arredondada pra cima + 1 PE**, pago antes de rolar, inclusive se errar — 2 PE nas maestrias 1 e 2, 3 PE nas 3 e 4. Acertar o ataque é acertar a condução, mesmo que o alvo passe no TR do efeito secundário — o acerto conta e renova o prazo. **Errar o ataque encerra a sequência imediatamente**, salvo gastar um uso de Persistência a partir do nível 23. **Não há teto de conduções acertadas.** Trocar de condução encerra os efeitos sustentados da anterior na declaração, mesmo que o novo ataque erre; os benefícios não se acumulam.

**Concluir.** Não custa PE adicional. Consome a sequência mesmo errando ou se o alvo passa no TR. Impede novo Golpe Inicial no mesmo turno.

**Prazo.** Um Golpe Inicial acertado ou uma Condução acertada no turno T mantém a sequência até o fim do turno T+2 — o segundo turno seu depois daquele. A sequência encerra por: erro numa condução; fim do prazo sem retomar; uma conclusão resolvida, acertando ou não. Efeitos com duração própria respeitam seu prazo; movimento já feito não se desfaz.

**Ataque fora do seu turno não é etapa** — o texto-base diz "no seu turno" e "uma vez por turno seu"; Reação não conta.

#### As seis Conduções

| Condução | Efeito |
|---|---|
| **Mudar o Ângulo** | 3 metros de reposicionamento |
| **Pressionar a Guarda** | +1 no acerto dos seus ataques enquanto o efeito está ativo |
| **Proteger o Avanço** | +1 de Defesa por rodada protegida; soma com o +1 de Postura Firme |
| **Acompanhar o Movimento** | metade do seu deslocamento |
| **Explorar o Desequilíbrio** | −1 no próximo TR elegível da conclusão; exige o alvo já Derrubado ou Agarrado |
| **Fechar a Rota** | após acerto e falha no TR Físico, o alvo não pode se afastar voluntariamente de você até o fim do próximo turno dele. Aproximar continua permitido; movimento forçado e teleporte são exceções |

#### As sete Conclusões de arma

CD dos TRs: 8 + atributo do ataque + maestria. Duração das condições: Impedido e Lento "até o fim do próximo turno dele" **não** rolam TR de fim de turno — a duração escrita substitui esse TR (decisão de 21/09).

| Conclusão | Exige | Fonte | Efeito |
|---|---|---|---|
| **Ponto Fraco** | nenhuma condução mínima | corpo a corpo | margem crítica passa de 20 pra 19–20, sem vantagem |
| **Explorar a Cobertura** | nenhuma condução mínima | distância, alvo com cobertura | reduz a cobertura um degrau: Boa → Parcial, Parcial → nenhuma |
| **Rasteira** | ≥ 1 condução | corpo a corpo ou distância | Derrubado, TR Físico; empurrão opcional |
| **Desarme** | ≥ 1 | corpo a corpo | Desarmado, TR Físico |
| **Interromper a Resposta** | ≥ 1 | distância | sem Reação até o começo do seu próximo turno; não desliga Bloquear |
| **Quebrar o Ritmo** | ≥ 1 | corpo a corpo ou distância | Lento, TR de Vigor |
| **Fixar o Alvo** | ≥ 2 conduções, alvo já com deslocamento reduzido antes do ataque | distância | Impedido, TR Físico |

Rasteira e Quebrar o Ritmo pertencem aos dois catálogos de arma. Depois de Fixar ou Rasteira, seus ataques seguintes contra o alvo carregam a condição: vantagem com Impedido; vantagem de perto e desvantagem de longe com Derrubado. "Movimento reduzido" pra Fixar inclui terreno difícil (decisão de 21/09 — ele já corta o deslocamento pela metade) e depende de aliado, feitiço ou Manha — **de propósito**, não defeito.

#### Escola de Arma

| Categorias | Manha | Efeito no Golpe Inicial acertado |
|---|---|---|
| Lâmina Curta, Arremesso, Yumi, Balestra, Arma de Fogo | **Ritmo** | +1 no próximo ataque com a categoria contra o alvo da sequência; consome mesmo errando |
| Lâmina Longa, Manopla, golpes desarmados | **Postura Firme** | +1 de Defesa até o começo do seu próximo turno; não acumula consigo mesma; inclui Bloquear |
| Massa, Porrete, Machado, Armas Longas | **Empuxo** | TR Físico; na falha, empurra até 3 m |
| Ceifa, Flexível | **Mover Alvo** | TR Físico; na falha, desloca até 1,5 m |

Aplica a Manha da categoria uma vez por sequência, no máximo uma por turno, resolvida depois do dano do Golpe Inicial. Não dispara em condução, conclusão, ataque comum ou abertura que erre.

**Versado, alternativa:** logo depois de acertar o Golpe Inicial, guarda uma arma e saca outra sem gastar ação, uma troca por sequência. Abre com qualquer arma elegível, sem as Manhas de categoria.

**Escola conferida no modelo v3 em 22/09:** [a tabela atual](vanguarda-escolas-rascunho.md) e `vanguarda-escolas-contas.json` separam o líquido do bruto adotado. Os valores históricos de 18/09 permanecem identificados no documento da Escola.

### Nível 15 — Não Cede

Reserva: **1,00 fatia** (medido 0,8173, não depende de PE).

> Quando falhar em qualquer Teste de Resistência, pode repetir o teste e usar o segundo resultado. Pode usar um número de vezes igual à **maestria por descanso curto**, no máximo **uma vez por rodada**. Não exige ação nem PE. Não recebe +1 na rerrolagem — dispensado expressamente pelo Mizuki.

Regra original mantida, sem o adicional que tinha sido cogitado. Entra no nível 15 — era onde já estava na progressão antiga, e nada mais disputa esse degrau.

### Nível 23 — Persistência

Reserva: **0,25 fatia** (marginal medido 0,2091 antes do 30). *Nome provisório.*

> Quando errar o ataque de uma Condução, pode gastar um uso pra impedir que o erro encerre a sequência. Avalie o resultado final do ataque, depois de rerrolagens, antes de decidir. Sem ação, sem PE.
>
> Usos: **metade da maestria arredondada pra baixo + 1**, por descanso curto ou longo — dois nos níveis 23–25, três nos 26–30.

O ataque continua errado, o PE continua gasto, não conta como acertada, **não renova o prazo**, ocupa a condução do turno. Só preserva sequência ativa, não recupera expirada. Efeitos encerrados por troca de condução não voltam.

### Nível 30 — Conclusão Dupla

Reserva: **1,00 fatia** (marginal medido 0,8395 com Persistência já presente). *Nome provisório.*

> Uma vez por cena, ao Concluir uma sequência em que acertou pelo menos duas conduções, escolha duas conclusões diferentes da mesma fonte e aplique as duas pelo mesmo ataque ou feitiço.

**Fontes: corpo a corpo, distância, feitiço — não mistura.** A fonte da preparação não precisa ser a da conclusão (preparar com arma, concluir com duas de feitiço, é permitido pela Estocada). Escolhe as duas antes de rolar; ambas precisam ter os requisitos cumpridos. Um ataque, uma rolagem, um dano; cada conclusão com TR rola o seu, resolve todos antes de aplicar os efeitos. Explorar o Desequilíbrio afeta só um TR, ordem declarada antes. Consome o uso na declaração, mesmo errando.

**Fixar + Quebrar o Ritmo:** o movimento reduzido precisa existir antes de declarar; o Lento que a outra vai aplicar não serve pra satisfazer o requisito. Impedido recém-aplicado não dá desvantagem no outro TR do mesmo ataque.

### O livro-caixa do Caminho — bruto, perfil de distância

| Peça | Reserva | Marginal medido |
|---|---:|---:|
| Sequência de Condução | 2,00 | 3,01 |
| Escola de Arma (Ritmo) | 0,75 | +0,12 |
| Não Cede (15) | 1,00 | 0,82 |
| Persistência (23) | 0,25 | +0,28 |
| Conclusão Dupla (30) | 1,00 | +0,84 |
| **Total** | **5,00** | **5,07** |

No perfil corpo a corpo (lâmina longa, Postura Firme), o mesmo total bruto mede **1,34** — Não Cede sozinho já é 0,82 dele; a Sequência inteira soma só 0,52.

## Trilha Estocada — Compasso e o catálogo de feitiços

### Nível 2 — Compasso

*Exceção declarada contra a peça 1 §5.3 do repositório principal — ver `excecao-atributo-no-pe.md`.*

> Escolha Essência ou Inteligência. Seu **PE máximo** aumenta em um valor igual ao atributo escolhido — o máximo passa a ser **5 × nível + atributo**. Esse é também o atributo que Compasso permite usar no acerto e no dano das armas dos grupos escolhidos, no lugar de Força ou Destreza. O requisito de Força pra empunhar continua valendo.
>
> Escolha um grupo de armas. Com Versado na Escola, escolhe grupos iguais à maestria.
>
> **Quando usar a ação Conjurar na ação padrão para lançar um feitiço cuja Classe seja pelo menos metade da maior Classe que você pode conjurar, arredondada para cima, pode fazer um ataque com arma de um desses grupos como ação bônus.** Não exige que o feitiço acerte pra liberar esse ataque.

No nível 30, a Classe máxima é 7 e Compasso exige **Classe 4 ou maior**. Bote e Ferrão usam a ação bônus de Compasso e precisam que ela tenha sido liberada; o Classe 0 carregado por Ferrão continua sendo Classe 0.

O ataque da ação bônus é um ataque existente e pode ser usado para dar o Golpe Inicial, Conduzir ou Concluir. O feitiço não conta como etapa nem renova o prazo por si só. Preço da parcela de PE: **0,58 a 0,96 fatia** (atributo 6 no nível 30; 0,58 sem descanso extra, 0,96 com dois descansos curtos aproveitados). O núcleo de conjurar-e-atacar não está revalidado como preço zero — participa da avaliação conjunta da Trilha.

### Nível 11 — as seis conclusões de feitiço

*Substitui Traçado. Base: depois de acertar pelo menos uma Condução, um feitiço de Classe 1 ou mais que cause dano ou imponha condição ao alvo da sequência pode Concluir. Ativa se o feitiço acerta ou o alvo falha no TR principal — dano parcial não basta. Escolhe antes de resolver; CD do TR adicional 8 + atributo de Compasso + maestria.*

| Conclusão | Exige | TR | Efeito | Fatia por trigger |
|---|---|---|---|---:|
| **Cortar a Resposta** | 2 conduções | Físico | o alvo não pode usar Reação contra o **próximo ataque** que sofrer | 0,34 |
| **Expor a Guarda** | 2 conduções | Vigor | próximo ataque de um aliado contra ele tem vantagem | 0,34 |
| **Romper Fileira** | 1 condução | Físico | move o alvo até 6 m; você se move até metade do deslocamento, sem gastar ação | 0,43 |
| **Refluxo** | 1 condução | sem TR | metade do PE gasto numa única condução acertada vira energia temporária | 0,56 |
| **Desorientar** | 1 condução | sem TR | próxima rolagem do alvo, de qualquer natureza, com desvantagem | 0,62 |
| **Ancorar** | 2 conduções | Físico | deslocamento do alvo cai a zero até o fim do próximo turno dele | 0,32 |

Preços medidos em 21/09 (`conferir-estocada-conclusoes-magicas.py`), pela régua já publicada do repositório principal: dois gates onde a opção pede TR adicional (o feitiço precisa acertar/o alvo falhar no TR principal, **e depois** falhar o TR adicional da opção), um gate só onde não pede. **Dois achados, resolvidos em 21/09:**

- **Cortar a Resposta pedia as mesmas 2 conduções que Expor a Guarda e Ancorar, e valia de 3× a 6× mais** — na mecânica antiga, "sem Reação até o começo do seu próximo turno" (janela larga, magnitude 36,50 — meia ação de chefe). **Decisão do Mizuki: estreitar a mecânica.** Agora nega Reação só contra o próximo ataque, não a janela inteira — mesma lógica de "vantagem numa rolagem" que Expor a Guarda já usa, e bate no mesmo número: 0,34. ⚠ Isto estreita só a versão de feitiço; a irmã de arma, **Interromper a Resposta**, continua com a janela larga e o 36,50 dentro do modelo já validado (`conferir-vanguarda-v3.py`) — o Mizuki decidiu manter essa diferença em 22/09: a conjuração oferece uma entrega própria, então o efeito adicional pode ter janela menor. A comparação dos dois cenários está em `RASCUNHO-comparacao-resposta.md`.
- **Desorientar não tinha convenção publicada pra "próxima rolagem de qualquer natureza".** Decisão do Mizuki: fecha no piso, 0,62 — a rolagem que ele pega é imprevisível, às vezes ataque, às vezes perícia sem importância nenhuma, e o preço tem que refletir o caso médio, não o favorável.

Catálogo fechado como versão mecânica de trabalho; preço do conjunto (rotina completa com Compasso/Bote/Ferrão, e as duplas de feitiço do 30) ainda não validado (ver "o que falta" abaixo).

### Nível 19 — Bote

> Quando conjurar na ação padrão um feitiço de condição que **não causa dano**, pode usar seu ataque extra na ação bônus de Compasso — o primeiro ataque pode dar o Golpe Inicial, o segundo Conduzir.

Não recebe outra ação bônus nem terceiro ataque. Se o feitiço concluiu, os dois ataques não dão etapa nem abertura nova. O feitiço não conta como condução por satisfazer o gatilho de Bote. **Bote e Ferrão são incompatíveis no mesmo turno.**

### Nível 27 — Ferrão

> Quando Concluir com um feitiço da ação padrão que afete o alvo, o primeiro ataque da ação bônus de Compasso pode carregar um feitiço de **Classe 0** junto.

Escolha usar Ferrão antes de rolar o ataque da arma; se a arma errar, o Classe 0 não sai. O Classe 0 resolve sua própria rolagem — a arma acertar não acerta o feitiço automaticamente. Se o ataque carregar um Classe 0 de dano, não soma o dano de Canalizar ou Estímulo Muscular naquele golpe. A sequência já terminou; Ferrão não reabre.

### O que falta pra fechar o preço da Estocada

O preço zero antigo do núcleo de Compasso se apoiava numa regra em que conjurar já dava um golpe de brinde — desde a v0.147 do repositório principal o ataque extra exige a Ação de Atacar, então Compasso e Bote hoje são **permissões de atacar depois de conjurar**, e isso tem preço. Falta:

1. ~~Comparar rotinas completas com a mesma ficha-base.~~ **Feito em 21/09** (`conferir-estocada-rotina.py`, `TUDO OK`, duas implementações independentes concordando). **A primeira versão desta conta, da mesma tarde, estava errada e foi desfeita**: comparava a Estocada com uma Vanguarda que nunca conjura e cobrava o feitiço a 5,14 por PE, e concluía que "Compasso nunca vence a arma pura". A régua do repositório principal diz que a Vanguarda de nível 30 conjura em 7 das 10,5 rodadas do dia (150 PE ÷ 21 do Classe 7, `conferir-orcamento.py`), e o 5,14 saiu dos próprios feitiços — cobrar o feitiço por ele faz qualquer feitiço valer zero. Refeito na base certa, em 7 conjurações por dia, bruto:

   | Entrega | Distância | Corpo a corpo |
   |---|---:|---:|
   | Compasso (2) — sobre a Sequência sozinha | **5,35** | **2,13** |
   | … dos quais, o dano cru dos 7 ataques de bônus | 3,01 | 1,98 |
   | Conclusões de feitiço (11) | **0,00** | **0,00** |
   | Bote (19), se todo feitiço conjurado for de condição sem dano | até **3,43** | até **2,05** |
   | Ferrão (27) | **0,00** | **0,00** |

   **O Compasso sozinho passa do orçamento inteiro da Trilha no perfil de distância.** O nível 11 e o 27 valem zero na referência: o ataque de bônus do Compasso já pode Concluir de arma, e toda conclusão de arma disponível vale mais que a melhor conclusão de feitiço — o otimizador nunca troca uma pela outra, e Ferrão depende de uma conclusão de feitiço pra disparar. O Bote é teto: supõe que todo feitiço conjurado seja de condição sem dano e que o feitiço de condição valha o mesmo que o de dano da mesma Classe (que é o que a economia de pontos do Fundamento promete, mas não foi medido aqui).
2. ~~Medir as seis conclusões de feitiço como catálogo de escolhas.~~ **Feito em 21/09**, tabela acima.
3. Conferir as duplas de feitiço do nível 30. A soma aditiva corrigida pela régua de condições vai de 0,66 a 1,18 fatia por acionamento condicionado; o maior par nessa abstração é Refluxo + Desorientar e o menor é Ancorar + Cortar a Resposta ou Ancorar + Expor a Guarda. São **tetos aditivos, não marginais do dia**: a dupla compartilha o gatilho do feitiço, pode sobrepor efeitos, exige preparação e compete com concluir pela arma. A frequência conjunta por cena ainda não foi medida.
4. Distribuir as cinco fatias da Trilha: na hipótese de feitiços de condição sem dano tão valiosos quanto os de dano, os números acima vão de 5,35 a 8,78 no perfil de distância e de 2,13 a 4,19 no corpo a corpo, concentrados no 2 e no 19. **Não são o preço líquido da Trilha.** A escolha entre os feitiços foi revalidada depois; ver abaixo.

**Comparação complementar de 22/09, condicionada:** os números do item 1 usam a Sequência sozinha. No Caminho completo, a ficha antiga de Yumi com benefícios de Batedor e Fixar prévio dá **6,49 fatias** para ataques e interações de Compasso (**2,32** na outra ficha corpo a corpo), antes de impor recursos compartilhados da missão. Se todos os sete feitiços habilitarem Bote e seu valor próprio empatar com a alternativa de dano, o cenário favorecido chega a **9,99** (**4,42** corpo a corpo). A [revalidação corrigida](RASCUNHO-revalidacao-estocada.md) separa os perfis sem Batedor e o custo de escolher feitiços de condição. Nenhum limite virou regra.

**Revalidação da escolha de feitiço:** [o cálculo atualizado](RASCUNHO-revalidacao-estocada.md) separa 3,01 fatias de ataques e 3,48 de interações no perfil antigo da Yumi. Sem Batedor, a Yumi mede **2,92** com Fixar previamente disponível e **2,43** sem Fixar, ainda condicionados ao modelo. O `21d8` com 55% de acerto e 5% de crítico vale **56,70**, não 66,15. No perfil sem Batedor e com Fixar, Bote vai de **0,00** se a condição valer zero a **2,14** se ela empatar com esse feitiço de dano. Sem descanso, sete Classe 7 deixam 3 PE na reserva base ou 9 com os seis extras; com descanso, o PE pode caber, mas a conta anterior reinicia Persistência e Conclusão Dupla por combate. Ultrapassar **5,50** não está demonstrado como resultado robusto entre fichas e rotinas.

## O que continua aberto

- **A assimetria entre distância e corpo a corpo** — 5,07 contra 1,34 no bruto; mais dura ainda no líquido.
- **O preço total da Estocada**, e as duplas de feitiço da Conclusão Dupla.
- **O alvo cair no meio da sequência**: o texto de regra agora explicita que um Golpe Inicial contra outro alvo substitui a sequência anterior; ainda não há regra nova de transferência gratuita.
- Revisar o [`RASCUNHO-sequencia-de-combate.md`](RASCUNHO-sequencia-de-combate.md) antes de portar o texto ao repositório principal.

## Fontes

`vanguarda-sequencia-conversa-18-09.md` (texto-base) · `vanguarda-sequencia-consolidada.md` (fonte por frase + decisões de 21/09) · `vanguarda-orcamento.md` (registro vigente do orçamento) · `vanguarda-nao-cede.md` · `vanguarda-nv23.md` · `vanguarda-conclusao-dupla.md` · `vanguarda-escolas-rascunho.md` · `estocada-compasso.md` · `estocada-conclusoes-feiticos.md` · `estocada-bote.md` · `estocada-ferrao.md` · `estocada-auditoria.md` · `RASCUNHO-orcamento-estocada.md` / `estocada-orcamento-cenarios-contas.json` · `excecao-atributo-no-pe.md` · `conferir-vanguarda-pe.py` / `vanguarda-pe-contas.json`, `conferir-estocada-conclusoes-magicas.py` / `estocada-conclusoes-magicas-contas.json` (validadores, `TUDO OK`).

**Comparação de 22/09:** os dois cenários de janela foram medidos em [Comparação de Resposta](RASCUNHO-comparacao-resposta.md), incluindo Sequência, Caminho completo, Dupla e efeito para o grupo. O Mizuki decidiu manter as janelas diferentes: Interromper continua com a janela larga e Cortar continua limitado ao próximo ataque.

**Decisão de 22/09 — mínimo de Classe em Compasso:** aplicado por autorização condicional do autor após a missão conjunta superar 5,50 em um cenário favorável. O requisito é metade da Classe máxima, arredondada para cima. Na Yumi sem vantagem e com Fixar externo, sete Classe 7 dão 4,34–4,66 fatias conforme descansos; com Classes livres e dois descansos, controle suposto equivalente ao dano, a versão anterior dá 6,861 e a nova 6,860. Portanto, o requisito não assegura 5,50. O arredondamento para baixo dá o mesmo resultado neste cenário e jamais reduz o conjunto de ativações. Ver a [missão conjunta](RASCUNHO-revalidacao-estocada.md). As estimativas antigas acima não substituem essa comparação.
