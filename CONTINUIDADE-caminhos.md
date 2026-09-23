# Continuidade — Vanguarda, Guia e Emanador

## Acordo desta etapa

Autorizado pelo Mizuki em 22/09/2026: aprovar a Estocada no estado em que está; fechar as outras Trilhas da Vanguarda; validar de forma proporcional; reconstruir Guia do zero, com suas Trilhas, e validar; depois repetir com Emanador. O autor delegou decisões de identidade, nomes e regras. Não é necessário aguardar aprovação entre essas etapas.

**Evocador está fora do escopo.** Bastião, a fotografia `referencia-jjk-project/` e os relatórios de `revisao/` permanecem preservados. O porte ao projeto principal é outra tarefa. Não há autorização de commit ou push nesta etapa.

O objetivo das novas Trilhas é **até 5,50 fatias no cenário de referência**, com orçamento de projeto de 5,00. O Caminho conserva os quatro degraus pagos 2/15/23/30; o 7 é correção de base, sem nova parcela de orçamento. A validação usa poucos cenários representativos, confere ações, recursos e uma combinação evidente. Não tenta equilibrar todas as combinações possíveis nem transformar cenário excepcional em preço universal.

## Decisão encerrada: Estocada

**Aprovada pelo autor no estado atual.** Compasso exige feitiço de Classe igual ou superior à metade da máxima, arredondada para cima. Canalizar energia permanece no golpe; Ferrão substitui esse dano no golpe que carrega o feitiço. As demais habilidades ficam como estão.

Os cálculos anteriores são histórico de cenários. A aprovação é uma decisão de design do autor, não uma afirmação de que todas as fichas foram demonstradas abaixo de 5,50. A conta favorável com muitas conjurações não bloqueia mais a fila, por instrução expressa do autor.

## Ordem e documentos donos

| Etapa | Estado | Documento único de regra e decisões |
|---|---|---|
| Estocada | Aprovada; não reabrir o preço nesta etapa | `vanguarda-completo.md`, com referências aos registros já existentes |
| Batedor e Executor | **Descartados pelo autor; aguardam nova conversa criativa** | nenhum documento vigente |
| Validação da Vanguarda | Removida junto das duas propostas descartadas | — |
| Guia e suas Trilhas, do zero | Concluídos; nomes conferidos no validador do principal | `guia-completo.md` |
| Validação do Guia | Contas, ações compartilhadas e negativos aprovados | `guia-completo.md` |
| Emanador e suas Trilhas, do zero | Concluídos | `emanador-completo.md` |
| Validação do Emanador | Contas, recursos, revisão independente, nomes e contraprovas aprovados | `emanador-completo.md` |

Guia e Emanador terão, cada um, suas regras, exemplos, conta, referências de inspiração, decisões e registro de validação no próprio documento. Este arquivo só acompanha a fila; não duplica o conteúdo dessas regras.

## Consumo e ponto de parada

Leitura inicial do indicador semanal: **10% consumidos**. O autor confirmou **até 20 pontos percentuais adicionais nesta tarefa**, correspondendo a aproximadamente **30% no indicador total**, se a janela não reiniciar. O indicador é compartilhado pela conta, portanto outras tarefas também podem fazê-lo avançar.

Os contadores de tokens e as leituras de percentual ficam fora do repositório, em `/home/mizuki/CHAT-GPT/consumo-codex/projeto-m-classes/`. Entrada em cache já integra entrada; tokens de raciocínio já integram saída. Percentual de cota não é uma conversão fixa por token nem uma fatura.

Parar quando as três frentes estiverem concluídas e validadas, ou quando o consumo adicional chegar perto do teto confirmado. Se o teto chegar antes, registrar aqui a etapa exata, o que está pronto e o próximo passo. Não consumir crédito de reset.

## Registro da rodada

- 22/09: autorização de autonomia recebida; Estocada aprovada; limite de consumo confirmado; preparação independente das Trilhas da Vanguarda e pesquisa curta em livros locais iniciadas.
- 22/09, 22:25 UTC: indicador semanal em 16%, aproximadamente 6 pontos adicionais. O registro externo identifica o modelo e esforço reais das chamadas; não se usa a antiga proporção de tokens do esforço Alto para estimar o consumo do Ultra.
- 22/09: Guia reconstruído e validado: Caminho 4,52; Cartógrafo 4,39; Analista 3,07; Regente 4,37, incluindo reservas declaradas. A sensibilidade de Regente fica em 5,45. Iniciada a reconstrução do Emanador; o Guia concentra seu próprio histórico e suas contas.
- 22/09: Emanador reconstruído e validado: Caminho 4,47 na referência de ataques e 5,33 na alternativa com TR; Prisma 3,53; Crivo 3,71; Vestígio 3,61. Revisão independente corrigiu o benefício de cobertura no redirecionamento e a cobrança de terreno nas rodadas de detonação. Todos os registros estão no documento do Emanador.
- 22/09, 22:46 UTC: indicador em 20%, aproximadamente **10 pontos adicionais**, abaixo do limite autorizado de 20 adicionais. Os registros externos separam entrada, cache, saída, raciocínio e o modelo/esforço efetivos, sem converter tokens em percentual.
- 22/09, 22:50:59 UTC, leitura de encerramento: indicador em **22%**, aproximadamente **12 pontos adicionais** desde os 10% iniciais. Encerrado por sucesso, antes dos 30% totais que representariam o limite de 20 pontos adicionais. O indicador é compartilhado pela conta; os contadores de chamadas observadas estão no registro externo.

## Continuidade depois desta entrega

A etapa autônoma foi encerrada antes do teto de consumo. Estocada foi preservada conforme a aprovação; **todo o trabalho desta rodada em Batedor e Executor foi removido por decisão posterior do autor**; Guia e Emanador continuam reconstruídos e validados. Evocador, Bastião, revisão e fotografia de referência não foram modificados. A branch continua `codex/revalidacao-estocada`, com HEAD `84ec7a2` e as alterações locais sem commit ou push.

A próxima atividade útil é ler os três kits e, quando o autor quiser, realizar teste de mesa das decisões de posição, disponibilidade de Reação e reservas de utilidade. Essa atividade não foi iniciada. Os documentos já permitem retomar sem consultar a conversa inteira. Não há autorização implícita para portar regras, fazer commit/push ou trabalhar no Evocador.

Conferência restante: `python3 validacao/caminhos.py` e `python3 validacao/contrateses.py`. A missão aprovada da Estocada também permanece conferida por `python3 conferir-estocada-rotina.py --verificar-missao`. As contraprovas usam cópias temporárias e não alteram a fotografia de referência.
