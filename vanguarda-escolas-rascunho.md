# Vanguarda — Escola de Arma simplificada

Versão de trabalho aprovada pelo autor em 18 de setembro de 2026, depois da apresentação da proposta e do exemplo de uso com katana, Guarda, Pressionar a Guarda e Derrubada. A reserva de 2,75 fatias para Sequência + Escola foi adotada; continua provisória como avaliação de equilíbrio. O nome do arquivo foi preservado para manter os links existentes. Nenhuma regra aprovada da Sequência ou arquivo do repositório de consulta foi alterado.

**Atualização de 19/09:** o autor retirou o teto de conduções e passou a encerrar a sequência ao errar uma condução, mantendo o prazo de dois turnos. As regras da Escola abaixo permanecem. Os valores numéricos desta conferência de 18/09 são históricos; os resultados com a continuidade nova estão em [Conclusão Dupla e revisão da Sequência](vanguarda-conclusao-dupla.md).

**Os números da regra vigente, medidos em 22/09.** Os de 18/09 continuam na tabela mais abaixo, e ficam porque o argumento deles é histórico — mas não são o preço de hoje. No mesmo cenário de referência (Yumi contra Defesa 20, disponível desde o primeiro turno):

| Uso | Sem Escola | Com Precisão | Acréscimo | Com Versado | Acréscimo |
|---|---:|---:|---:|---:|---:|
| 18/09 — teto de duas, erro não encerra | 1,4865 | 1,5960 | 0,1095 | 1,9310 | 0,4445 |
| **vigente — sem teto, erro encerra** | **1,2621** | **1,3869** | **0,1248** | **1,7770** | **0,5149** |

Os três valores da linha vigente saem do `vanguarda-contas-v3.json`, sem conta nova: `sequence_without_school.sem_nivel_30.net_slices` dá o 1,2621, `profiles.yumi_referencia` dá o 1,3869 e `profiles.yumi_versado` dá o 1,7770. **Perturbando as duas regras uma de cada vez, o teto é inerte neste perfil** — quem move o número é errar-encerra, sozinho.

**A margem da reserva cai junto:** 0,75 − 0,5149 = **0,2351**, e não os 0,3055 que a seção do orçamento abaixo ainda calcula sobre o 0,4445.

## Orçamento adotado

| Parte | Fatias reservadas |
|---|---:|
| Sequência de Combate, conforme registro vigente | 2,00 |
| Escola de Arma, nesta versão reduzida | 0,75 |
| Total reservado para a base | **2,75** |
| Saldo das cinco fatias do Caminho | **2,25** |

Os 0,75 são uma reserva provisória de projeto, não uma média observada nem um preço exato demonstrado para todas as interações. O ataque extra continua com o tratamento de correção de base. As antigas habilidades posteriores do Caminho não entram gratuitamente. Trilhas continuam com orçamento separado.

## Regra comum

Escolha uma categoria de arma. Também é possível escolher golpes desarmados como especialização própria, sem equipará-los à categoria Manopla. A categoria escolhida determina sua Manha pela tabela abaixo.

**Ao acertar a Abertura com essa categoria, você pode aplicar sua Manha, uma vez por sequência e no máximo uma vez por turno.** A Manha é resolvida depois do dano da Abertura e de sua redução normal. Não exige ação nem PE adicional; não dispara em conduções, conclusões, ataques comuns ou aberturas que errem.

Não é possível reabrir uma sequência ainda ativa para repetir a Manha. Permanecem as regras de encerramento e a proibição de reabrir no turno em que se concluiu. Acertar uma Abertura que termine com zero de dano continua suficiente.

As categorias agrupadas compartilham a mesma Manha; a escolha ainda é de uma categoria, não de todas as categorias da linha. Todos os nomes abaixo são funcionais e provisórios.

| Categorias | Manha | Efeito na abertura acertada |
|---|---|---|
| Lâmina Curta, Arremesso, Yumi, Balestra ou Arma de Fogo | Precisão | Recebe +1 no próximo ataque com a categoria escolhida contra o alvo da sequência. Consome o bônus mesmo se errar. O bônus expira se a sequência terminar antes desse ataque. Não melhora a margem crítica. |
| Lâmina Longa ou Manopla; golpes desarmados como escolha adicional | Guarda | Recebe +1 de Defesa até o começo do seu próximo turno. Não acumula consigo mesmo. Inclui Bloquear, sem contar o mesmo bônus duas vezes. |
| Massa, Porrete, Machado ou Armas Longas | Impacto | O alvo faz TR Físico; na falha, você pode empurrá-lo até 3 m para longe de si. |
| Ceifa ou Flexível | Desvio | O alvo faz TR Físico; na falha, você pode deslocá-lo até 1,5 m em uma direção à sua escolha. |

A CD das duas Manhas com resistência é 8 + atributo usado no ataque + maestria. Um sucesso no TR impede apenas a Manha; a Abertura continua válida. O deslocamento respeita obstáculos, espaços ocupados e as regras gerais de movimento forçado; a Manha não aumenta o alcance da arma.

Guarda não é um efeito sustentado de Conduzir: trocar de condução não a apaga. Ela dura até o começo do próximo turno, inclusive se a sequência terminar antes. Seu +1 pode somar ao +1 de Proteger o Avanço; o modelo conserva essa interação. Precisão pode somar a Pressionar a Guarda, mas continua valendo para apenas um ataque.

## Versado, como alternativa

Em vez de escolher uma categoria e sua Manha, pode escolher Versado.

**Imediatamente depois de acertar uma Abertura, pode guardar uma arma que esteja empunhando e sacar outra sem gastar ação. Uma troca por sequência, no máximo uma por turno.** Pode abrir com qualquer arma elegível ou golpe desarmado; continua recebendo apenas Versado, sem as Manhas das categorias usadas.

A troca não oferece bônus de acerto, ataque adicional, recarga ou ativação de item. A sequência continua no mesmo inimigo. Usar a troca para passar de uma arma corpo a corpo para outra à distância não ignora os requisitos de cada condução ou conclusão.

A referência de Compasso, da Trilha Estocada, a quem escolheu Versado permanece reconhecendo esta opção: continua escolhendo um número de grupos igual à maestria. Nenhum benefício de Trilha foi incorporado à reserva da Escola. A interação de Compasso com a versão reformada ainda requer revisão junto da Trilha.

## O que esta proposta substitui

- As treze descrições diferentes de Manhas passam a quatro efeitos compartilhados e à alternativa Versado.
- Saem dano no erro, dano atrasado e atingir um segundo alvo.
- Saem Derrubado e redução de deslocamento nas Manhas. A Escola não satisfaz sozinha Explorar o Desequilíbrio ou Fixar o Alvo.
- Saem +2 de Defesa, bônus para todos os aliados e o bônus recorrente de acerto de Versado.
- Os benefícios da Escola passam a acompanhar a abertura; nenhum deles se repete em cada ataque ou condução.
- As seis conduções, sete conclusões e custos da Sequência ficam preservados. Após a atualização de 19/09, não há teto de conduções: erro encerra, e o prazo até o fim do segundo turno seguinte permanece.

## Conferência do acréscimo

A comparação usa a mesma simulação determinística da auditoria v2, acrescentando a Escola e permitindo que a política de uso se adapte ao benefício novo. Conta erros, resistência, PE, perda na Abertura e turnos em que a sequência não está disponível. A Escola desativada reproduziu o modelo anterior em todos os perfis e cenários comparados.

Exemplos compatíveis com o Batedor de Yumi da referência, contra Defesa 20:

| Uso | Sem Escola | Com Precisão | Acréscimo de Precisão | Com Versado* | Acréscimo de Versado* |
|---|---:|---:|---:|---:|---:|
| Disponível desde o primeiro turno | 1,4865 | 1,5960 | 0,1095 | 1,9310 | 0,4445 |
| Começa no segundo turno | 0,6255 | 0,7091 | 0,0836 | 0,9944 | 0,3689 |
| Segundo turno sem ataque elegível | 0,5753 | 0,6571 | 0,0817 | 0,9516 | 0,3763 |

Valores em fatias por rodada; não são somas de fatias ao longo de vários turnos. A coluna sem Escola é a entrega líquida do cenário, e não a reserva de projeto de 2,00. Por isso não se deve somar novamente aquela reserva às colunas que já mostram a entrega conjunta.

*Versado foi avaliado pelo deslocamento que a Ação de Movimento poupada permitiria: 12 m × 0,60 equivalente/m no perfil de Yumi, apenas quando a abertura acerta. Essa é uma situação favorável de aproveitamento integral do gesto. O modelo não simula inventário, troca real entre perfis de armas, recarga ou outros usos dessa ação; logo, não demonstra que Versado nunca exceda esse acréscimo. Não há desconto de frequência de troca apresentado como se tivesse sido observado em mesa.

As outras Manhas também foram instrumentadas para inspeção, cruzando cada efeito com os mesmos perfis como comparação abstrata. Esse cruzamento não autoriza Manhas incompatíveis com a arma. Os valores convencionais são +1 Defesa = 3,39 equivalentes e movimento = 0,60 equivalente/m, com acerto e TR aplicados quando cabíveis. Não se presumiu que mover um inimigo elimina uma ação inteira ou todos os seus ataques.

Os efeitos de posição não têm equivalência completa nessa régua: deslocar lateralmente alguém, abrir passagem e empurrar em terreno relevante não são iguais a dano. As quatro Manhas não estão certificadas como escolhas de força idêntica. O rascunho controla o orçamento do conjunto; a atratividade de cada opção permanece assunto de revisão e uso em mesa.

Reservar 0,75 deixa 0,3055 acima do maior acréscimo dos exemplos compatíveis da referência — **número de 18/09; sob a regra vigente a margem é 0,2351, ver o bloco no topo deste arquivo**. Essa margem é deliberada, não calculada como uma entrega adicional. No teste extremo já existente, Versado acrescentou 0,4664 ao valor anterior de 4,8953; o extremo continua fora do orçamento nominal. Portanto, **2,75 é o orçamento adotado para avançar, não um teto universal comprovado**.

Esta proposta evita reduzir PE ou a perda de dano para financiar as Escolas. Nenhum novo uso gratuito das conclusões é concedido. O resultado completo da conferência está em `vanguarda-escolas-contas.json`, nesta mesma pasta autorizada.
