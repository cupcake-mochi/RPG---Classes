> **Relatório de agente, 20/09/2026.** Produzido numa sessão do Claude Code, com instrução de refutar, contra o JJK---Project na v0.261. Os achados 1 a 7 e o 12 foram conferidos à mão depois contra o texto do repositório, e batem. O achado 7 (nível 2) usa um modelo de uma rota só; a conta está em `nivel-2.py` nesta pasta. O −1,18 do Golpe de Impacto supõe o dado de Canalizar dobrando no crítico; pela regra que a própria pasta declara (não dobra), sai −1,25 — a conclusão não muda. Nenhum arquivo foi alterado por esta revisão.

# Revisão cética — reforma Vanguarda / Estocada / nomes do Bastião

Revisor: leitura só. Pasta de trabalho (são **15** `.md`) contra o repositório em v0.261 (lido de `.git/logs/HEAD`, sem rodar git).

Uma coisa antes de tudo: **o texto de regra das seis conduções e das sete conclusões de arma não está em nenhum arquivo da pasta.** Os `.md` falam "o rascunho", "o texto aprovado na conversa", e citam efeito só de tabela de preço. O que eu sei de Golpe de Impacto, Fixar, Pressionar etc. eu tirei do script `conferir-vanguarda-v3.py`. Isso contamina metade dos achados abaixo — vários "o texto não diz" podem estar resolvidos num texto que eu não vi. Marquei esses como tal.

---

## Triagem de nomes

Rodado de `sistema/03-mecanica/` com `python3 conferir-nomes.py --candidatos ...` (nome composto entra entre aspas; é `sys.argv[2:]` puro). Saída literal da seção 6, nos dois lotes:

```
  LIVRE    Sequência de Combate
  LIVRE    Abertura
  LIVRE    Abrir
  OCUPADO  Condução         ja e oficio no projeto
  LIVRE    Conduzir
  LIVRE    Conclusão
  LIVRE    Concluir
  LIVRE    Persistência
  LIVRE    Conclusão Dupla
  LIVRE    Mudar o Ângulo
  DENTRO   Pressionar a Guarda carrega "Guarda" (Melhoria) dentro dele
  LIVRE    Proteger o Avanço
  LIVRE    Acompanhar o Movimento
  LIVRE    Explorar o Desequilíbrio
  LIVRE    Fechar a Rota
  DENTRO   Golpe de Impacto carrega "Impacto" (Tema) dentro dele
  fraco    Derrubada        a uma letra de "Derrubado" (Condicao)
  LIVRE    Desarme
  LIVRE    Explorar a Cobertura
  LIVRE    Interromper a Resposta
  LIVRE    Quebrar o Ritmo
  LIVRE    Fixar o Alvo
  OCUPADO  Precisão         ja e vocabulario do glossario no projeto; e Melhoria no manual
  OCUPADO  Guarda           e Melhoria no manual
  OCUPADO  Impacto          e Tema no manual
  LIVRE    Desvio
```
```
  LIVRE    Cortar a Resposta
  LIVRE    Abrir Caminho
  LIVRE    Desorientar
  DENTRO   Expor a Guarda   carrega "Guarda" (Melhoria) dentro dele
  LIVRE    Ancorar
  fraco    Refluxo          a uma letra de "Reflexo" (Tema)
  LIVRE    Olhos Em Mim
  LIVRE    Nem Um Arranhão
  LIVRE    Duro de Matar
  LIVRE    Chega Mais
  LIVRE    Passa Pra Mim
  LIVRE    Guarda-Costas
  LIVRE    Casca Grossa
  LIVRE    Inabalável
  LIVRE    Trocação Franca
  LIVRE    Mão Pesada
  LIVRE    Minha Vez
  LIVRE    Arrastão
  LIVRE    Retaliação
  LIVRE    Embalo
  LIVRE    Oportunista
  LIVRE    Contra a Parede
  LIVRE    Combatente Amaldiçoado
```

Rodei mais uns pra testar o validador em si, e ele tem **dois pontos cegos** que a pasta explorou sem querer:

```
  LIVRE    Guarda-Costas          <- com hífen
  DENTRO   Guarda Costas    carrega "Guarda" (Melhoria) dentro dele   <- sem hífen
  OCUPADO  Caminho          ja e termo de sistema no projeto
  LIVRE    Abrir Caminho          <- carrega "Caminho" e passou
  OCUPADO  Corpo Amaldiçoado ja e Origem no projeto
  DENTRO   Amaldiçoado      dentro de "Corpo Amaldicoado" (Origem)
  prefixo  Rota             comeca "Rotação" (Tema)
  OCUPADO  Cobertura        ja e vocabulario do glossario no projeto
  OCUPADO  Alicerce         ja e entrega de catalogo no projeto   (é o mesmo Alicerce, mantido — ok)
  LIVRE    Dupla
```

1. **Hífen engana o `split()`**: a checagem "carrega X dentro dele" exige `len(cand.split()) > 1`, e `Guarda-Costas` é um token só.
2. **A checagem "carrega X" só varre as categorias do manual, não o vocabulário do projeto.** `Caminho` sozinho é OCUPADO; `Abrir Caminho` passa LIVRE. Mesma coisa faria `Fixar a Trilha` passar.

### Tabela

| nome | validador | colisão de sentido? | colisão com o hobby? | veredito |
|---|---|---|---|---|
| Sequência de Combate | LIVRE | não | não | ok |
| Abertura / Abrir | LIVRE | **sim** — "abrir" e "abertura" são o vocabulário da Expansão de Domínio no sistema (peça 11: "com N marcas você abre a Expansão N vezes, que são N−1 reaberturas"; `RASCUNHO-expansao-sem-barreira.md` usa "a cada abertura" cinco vezes). Um Vanguarda com Expansão que diz "abri" está dizendo duas coisas | "opening" de jogo de luta, inofensivo | **renomear** ou aceitar declarado |
| Condução | **OCUPADO** (ofício) | é o ofício de dirigir | — | **morto** |
| Conduzir | LIVRE | é o verbo do ofício Condução; morre por arrasto | — | **morto** |
| Conclusão / Concluir | LIVRE | não | não | ok |
| Persistência | LIVRE | não | "dano persistente" do PF2e, fraco | ok, provisório |
| Conclusão Dupla | LIVRE | `<substantivo> <adjetivo>`: lê como categoria "Conclusão" com nome "Dupla". E `Dupla` foi categoria de inimigo até a v0.221 ("a Dupla morreu") e **não está na lista MORTOS** do validador | — | ok com ressalva; se for nome de habilidade, inverter a forma |
| Mudar o Ângulo | LIVRE | não | não | ok |
| Pressionar a Guarda | DENTRO (Guarda, Melhoria) | a Melhoria `Guarda` é "+2 de defesa até o fim do próximo turno" (manual 40, l.715); aqui "guarda" é a postura defensiva do alvo — mesmo sentido, não colide | — | ok |
| Proteger o Avanço | LIVRE | não | não | ok |
| Acompanhar o Movimento | LIVRE | "Movimento" está em "Ação de Movimento", mas aqui É movimento | — | ok |
| Explorar o Desequilíbrio | LIVRE | não | não | ok |
| Fechar a Rota | LIVRE (prefixo de Rotação) | **sim** — `Rota` é termo do Batedor: "Rota: Yumi", "Rota: Besta", "Rota: Arma de Fogo", "a rota se escolhe no nível 2" (manual 35, oito ocorrências). Um Batedor que "fecha a rota" está fechando o quê? O validador não tem "Rota" no universo | — | **renomear** |
| Golpe de Impacto | DENTRO (Impacto, Tema) | **sim** — `Impacto` é tipo de dano/Tema ("Corte · Impacto · Perfuração"). A conclusão mexe em margem crítica e não tem nada a ver com tipo. "Minha katana é Corte, posso dar Golpe de Impacto?" | — | **renomear** |
| Derrubada | fraco (Derrubado) | **sim** — são três a uma letra: `Derrubar` (opção da ação Atacar, manual 11 §"Agarrar e Derrubar"), `Derrubado` (condição), `Derrubada` (conclusão) | Trip/Shove do 5e | **renomear** |
| Desarme | LIVRE | mesmo padrão: aplica `Desarmado` | "Desarmar" é ação opcional do 5e DMG e ação do PF2e | rever |
| Explorar a Cobertura | LIVRE (Cobertura sozinho é OCUPADO) | carrega o termo de propósito — ela mexe em cobertura | — | ok |
| Interromper a Resposta | LIVRE | **sim** — "Resposta" é apelido de `Reação`, que é termo definido (OCUPADO). E `Cortar a Resposta` da Estocada tem o **mesmo efeito** com outro nome | — | **unificar os dois** e dizer "Reação" no nome |
| Quebrar o Ritmo | LIVRE | não | não | ok |
| Fixar o Alvo | LIVRE | não | não | ok |
| Precisão (Manha) | **OCUPADO** (glossário + Melhoria) | a Melhoria `Precisão` é "+2 na rolagem de acerto"; a Manha é +1 no acerto. **Mesmo efeito, número diferente** — pior colisão possível. Todos os docs da pasta que dizem "Yumi com Precisão" precisam mudar | — | **morto** |
| Guarda (Manha) | **OCUPADO** (Melhoria) | a Melhoria `Guarda` é "+2 de defesa até o fim do próximo turno"; a Manha é "+1 de Defesa até o começo do seu próximo turno". **Mesmo efeito, número diferente**, igual ao caso da Precisão | — | **morto** |
| Impacto (Manha) | **OCUPADO** (Tema) | — | — | **morto** |
| Desvio (Manha) | LIVRE | **sim, invertido** — a Manha desloca o *alvo* 1,5 m; "desviar" no hobby é o *defensor* esquivar | Esquiva/Desviar em Tormenta, 3D&T, D&D em PT | **renomear** |
| Cortar a Resposta | LIVRE | idem Interromper a Resposta | — | unificar |
| Abrir Caminho | LIVRE (**ponto cego**) | **sim** — carrega `Caminho`, que é a classe do sistema. "Abrir Caminho" lê como "abrir uma classe". E ainda carrega "Abrir", a etapa | — | **renomear** |
| Desorientar | LIVRE | não | não | ok |
| Expor a Guarda | DENTRO (Guarda) | idem Pressionar — "guarda" como postura, não colide | — | ok |
| Ancorar | LIVRE | "ancorado" aparece na Expansão (domo ancorado), prosa | não | ok |
| Refluxo | fraco (Reflexo, Tema) | na mesa falada, "refluxo" é o gástrico | — | renomear |
| Olhos Em Mim … Contra a Parede (Bastião, 16 nomes) | LIVRE | — | — | ok |
| Guarda-Costas | LIVRE (**ponto cego**, hífen) | sentido de "pessoa" é outro do de "postura", então não colide de fato | — | ok, mas registrar que passou por buraco |
| Combatente Amaldiçoado | LIVRE | **fraco** — `Corpo Amaldiçoado` é Origem (OCUPADO). "X Amaldiçoado" no sistema é coisa feita de energia amaldiçoada (Ferramenta, Objeto, Corpo). Um Bastião de Origem Corpo Amaldiçoado e Trilha Combatente Amaldiçoado tem dois "Amaldiçoado" na ficha com sentidos diferentes | — | aceitar declarado, ou trocar |

Resumo: **cinco mortos** (Condução, Conduzir, Precisão, Guarda, Impacto), **seis pra renomear** por sentido (Abrir/Abertura, Fechar a Rota, Golpe de Impacto, Derrubada, Desvio, Abrir Caminho), dois pra unificar (as duas "Resposta").

---

## Achados

### BLOQUEIA porte ao repo

**1. O texto-base da Sequência não existe em arquivo.**
Os 15 `.md` da pasta não trazem o texto das seis conduções nem das sete conclusões de arma — requisito, efeito, duração, CD, alcance. `vanguarda-precificacao-v2.md` tem uma tabela "Valores de controle utilizados" que dá o *preço* de cada uma ("Mudar o Ângulo | 3 metros × 0,60 = 1,80"), e é tudo. Regras que só existem no script: `conferir-vanguarda-v3.py`, função `available_finishes` — Golpe de Impacto e Explorar a Cobertura exigem **zero** conduções; Desarme é só corpo a corpo; Interromper a Resposta e **Fixar o Alvo são só à distância** (`if n>=2 and not cfg.melee`). Nenhum documento diz isso. Não dá pra portar o que não está escrito, e não dá pra revisar o que não dá pra ler.

**2. A premissa de orçamento inteira não está no repositório.**
A pasta trabalha com "cinco fatias para o Caminho" e um degrau de Caminho no **nível 23** (Persistência; e `Chega Mais` do Bastião). O repo diz outra coisa em três donos:
- `DESENHO-caminhos.md` linha 5: *"Caminho em `2 · 7 · 15 · 30`, Trilha em `2 · 11 · 19 · 27`. **O Caminho leva `3` fatias** (níveis 2, 15 e 30); **o nível 7 é de graça**"*.
- `ESTADO-ATUAL.md` linha 994: *"a fatia é `5,08`, o Caminho leva `3` fatias e a Trilha leva `5`"*.
- peça 18, tabela de progressão: nível 23 = `—`. Manual 35, "Entregas por nível": 2, 7, 11, 15, 19, 27, 30 — não tem 23.

A "reforma do Bastião" que a pasta cita como referência (Olhos Em Mim, Provocar, Retaliação com Força no PE, cinco fatias) tem **zero ocorrências** no repo — `grep -rl "Encarar\|Aparar com Corpo\|Retaliação"` não acha nada fora da pasta. Ou a reforma entra antes, ou os 5,00 da Vanguarda viram 3,00 e o nível 23 some. E mesmo aceitando cinco: `vanguarda-orcamento.md` diz *"A distribuição dessas opções pelos níveis ainda pode ser definida"* — **ninguém consegue montar uma Vanguarda de nível 2 com a pasta**, porque não está escrito o que chega no 2.

**3. Compasso soma atributo ao PE máximo, e a peça 1 proíbe isso com motivo escrito.**
`estocada-compasso.md`: *"Seu máximo de pontos de energia aumenta em um valor igual ao atributo escolhido... o máximo passa a ser 5 × nível + atributo escolhido"*. Peça 01 §5.3: *"Pontos de energia = PE por nível do seu Caminho × o seu nível. **Sem atributo e sem valor inicial.** A parte do atributo é a decisão da seção 9 aplicada: se um atributo somasse PE, ele viraria o atributo obrigatório de todo conjurador pela porta dos fundos."* Manual 35, em negrito: *"Nenhum atributo entra nessa conta, e não existe valor inicial somado por cima."* A pasta não declara o conflito e justifica com *"seguindo a ideia de Força no PE máximo do Combatente Amaldiçoado"* — que também não está no repo. O `conferir-manual.py` confere a coluna "quantas vezes você lança" como `taxa × nível`. Não é que não possa ser exceção; é que exceção sem declarar contra um dono que diz "por quê não" vai quebrar validador e o argumento da peça 1 junto.

**4. O alvo morre no meio da sequência — e o texto dá duas leituras que travam a mesa de jeito oposto.**
`vanguarda-conclusao-dupla.md`: *"Uma única sequência ativa, contra um único inimigo."* `vanguarda-escolas-rascunho.md`: *"Não é possível reabrir uma sequência ainda ativa."* Nenhum documento diz o que acontece quando o inimigo cai, nem se dá pra abandonar uma sequência de propósito. `vanguarda-nv23-proposta.md` até lista "Passagem para outro adversário: aproveitar parte da preparação quando o alvo cai" como direção *não desenvolvida* — o que sugere que hoje a preparação se perde, mas não escreve isso como regra.
- Mestre A: o alvo caiu, a sequência acabou, abre em outro no mesmo turno.
- Mestre B: a sequência está "ativa" até o fim de T+2 (a última condução acertou), e "não é possível reabrir uma sequência ainda ativa" — o Vanguarda fica dois turnos sem poder abrir em ninguém.
Contra esquadrão de oito capangas (o encontro padrão da peça 26) isso acontece toda luta. É o filtro do projeto falhando na situação mais comum.

### VALE CORRIGIR

**5. Contradição interna: a v2 ainda publica o teto de duas conduções e "erro não apaga".**
`vanguarda-precificacao-v2.md`: *"**O autor confirmou que continua o teto de duas conduções acertadas por sequência.** Não existe renovação ilimitada. ... erro não renova nem apaga antecipadamente."* `vanguarda-orcamento.md`: *"Não há teto de conduções acertadas por sequência. ... Errar o ataque de uma condução encerra imediatamente."* A v2 tem banner só sobre o valor 2,00; sobre essas duas regras, nada. `vanguarda-escolas-rascunho.md` ganhou um "Atualização de 19/09" — a v2 não. Quem abrir a v2 (que é o documento com a tabela de escada e o método de preço) lê a regra velha como vigente.

**6. Conclusão Dupla é "uma vez por cena", e a peça 10 §5 manda descer.**
Peça 10 §5: *"Se o relógio é o único limitador — o gatilho é combate, e combate acontece toda missão —, desça para `por descanso curto`, cujo gatilho de ficção ... 'a luta acabou' dois mestres arbitram igual."* O gatilho da Dupla ("ao Concluir com ≥2 conduções") é combate. A própria pasta aplicou essa regra à Persistência (`vanguarda-nv23.md`: *"O contador substitui a proposta anterior de um uso por cena"*) e não à Dupla. Pior: a auditoria trata cena = combate (*"Cada combate é tratado como uma nova cena"*), e a peça 10 mediu que essa leitura varia **3,0×** entre mestres. O preço de 1,00 fatia da Dupla foi calculado numa das três leituras.

**7. No nível 2 a Sequência é botão de prejuízo, e a pasta só conferiu se o PE cabe.**
Toda a precificação é no 30 com dois ataques, Mirar e 87,75% de acerto. Enumerei o nível 2 (um ataque por turno até o 7, 55% de acerto, katana 1d8+3+1d4 = 10, maestria 1: perde 1d4, condução 2 PE de 10, erro encerra, sem Persistência):

```
Rota Abrir -> Conduzir -> Concluir Derrubada, luta de 3 turnos:
  P(abre)=0,550  P(condução acerta)=0,303  P(Derrubado aplicado)=0,058
  dano perdido esperado=1,38   PE esperado=1,10 de 10   benefício esperado=0,54 equiv.
  líquido SEM cobrar PE = -0,83 equiv por luta ; cobrando PE a 5,14 = -6,48
Rota Abrir -> Golpe de Impacto:
  ganho da margem crítica = +0,35 ; custo da abertura = 1,38 ; líquido = -1,18 por tentativa
Dois ataques normais nos mesmos 2 turnos: 11,00 ; abrir + Impacto: 9,82
```
(script em `nivel-2.py`, nesta pasta). Cinco níveis em que o mecanismo central do Caminho perde dinheiro em toda rota, mesmo de graça. A única conferência de nível 2 da pasta é *"duas conduções a 2 PE e dois feitiços de Classe 1 a 3 PE somam 10 PE"*. E o 10 de dano da katana vem da escada do **manual** (1d4 no refino 1); a peça 11 §6.9, que é a dona declarada, só dá dado no refino 3 — no nível 2 a katana faz 7,5 e a abertura come 33%, não 25%. A pasta viu a divergência e escolheu a fonte que não é dona.

**8. Abrir: declara antes de rolar ou decide depois que acertou?**
Conduzir: *"declarado e pago antes da rolagem"*. Concluir com Dupla: *"Escolha as duas antes de rolar"*. Ferrão: *"Escolha usar Ferrão antes de rolar"*. Abrir: *"A redução é rolada uma vez quando o ataque acerta"* — e só. Um jogador que só chama de Abertura o golpe que já acertou nunca paga abertura em golpe errado (que hoje não custa nada mesmo) mas também escolhe abrir só quando o dano sobrando compensa. Dois mestres respondem diferente; a Manha da Escola (que dispara "ao acertar a Abertura") herda a dúvida.

**9. Ataque fora do seu turno pode ser etapa?**
Peça 3: *"o ataque de oportunidade é ataque físico, rolado como ataque comum e pago com a Reação"*. O `Revide` do Executor e o contra-ataque do Aparar (peça 23) também são ataques. A pasta diz *"usando um ataque já disponível"* e *"no máximo uma condução ou conclusão por turno"* — turno de quem? Se um ataque de oportunidade no turno do inimigo pode Conduzir: (a) o limite "por turno" não segura nada fora do seu turno; (b) o prazo "fim do segundo turno **seu** após a última condução acertada" fica ambíguo pra uma condução que acertou no turno dele. Nenhum documento toca nisso.

**10. As condições das conclusões não têm duração escrita, e a peça 19 dá TR de fim de turno pra `Pesada`.**
O modelo conta *"a condição por uma rodada após aplicação"* (v1). Peça 19 §2.2: *"a condição dura UMA rodada"* — mas isso é da Melhoria `Condição` do manual, não regra geral de condição. E §3.3: *"Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo"*. O Impedido de Fixar (Pesada) dá esse TR? Dura uma rodada, "até o fim do próximo turno dele", até passar no TR? O Lento de Quebrar o Ritmo? O preço de 132,15 supõe uma rodada; a mesa não tem como saber. (Pode estar no texto que eu não vi — item 1.)

**11. "Redução de movimento" pra Fixar — o que conta?**
`vanguarda-precificacao-inicial.md` diz que Fechar a Rota *"não reduz a característica de deslocamento e, portanto, não satisfaz sozinha o requisito atual de Fixar"*. Isso é raciocínio de auditoria, não regra. Terreno difícil (Aterro do Muro), Laço/Prego (perde metade / 9 m do próximo turno), Agarrado (deslocamento 0), Ancorar, Alicerce do próprio alvo — cada mestre monta a lista dele.

**12. A "correção" de Fagulha troca a convenção da régua, não corrige aritmética.**
`bastiao-correcao-fagulha.md`: *"Na base, faltava aplicar o acerto do feitiço"* → 27 × 0,50 × 0,56. Só que a régua de Trilhas não aplica acerto ao golpe entregue: `DESENHO-trilhas.md` linha 650, *"O certo é `11,50 × 0,75 = 8,63`"* (Engate: soco cru × taxa de gatilho, sem os 55%); peça 5 §4, *"o soco no nível 30 — `d10 + Força 6` — permanente `11,50` = 2,26 fatias"*, cru. Aplicar 50% só na Fagulha põe ela numa escala diferente da irmã de tabela — o 2,05 não é comparável com o 1,70 do Engate. A parcela de vantagem da pasta (27 × 0,25 × 0,75 × 0,56 = 0,56 fatia) *bate* com a convenção da régua (25 pp × dano cru × gatilhos); a parcela base não. Ou os dois lados aplicam acerto, ou nenhum. Como está, é a armadilha do "esse número já inclui?" ao contrário: a régua **não** inclui acerto, e a correção pôs.

**13. Dominância no catálogo mágico da Estocada.**
Pela régua da peça 19 (vantagem/desvantagem = 25 pp; 1 pp de aliado = 0,230; uma ação de chefe = 73):
- **Expor a Guarda**: 2 conduções + TR Vigor → vantagem em um ataque de aliado ≈ 25 × 0,230 = 5,75 × chance de falha (0,35–0,55) ≈ **2,0–3,2**.
- **Desorientar**: 1 condução, **sem TR** → desvantagem na próxima rolagem dele; se for ataque, 25 pp × 73 ≈ **18,25**. Mesmo com desconto pesado, fica acima.
- **Refluxo**: 1 condução, sem TR → 1 PE temporário que some no fim da cena ≤ **5,14**, e só se for gasto.
Teste da skill: *"existe uma situação em que eu escolheria A em vez de B?"* Expor a Guarda contra Desorientar: praticamente nunca (requisito maior, TR a mais, valor menor). Refluxo contra Desorientar: só sem PE nenhum. A pasta reconhece que o catálogo não tem preço; o que eu digo é que ele já reprova antes do preço.

**14. Compasso escolhe "grupo de armas", e "grupo" não é termo.**
Peça 14 §5.1.2 define **treze categorias**. O manual 35 agrupa as treze em *"Simples, Marciais e Arma de Fogo"*. "Grupo" não está definido em lugar nenhum (grep em peça 14, manual 50, glossário). Um mestre lê "grupo" = categoria (Lâmina Longa); outro lê "grupo" = Marciais inteiro. A ambiguidade é herdada do manual, mas a pasta reescreveu o Compasso inteiro e manteve a palavra.

**15. Nível 7 da Vanguarda: `Não Pega` é dela ou do Bastião?**
Peça 06 §3.1: *"Vanguarda | ataque extra + `Não Pega` | 0,92 | 1,18 | **2,10**"* — a metade nova do nível 7 da Vanguarda. Manual 35: `Não Pega` e `Ainda de Pé` estão os dois no **Bastião**, e o nível 7 da Vanguarda é só o ataque extra. `bastiao-nomes-aprovados.md` segue o manual (renomeia Não Pega → Nem Um Arranhão no Bastião). O orçamento de 5,00 da Vanguarda não tem Não Pega. Se a peça 06 estiver certa, faltam 1,18 fatias na conta; se o manual estiver certo, a peça 06 §3.1 está errada. Contradição do repo, mas o porte tropeça nela.

**16. Duas conclusões com o mesmo efeito e dois nomes.**
`Interromper a Resposta` (arma) e `Cortar a Resposta` (feitiço): as duas tiram Reação até o começo do seu próximo turno. Derrubada e Quebrar o Ritmo são compartilhadas entre os catálogos de arma com um nome só; "sem Reação" ganhou dois. E "Resposta" é apelido do termo definido `Reação` — o critério da v0.40 é justamente que um nome pode carregar o termo quando *é* aquilo.

### SUSPEITA (não confirmei; digo o que falta)

**17. Escala mista na auditoria da Vanguarda.** Os custos (dano perdido, ganho de crítico) entram com 55% de acerto; os benefícios de condição (8,45; 39,20; 132,15), Defesa (3,39) e movimento (0,60/m) vêm da régua, que é em dano cru. Se a fatia foi calibrada em cru (a Rotina é dado médio sem acerto), a parte de dano da Sequência está deflacionada em ~0,55 e os 1,49–2,00 não são a mesma moeda dos 3,39 de +1 Defesa. **Falta confirmar:** qual escala a fatia usa — e rodar o Engate na convenção da pasta pra ver se a escala anda.

**18. Persistência: contador que cresce (maestria) sobre magnitude que cresce (PE por condução sobe com maestria).** A skill diz *"um dos dois cresce, nunca os dois"*. Não Cede já faz isso no repo, então pode ser convenção aceita. **Falta:** decisão declarada.

**19. Derrubada contra o `Derrubar` de graça.** Manual 11 §"Agarrar e Derrubar": *"Cada uma aplica a condição de mesmo nome"* — qualquer ataque pode Derrubar, sem abertura nem condução. A conclusão exige abertura + 1 condução + TR e dá Derrubado + empurrão de 3 m. **Falta:** a resolução do Derrubar livre (peça 3 §"são opção do ataque" não escreve o teste nem se ele substitui o dano). Se substitui o dano como no 5e de 2024, a conclusão não está dominada; se não, está.

**20. Proteger o Avanço (+1 Defesa) e o invariante da peça 23 §4.** *"Bloquear usa exatamente o mesmo modificador da Defesa passiva. Nada pode aumentar um sem aumentar o outro"* — e o validador confere a **mesma expressão**. A Manha Guarda diz "Inclui Bloquear"; Proteger o Avanço, que também é +1 Defesa (v2: *"3,39 por rodada protegida, pela régua publicada de Defesa"*), não tem texto que eu tenha visto. **Falta:** o texto (item 1).

### COSMÉTICO

**21. A pasta inventa arredondamento que a peça 1 §5.4 já dá.** *"Arredonde sempre para o lado que não te favorece. O que você paga sobe. O que você ganha desce. E o que você ganha nunca fica abaixo de 1."* Abertura e condução (paga) sobem; Persistência (ganho) desce. A v2 chama isso de *"interpretação de trabalho, não uma nova regra geral"* e a nv23 de *"específico deste contador"*. É regra geral, com dono. Cite o dono e apague as duas frases.

**22. Refluxo: *"Uma condução gratuita gera zero"*** — não existe condução gratuita na regra vigente. Sobra de versão anterior.

**23. Energia temporária, peça 1 §5.1.2:** a tabela lista só Braseiro e Trindade e diz *"Ninguém tem as duas"*. Refluxo (Estocada) e Embalo (Bastião) entram como terceira e quarta fonte; a tabela e a frase precisam andar.

**24. `Dupla` não está em MORTOS** apesar de "a `Dupla` morreu" na v0.221. Não morde, mas o contador de termo morto existe pra isso.

**25. Compasso mantém *"Se escolheu Versado, escolhe grupos iguais à maestria"*, e o Versado novo não escolhe categoria nenhuma** (*"Pode abrir com qualquer arma elegível"*). A regra do Compasso fazia sentido quando Versado era "trocar de arma no turno"; com o Versado da Escola simplificada, o número de grupos deixou de conversar com o que ele faz. `vanguarda-escolas-rascunho.md` diz que isso *"requer revisão junto da Trilha"*; `estocada-compasso.md`, mais novo, diz *"conforme a regra já existente"*. Um dos dois envelheceu.

---

## O que eu procurei e não achei

- **Duplo desconto no orçamento de 5,00.** Os marginais estão em ordem de progressão (23 antes do 30: 0,2091 + 0,8395 = 1,0487) e a interação Escola×Dupla está contada uma vez, dentro da Dupla. Refiz as decomposições (368,69 ÷ 10,5 ÷ 5,08 = 6,912; 18,0112 PE × 5,14 ÷ 10,5 ÷ 5,08 = 1,7356; Não Cede 0,50 × 0,35 × 0,65 × 36,5 ÷ 5,08 = 0,8173; Fagulha 0,50 + 0,75 × 0,25 = 68,75%) — fecham.
- **Fixar + Quebrar o Ritmo somando movimento duas vezes** — o modelo usa `max(movement)`, não soma. Ok.
- **Persistência numa Abertura errada** — o texto restringe a Condução, e uma Abertura errada não abre nada. Sem furo.
- **T+2: turno da abertura conta como 0 ou 1** — definido com exemplo em `vanguarda-conclusao-dupla.md` (abriu no 1, retoma no 2 ou 3, encerra no fim do 3). Consistente nos outros docs.
- **"Acertar a condução" vs "o alvo passa no TR"** — os seis documentos que usam dizem a mesma coisa (acerto conta e renova; TR passado não é erro).
- **"Afetar o alvo" pra feitiço** — `estocada-conclusoes-feiticos.md` e `estocada-ferrao.md` usam a mesma definição (acerto ou falha no TR principal; dano parcial não basta).
- **Bote e Ferrão no mesmo turno** — exclusão mútua escrita igual nos três docs e no manual.
- **Refluxo contra a regra de energia temporária** — bate ponto a ponto com a peça 1 §5.1.2 (gasta antes, não acumula, teto metade, some no fim da cena, mestre pode deixar atravessar).
- **Cortar/Interromper a Resposta "não impede Bloquear"** — confere: peça 23 §3, Bloquear *"não gasta a sua Reação"*.
- **Usuário Incapacitado** — na peça 19 Incapacitado só tira Bloquear e faz corpo a corpo crítico; não mexe em ataque nem turno. A sequência segue. Sem furo.
- **Duas Vanguardas no mesmo alvo** — cada uma tem a sua; Expor a Guarda diz que consome mesmo com vantagem prévia. Sem furo.
- **Âncoras numéricas** — fatia 5,08 e 1 PE = 5,14 (peça 5 §4), condições 8,45 · 3,45 · 39,20 · 132,15 (peça 19 §2.2), vantagem 25 pp, 10,5 rodadas por dia, maestria 1/2/3/4 em 2–9/10–17/18–25/26–30 (manual 10), CD 8 + atributo + maestria (manual 10), PE 10 → 150 da Vanguarda (peça 1 §5.3) — todas batem.
- **Não Cede** — texto da pasta bate com o manual 35 e com `DESENHO-caminhos.md` (qualquer TR, maestria usos por descanso curto, uma por rodada).
- **Nomes do Bastião contra o manual** — as mecânicas "mantidas" em `bastiao-nomes-aprovados.md` (Nem Um Arranhão = Não Pega, Passa Pra Mim, Alicerce, Ainda de Pé) batem com o texto do manual 35 onde o manual tem o texto. As que não batem são as da reforma, que não está no repo (item 2).
