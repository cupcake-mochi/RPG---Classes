# bastiao-reforma — a fonte do Bastião reformado

Este é o zip que saiu da conversa de **17/09/2026** que reformou o Bastião inteiro — o Caminho e as três Trilhas (Muro, Punho, Brasa). O repositório principal estava na v0.239. **Ele é mais velho que os dois arquivos de Bastião da raiz** (`bastiao-nomes-aprovados.md` e `bastiao-correcao-fagulha.md`, de 18/09), que fecham os dois primeiros itens da fila dele. **Onde os dois discordarem, a raiz vence.**

Leia `LEIA-PRIMEIRO.md`, depois `reforma-caminhos-continuidade.md`. O `conferir-dano-movido.py` reproduz cada número dos dois; saiu `TUDO OK` em 21/09/2026. A pasta `contas/` são os scripts de cada rodada de decisão, pra conferência.

## O que a raiz atualizou por cima deste zip

**Os onze nomes — item 1 da fila do zip — fecharam em 18/09**, e mais dois que o zip dizia que ficavam:

| Onde | No zip | Na raiz (vale) |
|---|---|---|
| Caminho 2 | Encarar | **Olhos Em Mim** |
| Caminho 7 | Não Pega · Ainda de Pé | **Nem Um Arranhão** · Ainda de Pé |
| Caminho 15 | Aparar com Corpo | **Duro de Matar** |
| Caminho 23 | sem nome | **Chega Mais** |
| Caminho 30 | Passa Pra Mim | Passa Pra Mim |
| Muro 2 · 11 · 19 · 27 | Alicerce · sem nome · sem nome · sem nome | Alicerce · **Guarda-Costas** · **Casca Grossa** · **Inabalável** |
| Punho 2 · 11 | Engate · Encontrão *("ficam")* | **Trocação Franca** · **Mão Pesada** |
| Punho 19 · 27 | sem nome · sem nome | **Minha Vez** · **Arrastão** |
| Trilha Brasa | Brasa | **Combatente Amaldiçoado** |
| Combatente 2 · 11 · 19 · 27 | sem nome ×4 | **Retaliação** · **Embalo** · **Oportunista** · **Contra a Parede** |

A mecânica de cada uma é a do zip — a tabela de nomes da raiz reescreve cada uma por extenso e confere. Os dezoito nomes passaram no `conferir-nomes.py` do repositório principal em 20/09 (ver `revisao/`).

**Fagulha — item 2 da fila — fechou em 18/09:** `bastiao-correcao-fagulha.md` dá **2,05** fatias, com o mesmo raciocínio do zip (o Classe 0 resolve por acerto e nunca tinha levado os 50%). O zip dizia "~2,04" e o validador imprime 1,99 por um atalho que a raiz explica.

## O que este zip decide pro sistema inteiro, e que o porte vai ter que escrever

- **Orçamento do Caminho: 5,00 fatias, em quatro degraus pagos — níveis 2 · 15 · 23 · 30.** O nível 7 é grátis, correção de base. Isso substitui o `DESENHO-caminhos.md` do repositório principal (3 fatias, níveis 2 · 15 · 30). Confirmado pelo Mizuki em 21/09 que vale pros cinco Caminhos.
- **O nível 7 do Bastião fica com ataque extra + Não Pega + Ainda de Pé, a 0,00.** A peça 6 do principal preça Não Pega em 1,18 *na Vanguarda* e Ainda de Pé em 1,10; as duas linhas envelhecem.
- **Provocar entra no lugar de Intimidação como perícia fixa do Bastião.** Toca o manual publicado.
- **Uma constante nova: 1 ponto de dano movido = 0,30 de dano causado.** Provisória, decidida, não medida. O `RASCUNHO-dano-movido.md` é o rascunho dela; sem ela o Bastião não tem preço, e com ela passam a ter o Ninguém Cai do Guia e o Escudo de Osso do Evocador.
- **O câmbio de 1 PE = 5,14 não se aplica ao Bastião**, porque o PE dele não compete com nada.
- **Retaliação (nível 2) soma Força ao PE máximo — exceção declarada contra a peça 1 §5.3 em 21/09**, junto com o Compasso da Estocada, que faz a mesma coisa. Ver [`excecao-atributo-no-pe.md`](../excecao-atributo-no-pe.md).

## Os preços, como o zip fechou

| Peça | Fatias | Observação |
|---|---:|---|
| Caminho | 5,20 a 5,58 | estouro declarado pelo Mizuki; a faixa é o Duro de Matar (15), que depende de quantas vezes o Bastião falha um Bloquear |
| Muro | 5,39 (4,79 a 6,46) | a largura toda é o Guarda-Costas (11) |
| Punho | 3,60 a 4,27 | escala corrigida em 21/09; a única com folga clara, ver `bastiao-correcao-escala.md` |
| Combatente Amaldiçoado | 5,51 | os três primeiros degraus somam 5,01; o Contra a Parede (27) está em 0,50 por decisão do Mizuki, medido 0,32 a 5,42 |

## O que continua aberto, na ordem do próprio zip

3. **Uma linha de playtest**: quantos ataques são mirados no Bastião por rodada e quantas vezes ele falha um Bloquear. Fecha o Duro de Matar, o Minha Vez e o Contra a Parede de uma vez.
4. **Uma linha na peça 19**: o Incapacitado preçou "não pode Bloquear" em zero porque Bloquear é neutro; pro Bastião deixou de ser.
5. **Fechar a taxa de dano movido como peça** — dono, validador com teste negativo, os seis refinos da seção 7 do rascunho.
6. **Repreçar com ela** Ninguém Cai, Escudo de Osso, Puxar Para Si e Segurar.
7. Os outros quatro Caminhos — a Vanguarda é o que a raiz deste repositório fez em 18 e 19/09.
8. Recalibrar o Bestiário contra a proporção nova (32,4%).

~~E uma tensão que a revisão de 21/09 achou lendo o zip: ele aplica 50% de acerto ao Classe 0 de Fagulha, mas preça o soco da bônus do Engate/Trocação Franca cru, sem os 50%. Mesma reforma, duas escalas.~~ **Resolvido em 21/09: com acerto, nas três — Fagulha, Trocação Franca e Retaliação.** O critério foi qual escala cabe melhor em 5,00 nas duas Trilhas que a tensão toca: cru levava o Combatente Amaldiçoado a passar de 7,00 fatias; com acerto ele fica em 5,51, igual ao que já estava aceito. Trocação Franca caiu de 1,70 pra 0,85; o Punho caiu de 4,45–5,12 pra 3,60–4,27. Fagulha e Retaliação não mudaram — já estavam nessa escala. Registro completo em [`bastiao-correcao-escala.md`](../bastiao-correcao-escala.md). **Isso diverge da convenção do repositório principal** (`DESENHO-trilhas.md`: "dano cru, como as nove Trilhas publicadas medem botão") — é exceção declarada, como o câmbio de PE que também não vale pro Bastião.
