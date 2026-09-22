# Vanguarda — nível 23: Persistência

Versão de trabalho fechada em 19 de setembro de 2026. **Persistência é nome provisório.** O autor aprovou o efeito, a quantidade vinculada à maestria e o fechamento, corrigindo expressamente o arredondamento para baixo. A recarga ocorre por descanso curto ou longo.

## Regra

Quando errar o ataque de uma Condução, você pode gastar um uso desta habilidade para impedir que esse erro encerre sua Sequência. Não exige ação nem PE adicional. Avalie o resultado final do ataque, depois de eventuais rerrolagens, antes de decidir.

Você tem **um número de usos igual à metade da sua maestria, arredondada para baixo, + 1**. Recupera todos os usos ao terminar um descanso curto ou longo.

Na progressão atual, são **dois usos na maestria 3 (níveis 23–25)** e **três usos na maestria 4 (níveis 26–30)**. Não há limite adicional de um uso por cena ou por sequência: cada erro que quiser preservar exige outro uso disponível.

- O ataque continua errado: não causa dano nem aplica o efeito da condução.
- O PE da tentativa continua gasto, e a tentativa não conta como condução acertada.
- **O prazo não é renovado.** A sequência conserva o vencimento no fim do segundo turno próprio após o último Golpe Inicial acertado ou a última Condução acertada. A habilidade não impede esse vencimento.
- Se trocou de condução antes do ataque, os efeitos encerrados pela troca não voltam.
- A tentativa ocupa a condução permitida naquele turno. Não recebe outro ataque nem outra etapa da sequência.
- Só preserva uma sequência ainda ativa. Não recupera uma sequência expirada ou concluída.
- Um erro para o qual não gastar um uso continua encerrando a sequência normalmente.

**Exemplo:** você já acertou uma condução e erra a tentativa seguinte. Gasta um uso e mantém uma condução acertada, dentro do prazo anterior. Ainda precisa acertar outra para habilitar Conclusão Dupla. Se o prazo terminar antes disso, a sequência se encerra mesmo que ainda tenha usos de Persistência.

## Escolha dos usos

A maestria mantém a disponibilidade igual entre construções do Vanguarda. Vincular ao atributo principal favoreceria o investimento nesse atributo e exigiria decidir qual atributo conta para cada arma ou construção híbrida. O descanso curto permite concentrar os usos em um combate difícil ou distribuí-los entre combates, sem recarga automática ao trocar de cena.

O contador substitui a proposta anterior de um uso por cena. Os demais efeitos e limites foram preservados, incluindo a regra geral de erro encerrar a sequência e o prazo de dois turnos.

## Conferência de orçamento

Compararam-se zero, um, dois e três usos disponíveis no começo de cada combate, com e sem Conclusão Dupla. **Isso é uma disponibilidade generosa para a versão por descanso curto:** se não houver descanso entre combates, os usos são compartilhados. Não se assumiu que tais descansos efetivamente ocorram nem se mediu sua frequência em mesa.

A régua continua avaliada no nível 30, com fatia de 5,08 equivalentes por rodada, PE a 5,14 e os mesmos perfis da auditoria anterior. Os valores são marginais, incluem erros, PE gasto, requisitos, prazo e sequências incompletas. Não representam três ativações garantidas em cada cena.

**Correção de arredondamento:** arredondar para baixo reduz a disponibilidade nos níveis 23–25 de três para dois usos. No nível 30, a maestria 4 continua concedendo três usos; por isso, a conta abaixo e a reserva de orçamento permanecem válidas sem mudança numérica. A comparação de dois usos no modelo anterior também é preservada, mas continua usando a ficha de nível 30, não uma simulação completa do nível 23.

| Cenário | Nível 23 sem o 30, três usos | Nível 23 quando o 30 já está presente, três usos |
|---|---:|---:|
| Referência de três/quatro turnos | **0,2091** | **0,2543** |
| Começa a sequência no segundo turno | 0,0599 | 0,0599 |
| Segundo turno sem ataque elegível | 0,0079 | 0,0079 |
| Cobertura Parcial | 0,2404 | 0,2795 |
| Cobertura Boa | 0,1208 | 0,2595 |
| Sem requisito externo para Fixar | 0,0176 | 0,1341 |
| Versado | 0,1623 | 0,2087 |
| Referência com seis turnos | 0,1512 | 0,1573 |
| Referência com oito turnos | 0,1847 | 0,1852 |

Na referência curta com Conclusão Dupla, passar de um para três usos por combate leva o marginal de 0,2501 a 0,2543. Dois e três usos empataram nesse horizonte; isso não significa equivalência geral, como mostram os combates mais longos.

**Reserva de trabalho do nível 23: 0,25 fatia.** É uma alocação provisória, não um teto universal do efeito. Para distribuir a interação sem cobrá-la duas vezes, a referência em ordem de progressão é:

- Nível 23 antes de adquirir o 30: 0,2091.
- Nível 30 depois de adquirir o 23: 0,8395.
- Acréscimo conjunto: **1,0487**, dentro da reserva conjunta de 1,25.

| Parte do Caminho | Reserva |
|---|---:|
| Sequência | 2,00 |
| Escola de Arma | 0,75 |
| Não Cede, sem +1 | 1,00 |
| Persistência, nível 23 | 0,25 |
| Conclusão Dupla, nível 30 | 1,00 |
| **Total** | **5,00** |

Os limites anteriores continuam: condições usam conversões simplificadas, os cenários não possuem frequências observadas, e a atratividade das conclusões corpo a corpo ainda merece revisão. No extremo de Defesa 14 com falha de 85% nos dois TRs, os níveis 23 e 30 juntos acrescentam 1,7559; a recuperação contribui apenas 0,0090 antes do 30. A revisão de usos não elimina esse resultado favorável à Conclusão Dupla.

Reprodução: `conferir-vanguarda-nv23-usos.py` e `vanguarda-nv23-usos-contas.json`. O teste com um uso reproduziu a conta histórica; foram conferidos o limite de usos, PE sem reembolso, prazo preservado e ausência de conduções acertadas fictícias. Os arquivos históricos de um uso por cena foram preservados para comparação.
