# Bastião — correção do preço histórico de Fagulha

Conferido em 18/09/2026. Nota preparada na pasta de trabalho; o repositório e os arquivos de consulta não foram alterados.

## Resultado

**O preço corrigido de Fagulha é 2,04625984 fatias, ou 2,05 fatias arredondando ao final**, preservadas as premissas históricas da tabela que publica 4,08 fatias.

A mudança corrige a conta da habilidade antiga. A habilidade reformada chama-se **Retaliação** e já aplica a chance de acerto; sua conta continua em **2,10 fatias** na referência adotada pela reforma.

## Fonte e premissas

O texto e a decomposição do preço vêm de [DESENHO-trilhas.md, linha 800](</media/mizuki/HD Externo II/Claude/Claude 2/DESENHO-trilhas.md:800>). A regra de mesa também aparece no [capítulo de Caminhos e Trilhas, linha 158](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/35-caminhos-e-trilhas.md:158>).

- Dano bruto do Classe 0 no nível 30: **27**.
- Uma fatia: **5,08 de dano por rodada**.
- Rodadas em que o personagem usa a Ação de Atacar e pode lançar o Classe 0: **56%**, frequência usada na conta publicada.
- Acerto de referência histórico: **50%**.
- Pelo menos um acerto em dois socos: **75%**; esse é o gatilho da vantagem no feitiço.
- Acerto do feitiço com vantagem, nessa base: **75%**, ganho de **25 pontos percentuais** sobre o acerto normal.

**Lançar o Classe 0 não exige acertar um soco.** Acertar um soco concede vantagem. Essa diferença separa a parcela base da parcela condicional.

## A conta corrigida

| Parcela | Conta em dano por rodada | Dano por rodada | Fatias |
|---|---|---:|---:|
| Classe 0 na Ação Bônus | 27 × 0,50 × 0,56 | 7,560 | 1,48818898 |
| Ganho da vantagem após um soco acertar | 27 × 0,25 × 0,75 × 0,56 | 2,835 | 0,55807087 |
| **Total** | Soma das parcelas | **10,395** | **2,04625984** |

Na base, faltava aplicar o acerto do feitiço. Na vantagem, a conta publicada multiplicava o dano bruto por 0,50; o ganho correto é de 0,25 de probabilidade. O aumento relativo de 50% que a vantagem dá a um acerto de 50% deve incidir sobre o dano já ajustado pelo acerto.

**As duas parcelas estavam duplicadas nessa base.** A reprodução das fórmulas impressas, antes de reduzir suas casas decimais, dá 4,09251969 fatias. A tabela publica as parcelas como 2,97 e 1,11, somando 4,08.

## Por que a retomada citava outros valores

- **2,04 fatias** é metade do valor publicado de 4,08. Recalcular a partir das premissas e arredondar apenas no final dá **2,05**.
- **1,99311024 fatias**, impresso como 1,99 no `conferir-dano-movido.py` do zip, vem de `27 × 0,50 × 0,75 ÷ 5,08`. Esse atalho usa 75% como frequência de lançamento e não inclui a parcela de vantagem. Ele não reproduz a decomposição histórica de Fagulha.
- A linha de Fagulha no script do zip é uma impressão, não uma regressão comparada à tabela original. O resultado `TUDO OK` não valida essa decomposição.

## Conferência independente

[conferir-fagulha.py](</home/mizuki/CHAT-GPT/RPG -JJK/conferir-fagulha.py>) enumera as combinações de dois dados de ataque dos socos e dois dados do feitiço. Sem vantagem, só o primeiro dado do feitiço conta.

Em **160.000 combinações**, o feitiço acerta em **110.000**: **68,75%** nas rodadas elegíveis. Multiplicar essa probabilidade por 27 de dano e pela frequência de 56% produz os mesmos **10,395 de dano por rodada**, ou **2,04625984 fatias**. O script também rejeita a conta histórica sem a correção como resultado válido.

## Escopo da correção

Esta é uma correção isolada do fator de acerto. Mantém o dano médio e a frequência histórica; não inclui dano adicional de críticos, resistências, sobreposição de vantagem ou competição pela Ação Bônus. Atualizar simultaneamente o acerto para 55% ou recalcular a frequência a partir de um dia de 10,5 rodadas produziria outra revisão, com outras premissas.

O total da Brasa antiga não foi reaprovado aqui: o documento contém tabelas de total de versões diferentes e outras entregas que precisam de conferência própria. O orçamento da reforma não é substituído pelo preço de Fagulha.

## Correção editorial preparada

Na tabela histórica de Fagulha, usar **1,49 fatia** para a parcela base e **0,56 fatia** para o ganho condicional da vantagem, totalizando **2,05 fatias**. Manter a regra de mesa. Atualizar as remissões ao preço de 4,08 apenas quando a correção for aplicada ao material publicado e seus totais forem revistos.
