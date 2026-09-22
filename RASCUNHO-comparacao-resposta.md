# Interromper a Resposta — comparação de janelas

Rodada de 22/09/2026. **Decisão do Mizuki: manter as janelas diferentes.** Golpe Inicial foi aprovado como nome da etapa inicial nesta rodada.

## Escolha registrada

**Hoje:** Interromper a Resposta exige uma Condução acertada e um ataque à distância que acerte; após falhar no TR Físico, o alvo fica sem Reações até o começo do próximo turno do Vanguarda. Bloquear continua permitido.

**Alternativa estreita:** manter fonte, requisito e TR; após a falha, o alvo não pode usar Reação contra o próximo ataque que receber. Bloquear continua permitido. Essa alternativa espelha a janela de Cortar a Resposta; não reduz o requisito de duas Conduções da conclusão de feitiço. O texto do feitiço não fixa prazo adicional para esse próximo ataque: a conta também não supõe um novo prazo.

A janela larga pode proteger diferentes aliados, inclusive ao se deslocarem e provocarem ataques de oportunidade. A estreita protege um único ataque subsequente, do Vanguarda ou de um aliado. Não protege o deslocamento que vem antes dele, nem ações que não sejam ataques. Um ataque que não precisava dessa proteção pode consumir a janela. Em ambas, o benefício desaparece se o alvo já não tiver Reação relevante disponível.

## Método e limites

A comparação usa o mesmo otimizador v3, com Persistência atual e contabilidade bruta de `conferir-vanguarda-pe.py`. O PE continua sendo pago em mesa; não é descontado da avaliação do benefício. A Sequência da tabela não inclui Escola, Persistência, nível 30 nem Não Cede. O Caminho inclui todos esses componentes. O marginal da Dupla compara o Caminho com e sem o nível 30. O marginal de Resposta remove somente essa opção do catálogo e reotimiza o Caminho completo: mede o que ela acrescenta diante das alternativas, não seu valor isolado por aplicação.

A magnitude larga é lida do registro em `estocada-conclusoes-feiticos.md`. A estreita usa a convenção já adotada na magia: vantagem/desvantagem multiplicada pelo valor de um ponto percentual numa rolagem aliada, ambos lidos da peça 19 em `referencia-jjk-project/`. Isso é uma **aproximação de orçamento**, não uma medição de quantas Reações o grupo realmente evita. O modelo não simula iniciativa dos aliados, quantidade de Reações do alvo ou qual ataque consome a proteção. Não multiplicamos a magnitude larga pelo número de aliados.

Mantém-se também a hipótese de sobreposição já existente entre Fixar e Resposta. Os resultados são condicionais a essas réguas. Estreitar a janela não resolve, por si, a diferença de orçamento entre armas nem a dominância do catálogo de feitiços; essas são outras tarefas da fila.

Os dois cenários abaixo variam apenas a probabilidade de o alvo **falhar** no TR de Vigor. São hipóteses de sensibilidade, não novas regras. No cenário sem Fixar, falta a redução prévia de deslocamento que habilita essa conclusão.

| Cenário | Probabilidade de falhar em Vigor |
|---|---:|
| vigor_resiste_mais | 0.35 |
| vigor_resiste_menos | 0.85 |

## Resultados conferidos

Todos os valores são fatias, exceto magnitude (dano equivalente por aplicação) e tentativas por dia. `resposta` é Interromper a Resposta; `ritmo` é **Quebrar o Ritmo**, a Conclusão, e não a Manha Ritmo; `derrubada` é **Rasteira**. A tabela de dupla isolada libera apenas aquele par no nível 30, mantendo as conclusões simples disponíveis. Seu valor é marginal ao Caminho sem o nível 30. Tentativas por dia não são acertos nem benefício adicional.

<!-- inicio-contas-resposta -->
| Grandeza | Larga | Estreita |
|---|---:|---:|
| Magnitude por aplicação bem-sucedida | 36.500000 | 5.750000 |
| distancia/sequencia | 3.010113 | 3.010113 |
| distancia/caminho | 5.068278 | 5.068278 |
| distancia/dupla_marginal | 0.839703 | 0.839703 |
| distancia/resposta_marginal | 0.000000 | 0.000000 |
| distancia/dupla:ritmo+fixar/tentativas_dia | 2.474763 | 2.474763 |
| distancia/dupla_isolada/derrubada+ritmo | 0.000000 | 0.000000 |
| distancia/dupla_isolada/derrubada+resposta | 0.000000 | 0.000000 |
| distancia/dupla_isolada/derrubada+fixar | 0.000000 | 0.000000 |
| distancia/dupla_isolada/ritmo+resposta | 0.000000 | 0.000000 |
| distancia/dupla_isolada/ritmo+fixar | 0.839703 | 0.839703 |
| distancia/dupla_isolada/resposta+fixar | 0.571979 | 0.089998 |
| corpo_a_corpo/sequencia | 0.100526 | 0.100526 |
| corpo_a_corpo/caminho | 1.340939 | 1.340939 |
| corpo_a_corpo/dupla_marginal | 0.050587 | 0.050587 |
| corpo_a_corpo/resposta_marginal | 0.000000 | 0.000000 |
| corpo_a_corpo/dupla:derrubada+ritmo/tentativas_dia | 0.906990 | 0.906990 |
| sem_fixar/sequencia | 1.226408 | 1.226408 |
| sem_fixar/caminho | 2.882867 | 2.341040 |
| sem_fixar/dupla_marginal | 0.633400 | 0.091573 |
| sem_fixar/resposta_marginal | 0.541827 | 0.000000 |
| sem_fixar/dupla:derrubada+ritmo/tentativas_dia | 0.000000 | 1.286803 |
| sem_fixar/dupla:resposta+ritmo/tentativas_dia | 2.466616 | 0.000000 |
| vigor_resiste_mais/sequencia | 2.998948 | 2.951169 |
| vigor_resiste_mais/caminho | 4.789081 | 4.700780 |
| vigor_resiste_mais/dupla_marginal | 0.572178 | 0.533829 |
| vigor_resiste_mais/resposta_marginal | 0.088301 | 0.000000 |
| vigor_resiste_mais/dupla:resposta+fixar/tentativas_dia | 2.474763 | 0.000000 |
| vigor_resiste_mais/dupla:ritmo+fixar/tentativas_dia | 0.000000 | 2.466616 |
| vigor_resiste_menos/sequencia | 3.098527 | 3.098527 |
| vigor_resiste_menos/caminho | 5.627601 | 5.627601 |
| vigor_resiste_menos/dupla_marginal | 1.306590 | 1.306590 |
| vigor_resiste_menos/resposta_marginal | 0.000000 | 0.000000 |
| vigor_resiste_menos/dupla:ritmo+fixar/tentativas_dia | 2.474763 | 2.474763 |
<!-- fim-contas-resposta -->

## Leitura da comparação

Na referência à distância, a rotina ótima escolhe Quebrar o Ritmo + Fixar o Alvo nas duas janelas. Por isso, cortar o valor de Resposta não muda o preço desse pacote. Isso não prova que Resposta seja inútil.

Sem Fixar, a janela larga sustenta Interromper a Resposta + Quebrar o Ritmo; ao estreitar, o otimizador troca para Rasteira + Quebrar o Ritmo. Contra Vigor mais resistente, também há troca: Resposta + Fixar dá lugar a Quebrar o Ritmo + Fixar. Na referência, liberar apenas Resposta + Fixar dá um marginal menor com a janela estreita. Os outros dois pares com Resposta já não são escolhidos diante das conclusões simples disponíveis e continuam com marginal zero; isso não significa que sua magnitude por aplicação ficou igual. Os pares sem Resposta mantêm o mesmo marginal.

**Manter a larga:** conserva uma função de proteção do grupo e uma alternativa em encontros nos quais Fixar não cabe. Aceita que arma e magia tenham identidades distintas apesar da origem comum.

**Adotar a estreita:** aproxima os textos e limita a proteção a um ataque, mas enfraquece a alternativa de arma justamente nos cenários em que hoje ela é escolhida. A referência principal sozinha esconde essa perda.

O Mizuki escolheu **manter a janela larga de Interromper a Resposta**. A conclusão de feitiço já entra por um feitiço, e o efeito adicional mais curto pode ser mais fraco. A comparação acima registra o custo hipotético de igualar os textos; as regras vigentes continuam com janelas diferentes.

## Reprodução e validação

`python3 conferir-vanguarda-v3.py --comparar-resposta` recalcula o modelo, confere a tabela publicada sem sobrescrevê-la e gera `vanguarda-resposta-contas.json`. A decisão registrada mantém a regra vigente de Interromper a Resposta. Os validadores antigos da Escola continuam sendo uma dívida já registrada, fora desta rodada.

Validação desta rodada: os 18 scripts passaram em cópia isolada; a comparação adicional também passou antes das perturbações. Em quatro cópias separadas, alterar a magnitude larga, a régua estreita, a chance de falha em Vigor e um resultado publicado fez a checagem da tabela falhar como esperado. As fontes protegidas do repositório permaneceram intactas. Esse verde conserva a limitação conhecida do validador antigo da Escola; não o reabilita.
