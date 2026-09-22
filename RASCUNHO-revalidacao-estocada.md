# Estocada — revalidação de Compasso e da escolha de feitiço para Bote

Análise de 22/09/2026, **sem mudança de regra**. Esta conta corrige a apresentação do preço de Bote: o antigo acréscimo de 3,50 fatias à distância mantinha o mesmo feitiço nos dois lados. Era o ganho dos ataques se os sete feitiços já fossem de condição sem dano e tivessem valor equivalente ao que seria conjurado sem Bote. **Não era o preço líquido de escolher esses feitiços no lugar de feitiços de dano.**

## Por que as duas armas diferem tanto

A referência à distância é Yumi com vantagem no ataque de arma e acesso a Fixar; a referência corpo a corpo é Lâmina Longa sem essa vantagem nem Fixar. São **duas fichas diferentes**, não uma taxa inerente à distância.

| Parcela de Compasso, sete conjurações | Distância | Corpo a corpo |
|---|---:|---:|
| Chance de acerto do ataque de arma | 87,75% | 55,00% |
| Dano esperado de um ataque, contando erro e crítico | 22,91 | 15,07 |
| Sete ataques da ação bônus, em fatias | 3,01 | 1,98 |
| Sequência, Escola, Persistência e Conclusão Dupla recuperadas por esses ataques | 3,48 | 0,35 |
| **Compasso, só os ataques** | **6,49** | **2,32** |

Os ataques adicionais à distância acertam mais e dão mais oportunidades de preparar e encerrar a Sequência, inclusive com Fixar. Como sensibilidade, retirar só a vantagem da ficha à distância reduz Compasso de 6,49 para **3,89**; retirar só o acesso a Fixar reduz para **4,61**. Portanto, o valor alto é dependente da ficha de referência. A troca de atributo da arma ainda não tem preço isolado.

## Bote contra o feitiço de dano que se deixa de escolher

No nível 30, o Fundamento publica **21d8** de dano cheio para um feitiço comum de Classe 7 em um alvo. A média exata dos dados é 94,5 (a tabela arredonda para 94). Com o acerto e o crítico das fichas usadas aqui, isso vale **66,15 equivalentes por conjuração à distância** e **56,70 corpo a corpo**. Ambos os lados gastam a mesma ação padrão, os mesmos 21 PE e mantêm o primeiro ataque de Compasso.

O outro feitiço precisa ser **de condição e não causar dano** para habilitar Bote. Como o valor do controle depende da condição escolhida e de seu alvo, a tabela varia seu benefício esperado por conjuração. Em cada luta o modelo escolhe quando usar Bote e compara o melhor feitiço disponível **com e sem** a habilidade. Os números são ganhos **incrementais de Bote**, não o valor dos feitiços em si.

<!-- inicio-contas-troca-feitico -->
| Valor esperado do feitiço de condição sem dano | Bote: distância | Usos/dia | Bote: corpo a corpo | Usos/dia |
|---|---:|---:|---:|---:|
| 0 | 0,076 | 0,500 | 0,000 | 0,000 |
| 20 | 0,263 | 0,500 | 0,000 | 0,000 |
| 40 | 0,451 | 0,500 | 0,016 | 0,500 |
| 50 | 1,383 | 7,000 | 1,215 | 7,000 |
| Igual ao feitiço de dano | 3,502 | 7,000 | 2,094 | 7,000 |
<!-- fim-contas-troca-feitico -->

Quando o controle vale zero, escolher os sete feitiços sem dano é ruim: Bote fica em **0,076 fatia à distância**, ativado em média apenas 0,5 vez no dia, e **zero corpo a corpo**. Mesmo nesse caso o otimizador à distância acha uma oportunidade rara em que o segundo ataque fecha uma Sequência valiosa. Os **3,50 / 2,09** anteriores reaparecem somente quando o feitiço de condição, por si, vale tanto quanto o feitiço de dano e Bote fica elegível em todas as sete conjurações. Entre os extremos, o ganho depende do controle. Como um personagem sem Bote também pode escolher o feitiço de condição, seu valor próprio nunca deve ser cobrado como benefício de Bote.

O modelo mantém separados o efeito próprio do feitiço e os ataques: não simula uma condição do feitiço melhorando os acertos seguintes, nem a interação com uma Conclusão de feitiço ou Ferrão. Portanto, esta é uma revalidação da **escolha dano versus controle**, não o preço fechado da Trilha.

## PE e o limite de 5,50 fatias

As sete conjurações de Classe 7 custam **147 PE**. O modelo anterior permite Conduções sem um teto de PE por dia, e a ficha à distância com Compasso gasta em média **20 PE adicionais** nelas. **Sem descanso curto**, 150 PE da Vanguarda, ou 156 após o bônus de Compasso, não sustentam essa rotina; o valor de 6,49 não vale para um dia sem descanso. Uma otimização com penalidade de PE dá **5,427 fatias como limite superior de Compasso sozinho** nesse dia sem descanso e com os seis PE adicionais, antes de reavaliar Bote.

**Com pelo menos um descanso curto**, a rotina de referência é viável: 150 + 37 = 187 PE disponíveis, enquanto sete conjurações e até uma Condução em cada uma das doze rodadas custariam no máximo 147 + 36 = **183 PE**. Se o descanso ocorrer após a segunda luta, antes dele cabem no máximo cinco conjurações e oito Conduções: 105 + 24 = **129 PE**. O dia publicado tem três lutas e a régua de recuperação prevê descanso entre elas. Nesse cenário, **Compasso sozinho continua em 6,49 fatias à distância**, acima de **5,50** mesmo antes de somar qualquer valor de Bote ou o PE máximo extra. Com dois descansos, o PE extra oferece até **0,964 fatia nominal**, se for recuperado e gasto; não é benefício garantido.

**Decisão de orçamento ainda aberta:** a ficha à distância de referência ultrapassa 5,50, mas o valor final da Trilha depende do feitiço de condição escolhido, da presença de descansos e das conclusões de feitiço. Nenhum limite de uso ou mudança de habilidade foi adotado nesta análise.

Reprodução: `python3 conferir-estocada-troca-feitico.py`. O script lê os dados do Classe 7 no Fundamento, recompõe Compasso no Caminho completo, recupera o teto anterior de Bote quando os feitiços têm valor igual e confere a tabela acima. A saída detalhada é `estocada-troca-feitico-contas.json`.

**Conferência:** 19 validadores passaram em cópia isolada. Em outras cópias, alterar os dados do feitiço no Fundamento, um valor de controle do cenário ou um número publicado fez a conferência falhar; os dois primeiros também mudaram o resultado recalculado. Os arquivos de referência foram preservados no repositório de trabalho.
