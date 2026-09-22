# A régua do Caminho: cinco fatias e degrau no nível 23

> **Veio da branch `claude/jjk-classes-review-g21rh1` (commit `e11a5f0`, 21/09 às 19:53), trazido pro `main` em 22/09.** Aquela branch saiu do commit `b29f238` e nunca voltou; o `main` seguiu por outro caminho e fechou o mesmo item 1 sem o argumento que está aqui. O texto abaixo é o original, sem uma palavra mexida — **três trechos dele envelheceram entre 19:53 e a noite do mesmo dia**, e é só isso:
>
> - **"A releitura da Vanguarda, medida, custa 3,2529 fatias… Sobram 1,7471 sem alocar"** (seção *O que isto não resolve*) é o número **líquido**. Na mesma noite o Mizuki decidiu contar o PE **bruto**: o perfil de distância mede **5,07** e o saldo não alocado é **0,00**. Dono: [`vanguarda-orcamento.md`](vanguarda-orcamento.md).
> - **"O Bastião continua sem número nenhum"** e **"`Olhos Em Mim` não existe em arquivo nenhum, só na tabela de nomes"** caíram os dois. O zip de 17/09 entrou no `main` às 21:37 e o consolidado às 22:44: o texto de regra do `Olhos Em Mim` e os preços das cinco entregas (2,46 · 0,00 · 2,12–2,50 · 0,00 · 0,62, total **5,20 a 5,58**) estão em [`bastiao-completo.md`](bastiao-completo.md) e em [`bastiao-reforma/`](bastiao-reforma/).
> - **"A Sequência de Combate mede 0,0000 fora de uma montagem"** continua de pé, e ficou pior: o achado da noite mostrou que os 5,07 e os 1,34 foram medidos numa Vanguarda que **nunca conjura**. Na régua do repositório principal, 7 de 10,5 rodadas, o Caminho cai pra **1,09** sem Compasso. Quadro em [`vanguarda-completo.md`](vanguarda-completo.md).
>
> **O que este arquivo tem e nenhum outro tem** é o *motivo* do degrau do 23 — e o aviso de que ele **reverte uma decisão registrada** do repositório principal (*"o vão fica, e é preço aceito e não defeito"*, `referencia-jjk-project/sistema/03-mecanica/RASCUNHO-trilhas.md`). Mais a lista de porte com arquivo e linha, o contra-teste dos degraus 22 · 23 · 24, e a vaga de nível 23 vazia no Guia, no Emanador e no Evocador.


Decidido pelo Mizuki em 21/09/2026, fechando o item 1 da fila de abertos.

Este arquivo existe porque a revisão de 20/09 achou que a releitura da Vanguarda distribuía cinco fatias e criava um nível 23 **sem que a mudança de régua estivesse escrita em lugar nenhum**. Estava só suposta, numa linha de "referências da reforma" da auditoria v2. Agora está escrita.

Nada disto foi aplicado ao JJK---Project. Continua sendo proposta — a diferença é que agora ela é uma proposta com dono e com motivo.

## O que ficou decidido

**O Caminho leva 5 fatias, e os degraus são `2 · 7 · 15 · 23 · 30`.** O nível 7 continua de graça, porque continua sendo correção de base. Então são **quatro degraus pagos**, contra três de antes.

**Vale para os cinco Caminhos**, não só para os dois reformados. Bastião, Vanguarda, Guia, Emanador e Evocador ganham as duas fatias e a vaga nova juntos.

Fatia aqui é a unidade de sempre: 5,08 de dano por rodada no nível 30. A Trilha não muda — continua em 5 fatias e `2 · 11 · 19 · 27`.

## O motivo já estava medido, e não é o orçamento

O argumento fácil seria "três fatias apertavam". Ele não se sustenta, e é melhor dizer isso agora do que alguém descobrir depois.

Nenhum dos cinco Caminhos foi preçado contra as três fatias. O próprio `DESENHO-caminhos.md` escreve a dívida. O único que chegou perto é o Guia, com dois degraus derivados de três — e nele **sobra** 1,26 fatia. Ninguém nunca bateu no teto de três.

O motivo de verdade é outro, e é o buraco na escada.

O calendário de Caminho era `7 · 15 · 23 · 29` até a v0.70. O desenho dos cinco Caminhos moveu para `2 · 7 · 15 · 30` sem refazer a conta que tinha escolhido o calendário antigo. Quando refizeram, na v0.71, o resultado foi: **o maior vão entre duas entregas de qualquer tipo passou de 5 para 8 níveis, e a pior seca de 24 para 31 missões — as duas por causa do degrau do 23 que saiu.** O Mizuki decidiu na época que o vão ficava, como preço aceito.

Essa decisão está sendo revertida aqui, e o número que ela custava volta ao que era.

| calendário | maior vão | onde |
|---|---:|---|
| antigo, até a v0.70 — Caminho em `7 · 15 · 23 · 29` | 5 | entre o 2 e o 7 |
| atual, da v0.70 em diante — Caminho em `2 · 7 · 15 · 30` | **8** | entre o 19 e o 27 |
| com o 23 de volta — Caminho em `2 · 7 · 15 · 23 · 30` | 5 | entre o 2 e o 7 |

Hoje um personagem passa do nível 19 ao 27 — sete níveis — sem receber nada nem do Caminho nem da Trilha. Um degrau no 23 parte esse trecho em quatro e quatro, e o gargalo volta a ser o 2 para o 7, que é onde ele estava quando o calendário foi escolhido.

A conta está em [`revisao/vao-do-nivel-23.py`](revisao/vao-do-nivel-23.py). Ela reproduz os dois números publicados (vão 5 e vão 8) antes de dizer qualquer coisa sobre o calendário novo — sem isso a comparação não valeria. A seca em missões não foi reproduzida: o modelo dela não veio na cópia de referência, então os 24 e os 31 estão citados, não conferidos.

**O 23 não é o único nível que fecha o buraco.** Um degrau no 22 ou no 24 também derruba o vão para 5. O 23 é o único que parte o trecho ao meio, e é o que o sistema já tinha antes da v0.70. O 22 já é marco, o que faz dele o mais cheio dos três.

## Onde o repositório principal diz outra coisa

Lista completa do que precisa mudar, com o arquivo e a linha. Decisão registrada não é decisão aplicada, e esta aqui termina em cinco lugares.

| onde | o que diz hoje |
|---|---|
| `DESENHO-caminhos.md`, linha 5 | *"Caminho em `2 · 7 · 15 · 30` … **O Caminho leva `3` fatias** (níveis 2, 15 e 30)"* |
| `sistema/ESTADO-ATUAL.md`, linha 994 | *"a fatia é `5,08`, o Caminho leva `3` fatias e a Trilha leva `5`"* — **citação da revisão, não conferida aqui**: o `ESTADO-ATUAL` ficou de fora da cópia de referência de propósito, e a revisão leu a v0.261 enquanto a cópia é da v0.263. O número da linha pode ter andado. |
| `sistema/03-mecanica/18-progressao.md`, linha 60 | nível 23, coluna "o que acontece": `—` |
| `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md`, "Entregas por nível" | a lista vai de 19 direto para 27 |
| `sistema/03-mecanica/06-caminhos-e-trilhas.md`, linhas 145 e 466 | *"o desenho dos cinco Caminhos o moveu para `2 · 7 · 15 · 30`"*, e o calendário fechado na v0.55 e v0.60 |

Fora dessas, tem duas que **descrevem** a régua sem serem donas dela, e envelhecem junto: `sistema/03-mecanica/RASCUNHO-trilhas.md` linhas 122 e 240, e `05-caminho-e-combate-sem-feitico.md` linha 219.

Não dá para saber daqui se algum validador do principal confere o número de fatias ou o calendário. Os `conferir-*.py` de lá não estão na cópia de referência. O porte tem que rodar todos, inclusive os dois de `manual/matematica/`, e conferir `PULADA=0`.

## O que isto não resolve

**Três Caminhos ficaram devendo uma entrega de nível 23.** Guia, Emanador e Evocador ganharam a vaga e não têm nada para pôr nela. Só a Vanguarda (Persistência) e o Bastião (Chega Mais) têm candidata.

**Cinco fatias é teto, não valor.** A releitura da Vanguarda, medida, custa 3,2529 fatias — 1,3869 da Sequência com a Escola, 0,8173 do Não Cede, 0,2091 da Persistência, 0,8395 da Conclusão Dupla. Sobram 1,7471 sem alocar. Isso é subtração, igual ao 1,26 do Guia: escrever como preço seria inventar entrega que ninguém mediu.

**O Bastião continua sem número nenhum.** As cinco entregas dele não têm preço nesta pasta nem no principal, e o nível 2 trocou de mecânica inteira — `Olhos Em Mim` é a área de Provocar, não é o `Absorver` de 1,60. Essa mecânica não existe em arquivo nenhum, só na tabela de nomes. A régua nova dá espaço para ele; não dá conta.

**A Sequência de Combate mede 0,0000 fora de uma montagem.** Nos JSON da própria pasta, `lamina_longa`, `lamina_curta` e `estocada_hibrida` dão zero em todas as linhas contábeis — a política ótima nunca abre sequência. O 1,3869 que sustenta a reserva de 2,00 sai de um Batedor Yumi com o `Mirar` ligado, e o `Mirar` se perde se você se deslocar na rodada. Decidir o tamanho do orçamento não conserta isso; só dá mais espaço para a peça que ainda precisa de conserto.

## O que não foi medido

Nada aqui mede se as cinco fatias cabem. Ninguém mediu se as três cabiam. O que esta decisão tem de argumento é o vão da escada, que é conta de nível e não de dano.

Os três Caminhos que não foram reformados continuam com dois degraus preçados no total — os do Guia. Subir o teto deles de 3 para 5 não foi testado contra nada, porque não há contra o que testar.
