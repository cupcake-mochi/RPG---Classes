# Vanguarda — primeira auditoria de preço

**Histórico: os custos desta proposta foram substituídos pela [precificação v2](vanguarda-precificacao-v2.md), com os dados de abertura e o PE escalando por maestria propostos pelo autor.**

18 de setembro de 2026. Propostas para decisão; não é texto aprovado de manual.

## O que o autor confirmou nesta rodada

Manter perda de dano na abertura, mesmo que Abrir → Golpe de Impacto produza menos dano médio do que ataques comuns. O crítico continua uma aposta em concentrar dano; não recebeu vantagem nem dados adicionais.

## Proposta de custo

**Abrir: 0 PE; −2 no dano total do ataque que acertar, uma vez, mínimo zero.** Calcular os dados da arma, atributo e extras normalmente, incluindo crítico e Kokusen quando ocorrerem; descontar os 2 depois dos modificadores do atacante, antes da mitigação do alvo. Acertar abre a sequência mesmo que o dano termine em zero. O número 2 é proposta, não decisão do autor.

**Conduzir: 1 PE por tentativa, declarado e pago antes da rolagem.** Erro não devolve PE e não renova o prazo; conserva a sequência até seu prazo anterior. O teste de resistência decide o efeito secundário, não se o ataque contou como condução acertada. Trocar de condução encerra os efeitos sustentados da anterior na declaração, mesmo errando a nova.

**Concluir: sem PE adicional.** Consome a sequência mesmo no erro ou no sucesso do TR do alvo. Isso não significa que a conclusão seja gratuita no orçamento do Caminho.

Os seis nomes de condução continuam provisórios. O preço de 1 PE é candidato para Mudar o Ângulo, Pressionar a Guarda, Proteger o Avanço, Acompanhar o Movimento e Explorar o Desequilíbrio. **Fechar a Rota, com proibição absoluta de movimento em uma direção, não recebeu aprovação matemática para esse preço.**

## Dano completo do golpe

Médias de um acerto comum, antes de crítico, resistência ou redução, sem bônus de Trilha ou ferramenta:

| Perfil | Composição | Dano médio | Perda de 2 como parte do golpe |
|---|---|---:|---:|
| Katana, nível 2, atributo 3, refino 1 | 1d8 + 3 + 1d4 | 10,00 | 20,00% |
| Katana, nível 30, atributo 6, refino 8 | 1d8 + 6 + 3d4 | 18,00 | 11,11% |
| Katana, nível 30, atributo 6, refino 10 | 1d8 + 6 + 4d6 | 24,50 | 8,16% |
| Espadão, nível 30, atributo 6, refino 10 | 1d12 + 6 + 4d6 | 26,50 | 7,55% |
| Arco Daikyū, atributo 6, Lapidação 10 | 1d10 + 6 + 4d6 | 25,50 | 7,84% |
| Rifle, refino 10 | 2d8 + 4d6; não soma atributo | 23,00 | 8,70% |

**Usada a escada do manual publicado.** A peça técnica 11 §6.9 ainda tem uma tabela anterior (sem dado nos refinos 1–2 e um dado a menos até 9). Essa divergência não foi corrigida no repositório. O topo de 4d6 concorda nas duas fontes.

Canalizar e Estímulo Muscular são alternativas de rotas, não dois extras para somar. Seus dados não dobram no crítico. Um feitiço ou Kata de dano transportado no mesmo ataque exclui esses dados, conforme o texto publicado. Feitiço de Toque não é ataque de arma e não entra automaticamente nesta sequência.

O texto geral de Refino também fala em excluir o bônus na rodada de conjuração, enquanto a entrada específica fala no mesmo ataque. Os exemplos acima são rodadas só de arma, compatíveis com ambas as leituras; não resolvem essa divergência.

### O crítico, isolado

Espadão com atributo 6 e refino 10, sem bônus de Trilha, Kokusen inicial de 20%:

- Acerto comum médio: 26,50.
- Crítico médio incluindo a chance inicial de Kokusen: 36,30.
- Melhorar a margem de 20 para 19–20 acrescenta **0,49 de dano por tentativa de conclusão**, com um d20 e 19 já suficiente para acertar.
- A 55% de acerto, a tentativa de abertura pagando 2 perde **1,10 de dano esperado**.
- Abrir no primeiro ataque e tentar Impacto no segundo, apenas se abriu, dá **−0,8305** contra dois ataques normais.

Com Kokusen Melhorado, na chance inicial do mesmo refino, o ganho por tentativa de conclusão é 0,622 e a diferença do par é −0,7579. O acúmulo de falhas no d100 muda essas chances durante a missão; esses números são estados iniciais explícitos, não médias do dia.

**Interpretação aprovada pelo autor:** essa perda média pode permanecer. Ela não deve ser escondida nem compensada com vantagem automática.

## O PE em níveis diferentes

Uma Vanguarda tem 10 PE no nível 2 e 150 no nível 30. Um uso de 1 PE consome 10% ou 0,67% da reserva inicial, respectivamente. Descansos curtos recuperam 25% do máximo; conjuração, Katas e outras habilidades também usam essa reserva.

Modelo de três combates por dia, cada um com chance igual de durar três ou quatro turnos, 55% de acerto:

| Rota repetida | 1 ataque por turno, nível inicial | 2 ataques por turno |
|---|---:|---:|
| Abrir → uma condução acertada → concluir | 3,47 PE/dia | 5,74 PE/dia |
| Abrir → duas conduções acertadas → concluir | 4,99 PE/dia | 7,71 PE/dia |

Inclui tentativas erradas, sequências que expiram e sequências inacabadas ao fim da luta. É uma política de repetição, não uma previsão de comportamento dos jogadores. Com menos conduções por escolha, gasta menos.

**1 PE é um custo baixo no topo e significativo na criação.** Cobrar mais de todas as conduções para financiar Fixar puniria as opções menores. Não há motivo medido aqui para cobrar maestria em PE de todas elas.

**O orçamento foi examinado sem subtrair automaticamente 5,14 por PE gasto.** Essa conversão só representa perda de oportunidade quando o PE realmente compete com outro uso. Energia que sobraria não paga a habilidade em poder efetivo.

## Como foi contado o relógio

- Um ataque existente por etapa; abrir e conduzir/concluir podem usar ataques diferentes no mesmo turno.
- No máximo uma condução OU conclusão declarada por turno.
- No máximo duas conduções acertadas por sequência.
- Abertura ou condução acertada no turno T mantém a sequência até o fim de T+2.
- Erro ao conduzir não renova o prazo nem apaga imediatamente o prazo antigo.
- Conclusão encerra e impede nova abertura naquele turno.
- Efeitos de condução mantêm seus prazos individuais, não ganham dois turnos extras.
- As simulações supõem que o alvo sobreviva, permaneça acessível e atenda às condições exigidas. Não aplicam descontos arbitrários por requisitos difíceis.

O cálculo de frequências foi conferido por enumeração independente de todos os resultados possíveis dos ataques em **48 cenários**, com um ou dois ataques, um a quatro turnos, três comprimentos de sequência e duas taxas de acerto. As contagens coincidiram.

## Fechar a Rota: problema identificado

O texto aprovado na conversa impede aproximação OU afastamento após acerto e falha em TR. Impedir aproximação pode impedir todos os ataques de um inimigo que só alcance alvos de perto. Correr não atravessa uma proibição absoluta.

**Teste de geometria desfavorável ao inimigo:** não há outro alvo alcançável, arma de distância, teleporte ou efeito útil alternativo. Contando negar a rodada como os 219 equivalentes da régua do chefe, 55% de acerto, 35% de falha no TR, repetir duas conduções e então concluir produz **6,09 fatias somente com essa negação**, antes de cobrar a abertura. Com abertura −2, fica em **5,97 fatias**. Não inclui o benefício da conclusão.

Isso é um caso de teste, não a média das mesas. Serve para refutar a ideia de que impedir uma direção inteira custa apenas alguns metros. Subtrair PE teoricamente não garante que o problema desapareça.

**Proposta de ajuste, ainda não aprovada:** conservar a escolha aproximar/afastar e o TR, mas fazer cada metro percorrido na direção escolhida custar dois metros de deslocamento até o fim do próximo turno do usuário. Não acumular multiplicadores com terreno difícil. Isso permite gastar mais movimento ou converter ações para atravessar a pressão. O preço de movimento vira finito; ainda pede teste de mapa.

Essa mudança não reduz automaticamente a característica deslocamento do alvo e, portanto, **não satisfaz sozinha o requisito atual de Fixar**. Alterar esse requisito seria outra decisão.

## Fixar e o orçamento do Caminho

Cinco fatias equivalem a **25,40 de benefício equivalente por rodada no nível 30**. Esse orçamento pertence ao Caminho inteiro; os efeitos de uma Trilha não cabem nele automaticamente. Benefícios alternativos não são somados como se todos fossem usados simultaneamente, mas o valor de escolher a melhor opção também não é zero.

A régua publicada da peça 19 atribui 39,20 por rodada ativa a Lento e 132,15 a Impedido. Usamos o valor do efeito multiplicado pela frequência de aplicação, nunca 132,15 em todas as rodadas da luta.

### Triagem agregada de controle — não é o preço definitivo do catálogo

O modelo escolhe, a cada ataque, se vale abrir, conduzir, concluir cedo ou esperar uma conclusão maior. Faz três combates de três ou quatro turnos, desconta 2 por abertura acertada e não desconta PE. Conta a condição por uma rodada após aplicação.

**Simplificações declaradas:** requisitos externos sempre satisfeitos; até 3,39 equivalentes por condução acertada, como Proteger o Avanço; dá ainda o benefício de −1 ao TR na conclusão mesmo junto desse valor, uma concessão otimista para esta triagem. Há conclusão inicial avaliada em 3,45 (referência favorável de cobertura). Fechar a Rota com bloqueio absoluto está excluído. O modelo não pretende reproduzir simultaneamente todas as conduções, todas as interações de Trilha, nem transformar 3,39 num teto universal de utilidade.

| Limite de tentativas de Fixar por descanso longo | Referência: acerto 55%, falha de TR 35% | Precisão de Batedor: acerto 87,75%, falha de TR 55% | Estresse: acerto 95%, falha de TR 75% |
|---|---:|---:|---:|
| Sem limite adicional | 0,81 fatia | 3,61 fatias | 5,62 fatias |
| 2 tentativas | 0,80 fatia | 3,19 fatias | 4,82 fatias |
| 1 tentativa | 0,73 fatia | 2,51 fatias | 3,80 fatias |

87,75% é 65% de acerto antes de vantagem, compatível com o bônus de +2 do Mirar em cima de uma base de 55%. A coluna extrema é cenário de sensibilidade, não taxa atribuída ao personagem normal. A concessão de −1 ao TR da triagem entra por cima das taxas nomeadas na tabela.

**Um limite consome uso na declaração, mesmo se errar ou o alvo resistir.** A proposta de duas tentativas deixa apenas 0,18 fatia no teste extremo; uma tentativa deixa 1,20. Isso é espaço aritmético neste modelo, não uma medição de novas habilidades ainda não desenhadas.

Se for para preservar o controle completo de Impedido, **a proposta mais conservadora é Fixar como opção tardia, uma tentativa por descanso longo**, preservando as duas conduções e o requisito de movimento prejudicado já definido. Duas tentativas são uma alternativa se a Sequência ocupar praticamente todo o Caminho. Ambos são ajustes novos para aprovação.

## Limites da auditoria e próxima decisão

**Não há aprovação final de cinco fatias para o texto atual.** Existe um custo inicial defensável para abertura e conduções comuns, um estouro demonstrável de Fechar a Rota e propostas de frequência para Fixar.

A régua histórica das condições não é uma simulação atual de todas as fichas: Derrubado usa uma convenção antiga de deslocamento para levantar; Desarmado já inclui três metros para recuperar a arma (não foram somados novamente); Impedido tem vantagem de aliados e desvantagem dos ataques do alvo, mas não monetiza toda combinação possível com desvantagem no TR Físico. Pressionar também pode beneficiar ataques de feitiço, conforme o alcance da redação, e precisa ser fechado junto à Estocada. Essas limitações impedem chamar as casas decimais acima de preço final.

Não foram atribuídos gratuitamente os antigos Escola de Arma, Não Cede e Não Acabou por cima da nova base. Se algum permanecer, entra no orçamento restante e nas combinações. O ataque extra do nível 7 mantém o tratamento de correção de base da reforma.

**Orçamento sugerido para desenvolvimento:** mirar até quatro fatias para a Sequência e reservar uma para complementos. É uma alocação proposta, não o valor já medido da classe. Se o autor preferir investir as cinco na Sequência, os outros degraus devem desenvolver esse mesmo mecanismo, e não somar pacotes independentes de poder.

## Fontes e reprodução

Consulta somente leitura ao repositório local:

- [Aptidões e Refino](referencia-jjk-project/sistema/05-material/livro/manual/45-aptidoes-e-refino.md), dano de Canalizar e Kokusen.
- [Bênçãos e Lapidação](referencia-jjk-project/sistema/05-material/livro/manual/47-bencaos-e-lapidacao.md), Estímulo Muscular.
- [Dano e condições, peça 19](referencia-jjk-project/sistema/03-mecanica/19-dano-e-condicoes.md), equivalências e ressalvas da régua.
- Caminhos e Trilhas, Como Jogar, O Turno, Equipamento e Descanso e Recuperação, nos capítulos do manual publicado.
- Peça 26 §3.1, referência de acerto e resistência do inimigo; DESENHO-manhas e continuidade da reforma, unidade e orçamento.

As contas e suas hipóteses estão em conferir-vanguarda.py e vanguarda-contas.json, nesta mesma pasta autorizada. Nenhum arquivo do repositório de consulta foi alterado.
