# Conclusões de feitiço — dominância de Desorientar

Análise de 22/09/2026. **Decisão do Mizuki: manter Desorientar e as demais conclusões de feitiço como estão.** Nenhuma habilidade foi alterada nesta rodada. Os preços vigentes por acionamento vêm de `estocada-conclusoes-magicas-contas.json`; não são o valor marginal da Trilha por dia.

## As seis escolhas hoje

Todas exigem que o feitiço elegível afete o alvo; essa primeira chance é de 55% na referência. O TR adicional, quando existe, tem 55% de falha na mesma referência. Assim, Desorientar e Refluxo têm um gate, as outras quatro têm dois.

| Opção | Conduções | TR adicional | Preço por acionamento | Ganho próprio | Perda de valor ou sobreposição |
|---|---:|---|---:|---|---|
| Cortar a Resposta | 2 | Físico | 0,3424 | Protege o próximo ataque da Reação do alvo; benefício direto ao grupo | Alvo já gastou a Reação, feitiço já a proíbe, ou o ataque seguinte não precisa dessa proteção; Bloquear ainda vale |
| Expor a Guarda | 2 | Vigor | 0,3424 | Dá vantagem ao próximo ataque de um aliado | Sem aliado que ataque antes do prazo, vantagem já existente ou ataque resolvido por TR |
| Romper Fileira | 1 | Físico | 0,4287 | Move o alvo e permite seu deslocamento | Sem espaço útil, obstáculo, ou posição que o feitiço já resolveu |
| Refluxo | 1 | nenhum | 0,5565 | Entrega 1 PE temporário no perfil medido | Reserva temporária maior ou nenhuma ocasião para gastar antes de expirar |
| Desorientar | 1 | nenhum | 0,6225 | Afeta a próxima rolagem do alvo, de qualquer natureza | O alvo não rola no prazo, a primeira rolagem é irrelevante, ou já há desvantagem |
| Ancorar | 2 | Físico | 0,3216 | Impede movimento voluntário até o fim do próximo turno do alvo | Alvo não pretende mover, teleporta, ou o feitiço já zerou o deslocamento |

**Teste de dominância.** Desorientar lidera as opções de uma Condução na comparação escalar se a próxima rolagem do alvo tiver todo o valor convencionado. Isso o torna escolha automática **dentro dessa abstração**. Não há dominância estrita das regras: Refluxo gera energia temporária sem depender de rolagem inimiga; Romper muda posições imediatamente; Cortar protege de Reações que não exigem rolagem; Expor beneficia um ataque aliado mesmo que o inimigo não role; Ancorar impede movimento sem precisar de uma rolagem futura. Desorientar também não substitui Ancorar num alvo que vai fugir sem rolar. Ancorar exige outra Condução e TR adicional. Sua magnitude de deslocamento foi corrigida para 5,40, diferença entre Impedido e Cego na régua publicada.

**Filtro de vários mestres.** O texto atual fixa qual rolagem recebe a desvantagem, quando expira, como resolve Bloquear/dados percentuais e quando cancela vantagem. Dois mestres conseguem aplicar o efeito. O dado ausente é a frequência com que a primeira rolagem é valiosa, que varia por inimigo, iniciativa e feitiço escolhido; não foi medida em mesa. Chamar 0,6225 de piso universal seria impreciso: a conta assume uma rolagem útil com magnitude convencional, embora Bloquear, dano e perícia não tenham necessariamente o mesmo valor de uma rolagem de ataque. A rotina completa disponível em `conferir-estocada-rotina.py` dá marginal zero para todo o catálogo de feitiços na referência porque a Conclusão de arma vence a escolha; isso não prova que Desorientar seja inútil fora dessa rotina.

## Sensibilidade e opções

A hipótese abaixo de aproveitamento é **ilustrativa, não frequência observada**. `u` é a fração do valor da rolagem convencionada que o primeiro teste do alvo realmente entrega. Refluxo supõe que o PE temporário seja gasto. Romper supõe que o deslocamento seja útil. Essas simplificações mostram a inversão de escolha; não convertem todos os efeitos numa utilidade universal.

| Premissa ilustrativa | Valor |
|---|---:|
| aproveitamento_u | 0.70 |
| ataques_aliados_expor | 2 |

<!-- inicio-contas-dominancia -->
| Grandeza | Fatias ou fração |
|---|---:|
| Desorientar se u do cenário | 0.435778 |
| Refluxo se o PE for gasto | 0.556496 |
| Romper se o movimento for útil | 0.428740 |
| u para empatar Refluxo | 0.893913 |
| u para empatar Romper | 0.688696 |
| Desorientar com TR adicional hipotético | 0.342397 |
| Expor em ataques aliados do cenário | 0.684793 |
<!-- fim-contas-dominancia -->

- **A. Manter as seis regras.** Se a primeira rolagem for plenamente valiosa, Desorientar fica em 0,6225 por acionamento e vence as outras duas opções de uma Condução por preço bruto. Com aproveitamento menor, a tabela mostra quando Refluxo ou Romper passa à frente. Conserva o catálogo diverso, mas a referência de rotina ainda escolhe as Conclusões de arma.
- **B. Exigir duas Conduções para Desorientar.** O preço por acionamento continua 0,6225; o acesso cai. Num roteiro isolado já publicado em `estocada-auditoria.md` (atacar em T1 e depois conjurar), tentativas médias de conclusão por cena caíram de 0,6666 para 0,2787 ao exigir duas Conduções. Esse roteiro não representa todos os jogadores nem prova que a regra ficaria equilibrada. A mudança iguala o requisito de Ancorar, Expor e Cortar, mas sacrifica uma opção simples do nível 11.
- **C. Acrescentar um TR a Desorientar.** Com a chance de falha de referência, o preço por acionamento cai ao valor calculado na tabela. Mantém o requisito de uma Condução e a abrangência, mas perde sua confiabilidade e exige escolher qual TR faz sentido. A Conclusão de arma ainda pode continuar mais atraente na rotina.
- **D. Fortalecer uma alternativa de grupo.** Permitir que Expor alcance os dois próximos ataques aliados leva ao teto calculado na tabela **se ambos ocorrerem no prazo e nenhum já tiver vantagem**. Torna Expor mais distinto, mas acrescenta contagem, pode falhar por falta de aliados e precisa de uma nova conta do pacote.

**Decisão após a análise:** conservar as regras. O preço escalar sugere preferência por Desorientar quando a próxima rolagem é útil, mas as funções das seis opções não são substitutas e a rotina de referência aponta um problema anterior: a escolha entre Conclusão de arma e de feitiço. Requisito novo ou fortalecimento só se justificam com uma meta explícita de frequência de escolha.
