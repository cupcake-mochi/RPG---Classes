# Bastião — a escala virou decisão: com acerto

Decidido em 21/09/2026. Fecha a tensão que a revisão cética achou (achado 12) e que `bastiao-reforma/README.md` deixava pendente.

## O problema

O zip aplicava duas escalas na mesma reforma. Fagulha (correção em `bastiao-correcao-fagulha.md`) e Retaliação (Combatente Amaldiçoado, nível 2) já aplicavam 50% de acerto no Classe 0. Trocação Franca (Punho, nível 2) usava o soco cru — `11,50 × 0,75`, sem acerto. As três vêm da mesma lógica: um golpe ou feitiço que depende de rolagem, preçado dentro de uma reforma que precisa caber em 5,00 fatias por Trilha.

## O critério e a decisão

**Qual escala faz as duas Trilhas afetadas — Punho e Combatente Amaldiçoado — caberem melhor em 5,00 fatias.** Decisão do Mizuki.

| Trilha | peça | cru | **com acerto — adotado** |
|---|---|---:|---:|
| Punho | Trocação Franca (nv2) | 1,70 | **0,85** |
| Punho | total do Caminho | 4,45–5,12 | **3,60–4,27** |
| Combatente Amaldiçoado | Retaliação (nv2) | 3,62 | **2,10** |
| Combatente Amaldiçoado | total do Caminho | **7,03** | **5,51** |

Cru deixava o Punho quase exato (4,45–5,12) mas fazia o Combatente Amaldiçoado passar de 7,00 — mais que qualquer estouro já aceito no projeto, e destruía o "os três primeiros degraus somam 5,01" que o próprio zip registra como a Trilha cabendo em 5,00 pela primeira vez. Com acerto deixa o Punho com folga (3,60–4,27, sem quebrar nada) e mantém o Combatente Amaldiçoado no mesmo estouro que já estava aceito (5,51, igual ao publicado).

Conta em [`conferir-escala-bastiao.py`](conferir-escala-bastiao.py), saída completa em `escala-bastiao-contas.json`. Reaproveita a fórmula de acerto que `conferir-fagulha.py` já tinha para Retaliação — essa conta não mudou, só ficou confirmada como a escala vigente.

## O que muda de fato

Só Trocação Franca. Fagulha (2,05, `bastiao-correcao-fagulha.md`) e Retaliação (2,10, já publicado no zip) já estavam na escala agora adotada — não mudam de número, só deixam de ser um caso isolado.

**Trocação Franca cai de 1,70 para 0,85 fatia.** O nível 2 do Punho (Trocação Franca + soco na Reação) cai de 2,35 para 1,50. O total do Caminho cai de 4,45–5,12 para **3,60–4,27 de 5,00** — o Punho deixa de ser "a única que quase encosta em 5" e passa a ser a que sobra mais espaço, o oposto do que `bastiao-reforma/README.md` registrava.

## A divergência que fica declarada

O repositório principal, no `DESENHO-trilhas.md`, afirma que as nove Trilhas já fechadas lá medem botão **cru**: *"dano cru, como as nove Trilhas publicadas medem botão"*. A mesma peça já tinha corrigido o soco do Engate pra cru, antes do zip existir: *"O certo é `11,50 × 0,75 = 8,63`"*.

**Esta decisão vai contra essa convenção, de propósito, porque cru quebra o Combatente Amaldiçoado.** É uma exceção declarada — do mesmo jeito que o câmbio de PE não vale pro Bastião (`bastiao-reforma/README.md`). Quando isso for portado pro repositório principal, a peça 5 e o `DESENHO-trilhas.md` vão pedir essa exceção por escrito, com o motivo: a régua cru do repositório principal nunca foi calibrada contra uma Trilha que amarra Classe 0 e soco na mesma reforma de 5,00 fatias.

## Escopo

Não mexe em Muro nem em nenhuma outra peça do Bastião. Não reabre o `0,50` do Contra a Parede (nível 27), que continua número do Mizuki, não medido. Os totais de Punho e Combatente Amaldiçoado nesta peça substituem os publicados em `bastiao-reforma/README.md`; a atualização desse arquivo é o próximo passo.
