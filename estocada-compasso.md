# Estocada — Compasso, nível 2

Versão de trabalho de 19 de setembro de 2026. **Exceção declarada em 21/09** contra a peça 1 §5.3 do repositório principal — ver [`excecao-atributo-no-pe.md`](excecao-atributo-no-pe.md). O autor aprovou acrescentar o atributo escolhido, entre Essência e Inteligência, ao PE máximo, seguindo a ideia de Força no PE máximo do Combatente Amaldiçoado. O núcleo de conjurar e atacar com a arma foi mantido. O nome Compasso continua sendo o nome de trabalho existente.

## Regra consolidada

**Escolha Essência ou Inteligência. Seu máximo de pontos de energia aumenta em um valor igual ao atributo escolhido.** Esse é também o atributo que Compasso permite usar no acerto e no dano das armas dos grupos escolhidos, no lugar de Força ou Destreza. O requisito de Força para empunhar continua valendo.

Escolha um grupo de armas para Compasso. Se escolheu Versado na Escola de Arma, pode escolher uma quantidade de grupos igual à sua maestria, conforme a regra já existente. A quantidade de grupos não multiplica o aumento de PE.

**Quando usar a ação Conjurar na ação padrão, pode fazer um ataque com uma arma de um desses grupos como ação bônus.** Compasso não exige que o feitiço acerte para liberar esse ataque.

O aumento é uma parcela do PE máximo, não um ganho de PE por ataque, condução ou conjuração. Para o Vanguarda sem outros modificadores, o máximo passa a ser **5 × nível + atributo escolhido**. Segue as regras normais de recuperação.

**Exemplos:** no nível 2, com Essência 3 escolhida, o máximo passa de 10 para 13 PE. No nível 30, com o atributo escolhido em 6, passa de 150 para 156 PE.

## Interação com a Sequência

O ataque da ação bônus é um ataque existente e pode ser usado para Abrir, Conduzir ou Concluir, respeitando os requisitos e custos dessas etapas. Permanece o limite de uma condução ou conclusão por turno. O feitiço não conta como uma etapa da sequência nem renova seu prazo por si só.

Compasso não libera automaticamente o ataque extra na ação bônus. Essa exceção pertence ao [Bote, nível 19](estocada-bote.md), mantido pelo autor quando o feitiço da ação padrão for de condição e não causar dano.

**Exemplo:** com uma sequência ativa, conjure na ação padrão e use o ataque da ação bônus para Conduzir. Pague o PE da condução normalmente. Acertar renova o prazo e registra uma condução bem-sucedida; errar encerra a sequência, salvo o uso de Persistência quando disponível.

## Preço da parcela nova de PE

A referência usa atributo 6 no nível 30, 10,5 rodadas de combate no dia, 1 PE = 5,14 equivalentes e uma fatia = 5,08 equivalentes por rodada. O valor por rodada é o total adicional disponível no dia dividido por 10,5; não se ganha o atributo em PE a cada turno.

| Situação declarada | PE adicional disponível no dia | Fatias nominais só do PE |
|---|---:|---:|
| Aumento inicial, sem recuperação adicional | 6 | **0,5782** |
| Um descanso curto com recuperação de 25% aproveitada | 8 | **0,7709** |
| Dois descansos curtos com recuperação de 25% aproveitada | 10 | **0,9636** |

O máximo maior também altera a recuperação: 25% de 150, arredondado para baixo, devolve 37 PE; 25% de 156 devolve 39. Portanto, cada descanso qualificado acrescenta 2 PE de recuperação nessa ficha. Os cenários supõem começar com PE cheio e ter espaço e demanda para aproveitar o incremento; capacidade disponível não é gasto garantido. Exaustão, descansos menos frequentes e PE sobrando podem reduzir o aproveitamento.

**Comparação com o Combatente Amaldiçoado:** a conta histórica do seu bônus de Força no PE máximo usa somente os seis PE iniciais, chegando aos mesmos 0,58. O cenário com recuperação foi explicitado aqui; nenhum preço anterior do Bastião foi alterado por esta revisão.

**Sugestão de reserva para a parcela de PE: 1,00 fatia**, considerando o cenário com dois descansos curtos aproveitados. É recomendação de orçamento, ainda não uma decisão numérica do autor nem o preço do Compasso inteiro.

O preço histórico zero para o núcleo do Compasso não está revalidado. A flexibilidade de conjurar e desenvolver a Sequência no mesmo turno, a escolha de atributo e a interação com Versado precisam participar da avaliação conjunta da Trilha. O câmbio de PE já representa o que esse recurso permite comprar: não se somará outra vez o benefício de gastar os mesmos pontos como se fosse recurso gratuito.

O orçamento da Estocada é separado das cinco fatias já reservadas para o Caminho Vanguarda. A adição de PE não foi cobrada novamente no Caminho, e o total da Trilha ainda está em revisão.

## Continuidade

**Nível 11 fechado como versão de trabalho:** o autor substituiu o segundo alvo de Traçado pela possibilidade de preparar a Sequência com armas e concluir com feitiço. O catálogo de seis opções está em [Estocada — conclusões para feitiços](estocada-conclusoes-feiticos.md), com os ajustes finais de Desorientar, Expor a Guarda e Refluxo. Rechaçar, que apenas empurrava 3 metros, foi rejeitada como fraca. O ataque da ação bônus de Compasso continua disponível, mas uma conclusão mágica ocupa a etapa da Sequência permitida no turno e impede nova abertura naquele mesmo turno. Bote, nível 19, foi mantido. [Ferrão, nível 27](estocada-ferrao.md), foi escolhido com gatilho após conclusão mágica. As quatro entregas estão definidas como versão mecânica de trabalho; a [conferência de orçamento](estocada-auditoria.md) registra por que o total da Trilha ainda não está validado.

Fontes de consulta: `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md`, seção Estocada; `sistema/03-mecanica/10-descanso-e-recuperacao.md`; regra reformada de Retaliação em `bastiao-nomes-aprovados.md`. Todos permanecem como consulta, sem alteração no repositório.

Conferência executada: `conferir-estocada-compasso-pe.py` e `estocada-compasso-pe-contas.json`, nesta pasta autorizada. A conta cobre apenas o acréscimo de PE.
