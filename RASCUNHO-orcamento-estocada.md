# Estocada — orçamento das rotinas e alternativas

**Resultado mais recente:** a [missão conjunta](RASCUNHO-revalidacao-estocada.md) inclui reserva de PE, descansos, conclusões e Ferrão. Na Yumi sem vantagem e com Fixar externo, sete Classe 7 medem 4,34–4,66 fatias com controle suposto equivalente ao dano. Com Classes livres e dois descansos, o cenário favorável chega a 6,861; o requisito de metade da Classe máxima arredondada para cima, aplicado a Compasso em 22/09, reduz para 6,860. A mudança não garante 5,50. As tabelas abaixo registram a comparação anterior, sem esse requisito e sem o livro-caixa conjunto.

**Correção de 22/09 sobre o commit `84ec7a2`:** esta tabela é um cenário histórico favorecido, não preço da Trilha. A ficha de Yumi incorporou vantagem, `+2` de Mirar e deslocamento do Batedor; Mirar e Compasso disputam a ação bônus. O modelo reinicia Persistência e Conclusão Dupla a cada combate e não acompanha a reserva de PE entre eles. As colunas “+ PE” são apenas capacidade nominal e **não podem ser somadas a uma simulação que já inclua o gasto desses PE**. A [revalidação corrigida](RASCUNHO-revalidacao-estocada.md) separa ataques, interações, perfis sem Batedor, escolhas de feitiço e livro-caixa por descanso. Nenhuma linha desta tabela demonstra que superar 5,50 seja robusto.

Análise de 22/09/2026, **sem alteração de regra**. Esta rodada compara a mesma ficha de Vanguarda que conjura nas sete rodadas do dia de referência, com e sem os ataques de ação bônus da Estocada. A escolha de quantas vezes permitir cada ataque é do Mizuki. **Leia também a [revalidação da escolha de feitiço](RASCUNHO-revalidacao-estocada.md): esta tabela fixa os feitiços como equivalentes e, por isso, o ganho de Bote nela é um teto condicional, não seu preço líquido.**

## Premissas e o que a conta significa

O dia tem três combates de três ou quatro turnos, com 10,5 turnos em média e sete conjurações conforme a régua do projeto. A política escolhe os turnos de conjuração e os usos permitidos para maximizar o benefício; isso torna a conta favorável, não uma média de decisões reais. A mesma conjuração ocorre nos dois lados e seu próprio dano ou condição se cancela na comparação. São contados Sequência, Escola, Persistência, Conclusão Dupla e o dano do ataque da ação bônus. Não se desconta o PE da Condução no preço, conforme a decisão de orçamento bruto. Não Cede permanece igual nos dois lados e também se cancela.

**Bote nesta tabela supõe que todos os sete feitiços sejam de condição e não causem dano**, exatamente o cenário favorável que permite seu gatilho em todos os turnos de conjuração. Um limite de uma vez por combate é uma **alternativa hipotética**, não a regra aprovada; o preço muda se vários combates estiverem na mesma cena. Sem limite, os valores reproduzem a conta anterior de Compasso no Caminho completo, mais o dano cru dos ataques de bônus. `C0` é sem Compasso, `C1` permite no máximo um uso por combate, `C2` dois e `C∞` todos os usos; `B` é o número máximo de turnos por combate com o segundo ataque de Bote. Bote só pode ocorrer num uso de Compasso. O modelo escolhe não usar uma permissão que não acrescente valor.

| Premissa | Valor |
|---|---:|
| orcamento_trilha_fatias | 5 |
| descanso_curto_min | 0 |
| descanso_curto_max | 2 |

| Cenário | Limite Compasso/combate | Limite Bote/combate |
|---|---:|---:|
| Sem ataques de bônus | 0 | 0 |
| Compasso uma vez | 1 | 0 |
| Compasso duas vezes | 2 | 0 |
| Compasso atual | sem_teto | 0 |
| Ambos uma vez | 1 | 1 |
| Compasso atual, Bote uma vez | sem_teto | 1 |
| Ambos atuais | sem_teto | sem_teto |

Valores abaixo são **acréscimos ao Caminho sem esses ataques** na mesma rotina de sete conjurações, em fatias. As colunas com PE somam apenas a **capacidade nominal** adicional do Compasso, caso ela seja toda recuperada e gasta; não garantem que exista demanda real por ela. Se o personagem não puder gastar os PE extras, vale o acréscimo sem PE. A coluna corpo a corpo usa a mesma pergunta na outra arma.

**Ressalva de PE:** a rotina de ataques do Caminho completo requer ao menos um descanso curto para acomodar sete feitiços de Classe 7 e as Conduções modeladas. Portanto, a coluna "0 descanso" abaixo combina um benefício de ataques que **não é plenamente viável nesse dia** com uma capacidade nominal de PE. Ela permanece apenas como limite formal da comparação antiga. A revalidação mostra essa diferença e o caso com descanso.

<!-- inicio-contas-orcamento-estocada -->
| Cenário | Distância | Corpo a corpo | Distância + PE, 0 descanso(s) | Distância + PE, 2 descanso(s) |
|---|---:|---:|---:|---:|
| Sem ataques de bônus | 0,000000 | 0,000000 | 0,578178 | 0,963630 |
| Compasso uma vez | 2,664878 | 0,999110 | 3,243055 | 3,628507 |
| Compasso duas vezes | 5,751195 | 1,990965 | 6,329373 | 6,714824 |
| Compasso atual | 6,489229 | 2,323643 | 7,067407 | 7,452859 |
| Ambos uma vez | 3,953545 | 1,863718 | 4,531722 | 4,917174 |
| Compasso atual, Bote uma vez | 8,270453 | 3,233791 | 8,848630 | 9,234082 |
| Ambos atuais | 9,991585 | 4,417990 | 10,569763 | 10,955215 |
<!-- fim-contas-orcamento-estocada -->

## Ação bônus, opções e custo de cada uma

A comparação antiga atribui custo de oportunidade **zero** à ação bônus. Isso omite usos alternativos reais; em particular, Mirar do Batedor custa essa mesma ação bônus e não pode ocorrer junto de Compasso no turno. Bote usa **a mesma ação bônus** de Compasso, portanto não se cobra uma segunda ação bônus pelo segundo ataque. A linha de sensibilidade abaixo é apenas um limiar formal da ficha antiga, com PE nominal somado; não é custo observado nem preço da Trilha.

<!-- inicio-limiar-orcamento-estocada -->
| Versão sem limite, PE aproveitado | Alternativa por ação bônus em equivalentes | Fração de um ataque comum |
|---|---:|---:|
| Compasso atual, 0 descanso(s) | 15,753641 | 0,687557 |
| Compasso atual, 2 descanso(s) | 18,690783 | 0,815746 |
| Ambos atuais, 0 descanso(s) | 42,441595 | 1,852334 |
| Ambos atuais, 2 descanso(s) | 45,378738 | 1,980523 |
<!-- fim-limiar-orcamento-estocada -->

**Conservar tudo sem limite:** mantém a identidade de conjurar e atacar em toda oportunidade. O teto favorecido desta ficha excede cinco fatias, mas não demonstra estouro robusto entre fichas, descansos e rotinas. A decisão de orçamento depende da revalidação corrigida.

**Limitar só Bote a uma vez por combate:** reduz o pico do nível 19 nesta ficha antiga. Sem os benefícios de Batedor, Compasso não foi demonstrado acima de cinco fatias; esta linha não decide o orçamento.

**Limitar Compasso e Bote a um uso cada por combate:** reduz o teto formal desta ficha antiga para a linha “Ambos uma vez”. Isso não certifica o orçamento, porque a ficha incorporou benefícios de Batedor e somou PE nominal sem gasto demonstrado. Compasso deixaria de oferecer o ataque na maioria dos turnos de conjuração; as conclusões de feitiço e Ferrão poderiam ganhar valor e precisariam de nova otimização. É uma opção para decisão futura, não regra adotada.

**Manter a regra enquanto se mede a mesa:** preserva todas as escolhas atuais; requer medir quantos dos sete feitiços realmente seriam de condição sem dano, quais ações bônus competem com Compasso e se o PE extra é efetivamente gasto. Sem esses dados, o intervalo é mais informativo que um preço único.

## Limites que impedem declarar preço final

O otimizador de Compasso/Bote acima mantém o feitiço igual nos dois lados, mas **não precifica o efeito próprio do feitiço, a sobreposição desse efeito com uma Conclusão de feitiço nem a escolha de feitiço de dano versus condição**. O valor de Bote só se aplica a feitiços de condição sem dano. O catálogo de feitiços e Ferrão tiveram marginal zero na rotina anterior baseada na Sequência sozinha; esse zero não foi revalidado sob limites de uso ou sob a ficha completa. Ferrão exige acertar a Conclusão de feitiço, pode substituir Canalizar no golpe e compete com Bote na mesma ação bônus. As duplas de feitiço do nível 30 também não foram reotimizadas aqui. Portanto, a tabela é **sensibilidade do núcleo de ataques**, não certificação das cinco fatias da Trilha inteira.

As duas implementações da conta anterior concordaram em Compasso sobre a Sequência sozinha. Nesta rodada, a versão de Caminho completo parte da mesma implementação v3 e reproduz o cenário de sete conjurações já publicado em `estocada-rotina-contas.json`. `python3 conferir-estocada-rotina.py --comparar-orcamento` refaz as linhas e confere as tabelas sem sobrescrevê-las.

**Conferência em 22/09:** os 18 validadores da releitura passaram em cópia isolada, assim como a comparação opcional acima. Em cópias separadas, aumentar em 10% cada valor L e Br de origem da Sequência fez a regressão falhar; aumentar o PE nominal de dois descansos e mudar o limite de Compasso de um para dois usos no cenário “Ambos uma vez” fizeram a tabela falhar e mudaram o resultado recalculado. Os arquivos de referência, Bastião e revisão não foram alterados.
