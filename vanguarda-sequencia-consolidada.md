# Sequência de Combate — tudo que está escrito, com fonte

Consolidado em 21/09/2026. **Não é texto novo de regra.** É a junção de tudo que os documentos desta pasta dizem sobre Abrir, Conduzir e Concluir, mais o que só existe dentro dos scripts. Cada frase traz de onde veio. Quando duas fontes discordam, a mais nova vence e a velha vai marcada como histórico.

Isso existe porque a revisão de 20/09 achou que o texto-base da Sequência não estava em arquivo nenhum — só o preço de cada etapa. Este documento é o primeiro passo pra fechar esse buraco; o segundo é você escrever a regra.

**Siglas das fontes:** V1 = `vanguarda-precificacao-inicial.md` · V2 = `vanguarda-precificacao-v2.md` · ESC = `vanguarda-escolas-rascunho.md` · N23 = `vanguarda-nv23.md` · N23P = `vanguarda-nv23-proposta.md` · CD = `vanguarda-conclusao-dupla.md` · ORC = `vanguarda-orcamento.md` · EC = `estocada-compasso.md` · ECF = `estocada-conclusoes-feiticos.md` · EB = `estocada-bote.md` · EF = `estocada-ferrao.md` · **v2.py / v3.py** = `conferir-vanguarda-v2.py` / `-v3.py`, quando a regra só existe no código.

---

## 1. A forma geral

- Três etapas: **Abrir, Conduzir, Concluir**. Uma única sequência ativa por vez, contra um único inimigo. [CD]
- Cada etapa usa **um ataque que você já tem**. A Sequência não concede ataque nem ação. [V1, CD] O ataque da ação bônus do Compasso conta como ataque existente. [EC] Concluir com feitiço só existe pela Estocada. [ECF]
- **No máximo uma Condução OU uma Conclusão por turno.** Abrir e conduzir/concluir no mesmo turno, com ataques diferentes, pode. [V1, V2, CD, ORC]
- Reserva de orçamento: 2,00 fatias pra Sequência, 0,75 pra Escola de Arma. [ORC]
- Os nomes das seis conduções e das sete conclusões eram provisórios. [V1] A maioria fechou em 21/09 — ver §12.

## 2. Abrir

**A regra.** Acertar um ataque abre a sequência. O golpe que abriu **perde Xd4 do dano total, mínimo zero**, sendo X metade da maestria arredondada para cima: **1d4 nas maestrias 1 e 2, 2d4 nas 3 e 4.** [V2, ORC]

- A redução é rolada uma vez, quando o ataque acerta. Desconta-se do total depois dos modificadores do atacante e antes da mitigação do alvo. Não se subtrai de cada componente. Arma, atributo e Canalizar ou Estímulo Muscular entram normalmente. A redução não dobra no crítico. [V2]
- **Acertar abre mesmo que o dano termine em zero.** [V1, V2, ESC]
- Não pode abrir no turno em que concluiu. [V1, CD] Não pode reabrir uma sequência ainda ativa. [ESC] Depois de errar uma condução — sequência encerrada —, um ataque restante pode pagar uma nova Abertura, mas não dá outra condução naquele turno. [CD]
- Não custa PE. [V1, V2]

**Escola de Arma em cima da Abertura.** Ao acertar a Abertura com a categoria escolhida, você aplica a Manha da categoria — uma vez por sequência, no máximo uma por turno, resolvida depois do dano e da redução. Não dispara em condução, conclusão, ataque comum nem abertura que erre. [ESC] Versado: logo depois de acertar a Abertura, guarda uma arma e saca outra sem gastar ação, uma troca por sequência. [ESC]

**Histórico.** A primeira proposta era −2 fixo no dano, sem dado. [V1]

**Não está escrito:** se Abrir é declarado antes de rolar ou decidido depois de ver que acertou. Conduzir, Concluir com Dupla e Ferrão dizem "antes de rolar"; Abrir não diz nada.

## 3. Conduzir

**A regra.** Cada tentativa de Condução custa **metade da maestria arredondada para cima + 1 PE**, pago antes de rolar, inclusive se errar: **2 PE nas maestrias 1 e 2, 3 PE nas 3 e 4.** [V2, ORC]

- **Acertar o ataque é acertar a condução**, mesmo que o alvo passe no TR do efeito secundário. O acerto conta e renova o prazo. [V1, V2, CD]
- **Errar o ataque encerra a sequência imediatamente**, salvo gastar um uso de Persistência a partir do nível 23. [CD, ORC]
- **Não há teto de conduções acertadas.** Você conduz enquanto a sequência estiver ativa e puder pagar. [CD, ORC]
- Trocar de condução encerra os efeitos sustentados da anterior **na declaração**, mesmo que o novo ataque erre. Os benefícios não se acumulam. [V1, V2, CD]
- Os efeitos de condução têm prazo próprio; não ganham os dois turnos da sequência. [V1] No código, um efeito de condução vale até o fim do turno seguinte ao acerto. [v2.py, `be = t+1`]

**As seis conduções.** Nenhum documento traz o texto de regra delas. O que existe é a base de preço [V2, tabela "Valores de controle"] e como o script modela cada uma [v2.py]:

| Condução | O que faz, pelo que está escrito | Fonte |
|---|---|---|
| **Mudar o Ângulo** | 3 metros de reposicionamento (1,80 equivalentes). De quem, pra onde — não escrito. | V2 |
| **Pressionar a Guarda** | +1 no acerto dos seus ataques enquanto o efeito está ativo (o código usa +5 pontos percentuais). "Pode beneficiar ataques de feitiço, conforme o alcance da redação"; precisa fechar junto da Estocada. | V2, V1, v2.py |
| **Proteger o Avanço** | +1 de Defesa por rodada protegida (3,39). Soma com o +1 da Manha Guarda. | V2, ESC |
| **Acompanhar o Movimento** | Metade do deslocamento (× 0,60 por metro). Detalhe não escrito. | V2, v2.py |
| **Explorar o Desequilíbrio** | −1 no próximo TR elegível da conclusão (5 pontos percentuais). Exige um requisito externo: o alvo Derrubado ou Agarrado. Numa Conclusão Dupla afeta só um dos TRs. | V2, CD, v2.py (`external_explorable`) |
| **Fechar a Rota** | Após acerto e falha no TR Físico, o alvo não pode se afastar voluntariamente de você até o fim do próximo turno dele. Aproximar continua permitido. Movimento forçado e teleporte são exceções. Não reduz a característica de deslocamento — logo não satisfaz o requisito de Fixar sozinha. | V2, ORC, V1 |

**Histórico de Fechar a Rota.** A primeira versão impedia aproximação OU afastamento. Foi rejeitada porque, contra um inimigo que só alcança de perto, impedir aproximação nega a rodada inteira dele: 6 fatias só nisso. A alternativa de cobrar dois metros por metro não foi adotada. [V1, V2]

**Histórico do teto.** V1 e V2 tinham teto de duas conduções acertadas por sequência, e erro não apagava a sequência — só não renovava o prazo. A V2 ainda publica isso como vigente, sem aviso. Caiu em 19/09. [V2, CD]

## 4. Concluir

**A regra.** Concluir não custa PE adicional. **Consome a sequência mesmo errando ou se o alvo passa no TR.** Impede nova Abertura no mesmo turno. [V1, ORC, CD]

**As sete conclusões de arma.** Como nas conduções, não há texto de regra — só a base de preço [V2] e o que o script permite [v3.py, `available_finishes`]. As colunas *exige* e *fonte* vêm **só do código**, exceto onde marcado:

| Conclusão | Exige | Fonte | Efeito | Valor de preço |
|---|---|---|---|---|
| **Ponto Fraco** (antes Golpe de Impacto) | sequência aberta; zero conduções | corpo a corpo | margem crítica passa de 20 pra 19–20. Sem vantagem. [V2, ORC] | diferença real de crítico |
| **Explorar a Cobertura** | zero conduções | distância, alvo com cobertura | reduz a cobertura do alvo um degrau: Boa → Parcial, Parcial → nenhuma [V2] | melhora de chance |
| **Derrubada** | ≥ 1 condução [V2: "exige condução anterior"] | corpo a corpo ou distância | Derrubado, TR Físico; empurrão opcional | 8,45 + 0,90 |
| **Desarme** | ≥ 1 | corpo a corpo | Desarmado, TR Físico; a régua já inclui buscar a arma | 3,45 |
| **Interromper a Resposta** | ≥ 1 | distância | sem Reação; não desliga Bloquear [V2] | 36,50 |
| **Quebrar o Ritmo** | ≥ 1 | corpo a corpo ou distância | Lento, TR de Vigor [V2] | 39,20 |
| **Fixar o Alvo** | **≥ 2 conduções e o alvo já com movimento reduzido antes do ataque** [V1, V2, ORC] | distância; requisito externo de Lento | Impedido, TR Físico | 132,15 |

- Derrubada e Quebrar o Ritmo pertencem aos dois catálogos de arma. [CD, ECF]
- A CD dos TRs: 8 + atributo usado no ataque + maestria. [ESC, para as Manhas; ECF, para as conclusões mágicas. Para as conclusões de arma está implícito.]
- Depois de Fixar ou Derrubada, os seus ataques seguintes contra o alvo carregam a condição: vantagem com Impedido; vantagem de perto e desvantagem de longe com Derrubado. [v2.py, `attack()`]
- Fixar não tem contador por descanso. [V2, ORC] A V1 propôs uma ou duas tentativas por descanso longo; não foi adotado. [V1]

**Não está escrito:** quanto tempo dura cada condição aplicada (o preço supõe uma rodada); o que conta como "movimento reduzido" pra Fixar; se Interromper a Resposta e Desarme são mesmo só de uma fonte, ou se isso é simplificação do modelo.

## 5. Prazo e encerramento

- **Abertura ou Condução acertada no turno T mantém a sequência até o fim do turno T+2** — o segundo turno seu depois daquele. Exemplo: abriu ou conduziu no turno 1; pode retomar no 2 ou no 3; se não retomar, encerra no fim do 3. [V1, V2, CD, ORC]
- A sequência encerra por: erro no ataque de uma condução; fim do prazo sem retomar; uma conclusão resolvida, acertando ou não. [CD]
- Encerrar remove o acesso às etapas e o progresso acumulado. Efeitos com duração própria respeitam o prazo deles; movimento já feito não se desfaz; Guarda segue até o começo do seu próximo turno. [CD]
- Erro em condução **não** renova nem, antes de 19/09, apagava o prazo. [V1, V2 — histórico na parte de apagar]

**Não está escrito:** o que acontece se o alvo cai no meio da sequência; se dá pra abandonar uma sequência de propósito; se um ataque fora do seu turno (Reação, ataque de oportunidade, Revide) pode ser etapa — e, nesse caso, "por turno" e "turno seu" de quem.

## 6. Persistência — nível 23

Quando errar o ataque de uma Condução, pode gastar um uso pra impedir que o erro encerre a sequência. Sem ação, sem PE. **Usos: metade da maestria arredondada para baixo + 1, por descanso curto ou longo** — dois nos níveis 23–25, três nos 26–30. Avalia o resultado final do ataque, depois de rerrolagens, antes de decidir. [N23]

- O ataque continua errado; o PE continua gasto; não conta como acertada; **não renova o prazo**; ocupa a condução do turno; só preserva sequência ativa; efeitos encerrados por troca de condução não voltam. [N23]
- **Histórico:** um uso por cena. [N23P]

## 7. Conclusão Dupla — nível 30

**Uma vez por cena, ao Concluir uma sequência em que acertou pelo menos duas conduções, pode escolher duas conclusões diferentes da mesma fonte e aplicar as duas pelo mesmo ataque ou feitiço.** [CD]

- Fontes: corpo a corpo, distância, feitiço. **Não mistura.** A fonte da preparação não precisa ser a da conclusão. [CD, ECF]
- Escolhe as duas antes de rolar; os requisitos de ambas precisam estar cumpridos. Um ataque, uma rolagem, um dano. Cada conclusão com TR rola o seu; **resolve todos antes de aplicar os efeitos novos.** Explorar o Desequilíbrio afeta só um TR, e você declara a ordem antes. [CD]
- Consome o uso da cena na declaração, mesmo errando. Não dá ataque nem PE. Ocupa a conclusão do turno. [CD]
- Fixar + Quebrar o Ritmo: o movimento reduzido tem que existir antes de declarar; o Lento que a outra vai aplicar não serve. Impedido recém-aplicado não dá desvantagem no outro TR do mesmo ataque. [CD]

## 8. A Estocada em cima da Sequência

- **Compasso (2).** O ataque da ação bônus serve pra Abrir, Conduzir ou Concluir, com os custos e requisitos normais. O feitiço não é etapa e não renova prazo. [EC]
- **Conclusões mágicas (11).** Depois de acertar pelo menos uma Condução, um feitiço de Classe 1 ou mais que cause dano ou imponha condição ao alvo da sequência pode Concluir. Ativa se o feitiço acerta ou o alvo falha no TR principal — dano parcial não basta. Escolhe antes de resolver. Afeta só o alvo da sequência. Consome a sequência mesmo falhando. TR adicional com CD 8 + atributo do Compasso + maestria; os efeitos novos do feitiço não pioram esse TR. Uma conclusão mágica ocupa a etapa do turno e impede nova abertura nele. [ECF, EC]
  Seis opções: **Cortar a Resposta** (2 conduções, TR Físico, sem Reação) · **Abrir Caminho** (1, TR Físico, move o alvo 6 m e você meio deslocamento) · **Desorientar** (1, sem TR, desvantagem na próxima rolagem dele) · **Expor a Guarda** (2, TR de Vigor, vantagem no próximo ataque de um aliado) · **Ancorar** (2, TR Físico, deslocamento zero) · **Refluxo** (1, sem TR, metade do PE de uma condução em energia temporária). [ECF]
- **Bote (19).** Com feitiço de condição sem dano na padrão, dois ataques na bônus: o primeiro pode Abrir e o segundo Conduzir. Se o feitiço concluiu, os dois ataques não dão etapa nem abertura nova. O feitiço não conta como condução. [EB]
- **Ferrão (27).** Depois de Concluir com feitiço que afetou o alvo, o primeiro ataque da bônus leva um Classe 0. A sequência já terminou; Ferrão não reabre. [EF]

## 9. O que ficou sem escrever, junto

1. O texto de regra das seis conduções e das sete conclusões — requisito, efeito, duração, alcance, CD. Só existe o preço e o que o código permite.
2. Em que nível cada pedaço entra. [ORC: "a distribuição pelos níveis ainda pode ser definida"]
3. Abrir: declara antes ou decide depois.
4. O alvo cai no meio. Abandonar de propósito.
5. Ataque fora do seu turno como etapa.
6. Duração das condições das conclusões.
7. O que conta como "movimento reduzido" pra Fixar.
8. Se as restrições de fonte (Desarme só de perto, Interromper e Fixar só de longe) são regra ou simplificação do modelo.

## 10. Linha do tempo

| Quando | O que mudou | Fonte |
|---|---|---|
| 18/09, manhã | Primeira auditoria: Abrir custa −2 de dano, Conduzir 1 PE, teto de duas conduções, Fechar a Rota bloqueia uma direção inteira, Fixar com limite por descanso proposto | V1 |
| 18/09, tarde | Custos do autor: Xd4 e maestria/2+1 PE. Teto de duas mantido. Fechar a Rota só impede afastar. Fixar sem contador. Escola reduzida a quatro Manhas + Versado | V2, ESC |
| 18/09, noite | Não Cede mantido, reserva de 1,00 | NC |
| 19/09, manhã | Persistência: um uso por cena → metade da maestria pra baixo + 1 por descanso | N23P, N23 |
| 19/09, tarde | Sem teto de conduções; erro encerra; Conclusão Dupla no 30, com fontes que não misturam. Estocada: Compasso com atributo no PE, seis conclusões mágicas, Bote mantido, Ferrão após conclusão mágica | CD, ORC, EC, ECF, EB, EF |

---

## 11. O que a conversa de origem respondeu (21/09)

Em 21/09 o Mizuki trouxe a transcrição da conversa de 18/09 que gerou a Sequência. Ela tem o texto de regra que os documentos daqui não tinham. Contra a lista da seção 9:

| Lacuna | Estado | Onde a conversa responde |
|---|---|---|
| 1. Texto das seis conduções e sete conclusões | **respondida** | as duas tabelas da segunda rodada, com os ajustes da terceira (Acompanhar = metade do deslocamento; Fechar a Rota = só impede afastar; Quebrar o Ritmo = Lento, uma condução, nas duas fontes; Tirar da Cobertura removida) |
| 2. Em que nível cada pedaço entra | **aberta** | a conversa diz "distribuição por nível ainda em aberto" e para em "Sequência registrada em 2 fatias" |
| 3. Abrir: antes ou depois de rolar | **respondida** | *"Antes de rolar um ataque, declare que está abrindo uma sequência."* |
| 4. Alvo cai no meio; abandonar | **respondida, precisa ficar explícita** | *"Abrir uma sequência contra outro alvo substitui a anterior."* Isso derruba a leitura de ficar dois turnos travado. "Não pode reabrir sequência ativa" (ESC) vale pro mesmo alvo |
| 5. Ataque fora do turno como etapa | **respondida, precisa ficar explícita** | *"ataque com arma ou desarmado que você já possa realizar **no seu turno**"* e *"uma vez por turno **seu**"* — Reação não é etapa |
| 6. Duração das condições | **respondida** | Interromper: até o início do seu próximo turno · Fixar e Quebrar: até o fim do próximo turno do alvo · efeitos de condução: até o fim do seu próximo turno · Derrubado e Desarmado: regra própria da condição |
| 7. O que é "movimento reduzido" pra Fixar | **meio respondida** | *"alvo já com deslocamento reduzido por um efeito"*, e o requisito "permite aproveitar uma Manha, uma técnica própria ou a preparação de um aliado". Terreno difícil não é "efeito" — fica sem resposta |
| 8. Restrição de fonte é regra ou modelo? | **respondida: é regra** | as conclusões vêm em duas tabelas, *corpo a corpo* e *à distância*. Desarme só de perto; Interromper e Fixar só de longe; Derrubada e Quebrar nas duas. O código estava certo |

**O que a conversa tem e já morreu em 19/09 — não carregar pro texto:** errar condução *"conserva o prazo que já tinha"* (hoje: erro encerra); *"máximo de duas conduções acertadas"* (hoje: sem teto); e o prazo de *"até o fim do seu próximo turno"* do primeiro rascunho (virou T+2 ainda na conversa).

**E uma coisa que a conversa revela sobre o bloqueio do orçamento:** as "cinco fatias para o Caminho" aparecem só nas falas do assistente — *"antes de aprovarmos o conjunto nas cinco fatias"*, *"reservar as cinco fatias"*. O Mizuki nunca disse cinco; ele disse *"não pode estourar o quanto a fatia da classe pode dar"*. O 5 não foi decisão: foi premissa do chat. O repositório diz 3.

**Respostas do Mizuki, 21/09, às quatro pendências acima:**

1. **Nível de entrada:** Abrir, Conduzir e Concluir entram **no nível 2**, junto da Escola de Arma. Persistência (23) e Conclusão Dupla (30) continuam onde estão; o nível 23 não existe na escada do repositório e precisa de decisão.
2. **Terreno difícil conta** como movimento reduzido pra Fixar — ele já corta o deslocamento pela metade ("metade da metade").
3. **A duração escrita substitui o TR de fim de turno** das condições Pesadas: Impedido "até o fim do próximo turno dele" não rola TR pra terminar antes, porque vai terminar de qualquer jeito.
4. **Explorar e Fixar dependerem de aliado, feitiço ou Manha é de propósito.** Declarado, não é defeito.

**Decisão do Mizuki, 21/09: o orçamento do Caminho é 5 fatias nesta atualização** (a Trilha já era 5 no repositório). Isso muda a régua de `DESENHO-caminhos.md` (3 fatias, níveis 2 · 15 · 30) e precisa ser escrita lá quando o porte acontecer. Falta dizer se vale pros cinco Caminhos e se o nível 23 entra na escada de todos. O repositório registra que *"nenhum dos cinco Caminhos foi preçado contra as 3 fatias dele"* (`DESENHO-caminhos.md`, linha 176) — a régua de 3 estava escrita, não aplicada.

**O 1,39 aberto (conta rodada em 21/09 com o `conferir-vanguarda-v3.py`, cenário de referência, nível 30):** benefício bruto 3,45 − abertura 0,32 − PE 1,75 = **1,39 líquido**. Sem cobrar PE: **3,13**. Cobrando metade: 2,26. A cobrança de PE a 5,14 por ponto é convenção da auditoria v2, simétrica ao que o repositório paga por "+1 PE por rodada" (5,14, peça 5 §4); a v1 tinha argumentado contra descontar PE automaticamente. **Cobrando PE, a Vanguarda inteira mede ~3,0–3,25; sem cobrar, ~4,7–4,95.** Os dois orçamentos são as duas contabilidades.

**Decisões do Mizuki, 21/09, sobre a escada:** o orçamento de 5 fatias vale **pros cinco Caminhos**, e **todos passam a ter quatro habilidades — níveis 2, 15, 23 e 30 — sem contar o ataque extra do 7.** Isso substitui a régua de `DESENHO-caminhos.md` ("3 fatias, níveis 2 · 15 · 30") no porte.

## 12. Nomes fechados em 21/09

Triagem rodada no `conferir-nomes.py` do repositório principal, de `sistema/03-mecanica/`. Os cinco mortos do achado de nomes (Condução, Conduzir, Precisão, Guarda, Impacto) e quatro dos seis por sentido (Abertura como nome de conclusão, Golpe de Impacto, Derrubada, Desvio) ficam resolvidos assim:

| Onde | Nome antigo | **Nome novo** | Nota |
|---|---|---|---|
| Sequência inteira | Sequência de Combate | **Sequência de Condução** | "Condução" é ofício no repositório principal (peça 7, manual 12 e 25 — dirigir carro/moto/van); batizar a Sequência inteira com o nome desambigua. **Etapa 2 continua "Conduzir" / "uma condução"**, sem trocar — nunca colidia sozinha, só por associação com a Sequência sem nome próprio |
| Escola de Arma, Manha (bônus no próximo ataque) | Precisão | **Ritmo** | Precisão é Melhoria no manual (+2 no acerto), mesmo efeito, número diferente |
| Escola de Arma, Manha (+1 Defesa) | Guarda | **Postura Firme** | Guarda é Melhoria no manual (+2 Defesa), mesmo efeito, número diferente |
| Escola de Arma, Manha (empurrar 3 m) | Impacto | **Empuxo** | Impacto é Tema (tipo de dano) no manual |
| Escola de Arma, Manha (deslocar o alvo 1,5 m) | Desvio | **Mover Alvo** | sentido invertido: a Manha desloca o alvo, "desviar" no hobby é o defensor esquivando |
| Conclusão de arma (crítico em 19–20) | Golpe de Impacto | **Ponto Fraco** | Impacto é Tema (tipo de dano) no manual |
| Conclusão de arma (Derrubado + empurrão) | Derrubada | **Rasteira** | a uma letra de Derrubado (condição) e Derrubar (opção de ataque do manual) |
| Conclusão mágica da Estocada (desloca o alvo 6 m, você meio deslocamento) | Abrir Caminho | **Romper Fileira** | "Caminho" é a classe inteira — 53 arquivos do repositório principal usam o termo |

**Mantidos sem troca, colisão aceita de propósito:**
- **Fechar a Rota** (condução): "Rota" é termo definido no repositório principal (Rota de arma, Rota de ferramenta, peça 20 e manual 42; Rota: Yumi/Besta/Arma de Fogo do Batedor, manual 35) — colisão real, não incidental. Mantido por decisão do Mizuki.
- **Interromper a Resposta** (conclusão de arma, só à distância) e **Cortar a Resposta** (conclusão mágica da Estocada): mesmo efeito, dois nomes — ficam separados de propósito, porque são entregas de catálogos diferentes (arma × feitiço), não a mesma entrada duplicada.

**Ainda sem nome fechado:** a etapa 1 (Abrir/Abertura). "Abertura" colide de sentido com o vocabulário de Expansão de Domínio ("a cada abertura", "reaberturas"). Candidatos triados e livres: Golpe Inicial, Primeiro Golpe.
