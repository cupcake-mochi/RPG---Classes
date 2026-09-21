> **Relatório de agente, 20/09/2026.** Produzido numa sessão do Claude Code contra o JJK---Project na v0.261. Os achados #3.1 (Caminho tem 3 fatias) e #8 (escada de Refino diverge) foram conferidos à mão depois, e batem. Nenhum arquivo foi alterado por esta conferência.

# Cruzamento de constantes — scripts `conferir-*` da pasta de trabalho vs. repositório do sistema

## Tabela

| # | constante | valor no script (arquivo) | documento dono (caminho:linha) | valor no dono | veredito |
|---|---|---|---|---|---|
| 1 | 1 fatia = dano/rodada nível 30 | `FATIA=5.08` / `SLICE=5.08` (`conferir-vanguarda.py:13`, `conferir-vanguarda-v2.py:95`, `conferir-nao-cede.py:14`, `conferir-estocada-auditoria.py:18`, `conferir-estocada-compasso-pe.py:14`) | `sistema/03-mecanica/19-dano-e-condicoes.md:70` (cita `DESENHO-trilhas.md` como dono); valor primário em `DESENHO-trilhas.md:628` | `5,08` de dano por rodada | BATE |
| 2 | 1 PE = equivalentes | `PE_EQ=5.14` / `PE_RATE=5.14` (`conferir-vanguarda.py:14`, `conferir-vanguarda-v2.py:96`, `conferir-estocada-compasso-pe.py:14`) | `sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md:145`; também `11-aptidoes-e-refino.md:438`, `22-pactos.md:103`, `26-bestiario.md:533` | `1 PE por rodada = 5,14 de dano por rodada` | BATE |
| 3.1 | Orçamento do **Caminho** = 5 fatias | `vanguarda-orcamento.md` (tabela: "Orçamento total do Caminho \| 5,00"); embutido em `conferir-nao-cede.py:96-97` | `08-criacao-de-personagem.md:241`; `20-tecnica-marcial.md:167,11034`; `ESTADO-ATUAL.md:989,994` | **`3` fatias** (não 5) | **NÃO BATE** |
| 3.2 | Orçamento da **Trilha** = 5 fatias, separado | usado em toda a pasta como teto de 5,00 por Trilha | `DESENHO-trilhas.md:628`; `ESTADO-ATUAL.md:994` | `5,00` fatias por Trilha | BATE |
| 4 | Dia de referência: 3 combates de 3–4 turnos, peso igual = 10,5 rodadas | `ROUNDS=10.5` (`conferir-estocada-compasso-pe.py:14`); `product((3,4),repeat=3)` em `conferir-nao-cede.py` | `10-descanso-e-recuperacao.md:87`; `01-atributos-acerto-defesa.md:680-688` | 3 lutas/dia de graça; 3,4–4,0 rodadas/luta | BATE (simplificação declarada) |
| 5 | PE máximo Vanguarda = 5×nível (10@nv2, 150@nv30); Bastião = 120@nv30 | `base = 5 * level` (`conferir-estocada-compasso-pe.py:16`) | `01-atributos-acerto-defesa.md:424-426` | Vanguarda·Guia: 10→150; Bastião: 8→120 | BATE |
| 6 | Descanso curto recupera 25% do PE máx., arred. p/ baixo | `recovered = max(1, base // 4)` | `10-descanso-e-recuperacao.md:41,62,111` | 25%, arredonda p/ baixo, piso 1 | BATE |
| 7 | Maestria por faixa: 1(2–9) 2(10–17) 3(18–25) 4(26–30) | `POOL=4` (`conferir-nao-cede.py:16`); tabela em `vanguarda-precificacao-v2.md:38-42` | `01-atributos-acerto-defesa.md:30-32` (§2) | 1/2/3/4 nas mesmas faixas | BATE |
| 8 | Escada de Refino `CHANNEL={1:2.5,3:5.0,6:7.5,9:10.0,10:14.0}` | `conferir-estocada-auditoria.py:17` | (a) manual `45-aptidoes-e-refino.md:151`; (b) peça `11-aptidoes-e-refino.md:1091-1101` (§6.9) | (a) 1→1d4, 3→2d4, 6→3d4, 9→4d4, 10→4d6; (b) 1·2→0, 3→1d4, 6→2d4, 9→3d4, 10→4d6 | **DIVERGE ENTRE FONTES** |
| 9 | Classe 0 nível 30 = 6d8 (27); tabela 2d8·3d8·4d8·5d8·6d8 | `'c0_mean':27` (`conferir-estocada-auditoria.py:134`) | `40-fundamento.md:148-154` | nv1→2d8...nv25→6d8(27) | BATE |
| 10 | Armas: katana 1d8, espadão 1d12, Daikyū 1d10, rifle 2d8 sem atributo | `conferir-vanguarda.py:159-165` | `14-equipamento.md:1127,1129,1220,1227` | d8 / d12 / 1d10(+Destreza) / 2d8(nenhum atributo) | BATE |
| 11 | Acerto de referência 55%; Defesa 20; "peça 26 §3.1" | `p_die=.55` default | `26-bestiario.md:57-64` (§3.1) | Defesa 20 no nv30; acerto 50-55% | BATE |
| 12 | Falha de TR do inimigo de referência: 35% (v1) e 55% (v2+) | v1 `save_fail=.35`; v2+ `q_physical=.55,q_vigor=.55` | sem dono único — ver Achados | 35% = TR treinado de PC (`26-bestiario.md:64`); 55% = derivação não publicada verbatim | **DIVERGE ENTRE FONTES** |
| 13 | Mirar +2 acerto; vantagem s/ 65% = 87,75% | `p_die=.65,advantage=True` | `DESENHO-trilhas.md:246,253`; `19-dano-e-condicoes.md:60` | +2 acerto; vantagem=1−(1−p)² | BATE |
| 14 | Kokusen 20%; margem crítica natural 20; crítico feitiço 5% | `kokusen=.2`; `crit_chance=.05` | `45-aptidoes-e-refino.md:219`; `01-atributos-acerto-defesa.md:81` | refino10→20%; crítico padrão 5% | BATE |
| 15 | Lento = 39,20/rodada | `magnitudes['ritmo']=39.2` | `19-dano-e-condicoes.md:121` | `39,20` | BATE |
| 16 | Impedido = 132,15/rodada | `magnitudes['fixar']=132.15` | `19-dano-e-condicoes.md:114` | `132,15` | BATE |
| 17 | Derrubado = 8,45 (+0,90 empurrão) | `magnitudes['derrubada']=9.35`=8,45+0,90 | `19-dano-e-condicoes.md:122,213,77` | `8,45`; empurrão 1,5m=0,90 | BATE |
| 18 | Desarmado = 3,45 (inclui 3m) | `magnitudes['desarme']=3.45` | `19-dano-e-condicoes.md:125,259` | `3,45` | BATE |
| 19 | +1 Defesa = 3,39/rodada | `protect_value:float=3.39` | `05-caminho-e-combate-sem-feitico.md:143` | `3,39` | BATE |
| 20 | Movimento = 0,60/m | `.6` em `conferir-nao-cede.py` | `19-dano-e-condicoes.md:77,506` | "1 m vale 0,60" | BATE |
| 21.1 | Golpe do chefe de referência = 73 | `conferir-nao-cede.py` (`73/2`) | `26-bestiario.md:253` | golpe Desastre = 8d8+37 = 73 | BATE |
| 21.2 | Meia ação = 36,50 | `vanguarda-nao-cede.md:32` | derivado 73÷2 | 36,5 | BATE |
| 21.3 | 219 equivalentes negar rodada do chefe | `vanguarda-precificacao-inicial.md:88` | `19-dano-e-condicoes.md:72,106`; `26-bestiario.md:253` | 219=73×3 ações | BATE |
| 21.4 | 167 âncora de Recarga | `conferir-nao-cede.py` (`167/2`) | `26-bestiario.md:576` | golpe 67×2,5≈167 | BATE |
| 21.5 | 182,5 âncora Desastre/Recarga | `conferir-nao-cede.py` (`182.5/2`) | procurado e não achado em `19-dano-e-condicoes.md` e `26-bestiario.md` | — | **NÃO ACHEI** (é 73×2,5, extrapolação não escrita no repo) |
| 22.1 | Cobertura Parcial = +2/+2 | `cover=2`×.05 | `19-dano-e-condicoes.md:432` | +2 Defesa e +2 TR Físico | BATE |
| 22.2 | Cobertura Boa = ? | `cover=5`×.05 | `19-dano-e-condicoes.md:433` | +5 Defesa e +5 TR Físico | BATE |
| 23 | Ataque extra nv7 exige Ação de Atacar (v0.147) | assumido em `vanguarda-precificacao-v2.md:44` | `06-caminhos-e-trilhas.md:238-240`; manual `35-caminhos-e-trilhas.md:195`; CHANGELOG v0.147 | "exige a Ação de Atacar" | BATE |
| 24 | Golpe com feitiço/Kata não soma Canalizar/Estímulo | docstring `conferir-estocada-auditoria.py:35-36` | `45-aptidoes-e-refino.md:153` | "este dano não se soma por cima" | BATE |
| 25 | Feitiço que acompanha a arma tem acerto/crítico próprios | modelado em `conferir-estocada-auditoria.py` (`p_c0` separado de `p_weapon`) | `10-como-jogar.md:133` | "tem crítico próprio" | BATE |
| 26 | Energia temporária: gasta antes, não acumula, teto metade PE máx, some no fim da cena | citado em `conferir-estocada-compasso-pe.py` | `01-atributos-acerto-defesa.md:350-356` (§5.1.2) | idêntico | BATE |
| 27 | CD de TR = 8 + atributo + maestria | implícito no item 12 | `01-atributos-acerto-defesa.md:85`; `40-fundamento.md:62` | `8 + atributo + maestria` | BATE |
| 28 | Bloquear rola 2d10 e NÃO é reação | citado em `estocada-auditoria.md:135` | `23-bloquear.md:83,89` | "não gasta a sua Reação" | BATE |
| 29 | Não Cede: maestria/descanso curto, máx 1/rodada | regra citada em `conferir-nao-cede.py` | manual `35-caminhos-e-trilhas.md:198` | idêntico | BATE |
| 30 | Fagulha histórico 4,08=2,97+1,11; soco Bastião 56% | `conferir-fagulha.py` docstring | `DESENHO-trilhas.md:800-810` | idêntico | BATE (valor histórico citado para comparação, não afirmação do preço vigente) |

## Achados (NÃO BATE e DIVERGE ENTRE FONTES)

**#3.1 — Orçamento do Caminho: scripts usam 5,00; o repositório fecha em 3,00.** `vanguarda-orcamento.md` declara "Orçamento total do Caminho | 5,00" e `conferir-nao-cede.py` embute essa mesma suposição (`remaining_if_accepted=1.25` só fecha se o total for 5). O repositório diz o contrário, repetidamente: `08-criacao-de-personagem.md:241` — "o Caminho leva `3` fatias, a Trilha leva `5`"; `20-tecnica-marcial.md:167` — "Um Caminho custa `3` fatias na campanha inteira"; a mesma frase reaparece em `20-tecnica-marcial.md:11034` especificamente sobre a Vanguarda; `ESTADO-ATUAL.md:994` — "o Caminho leva `3` fatias e a Trilha leva `5`". Não achei nenhuma decisão registrada elevando esse teto para 5 na Vanguarda. As contas de trabalho somam 5,00 fatias de entregas de Caminho contra um teto publicado de 3,00 — ou seja, gastam 2,00 fatias além do que a régua do repositório permite.

**#8 — Escada de Refino: manual e peça 11 §6.9 realmente divergem.** Peça `11-aptidoes-e-refino.md:1091-1101`: refino 1·2→0; 3→1d4; 6→2d4; 9→3d4; 10→4d6. Manual `45-aptidoes-e-refino.md:151`: "1d4 no refino 1, 2d4 no 3, 3d4 no 6, 4d4 no 9. No refino 10... 4d6." O próprio arquivo de trabalho já sabia disso: `vanguarda-precificacao-inicial.md:34` — "Usada a escada do manual publicado. A peça técnica 11 §6.9 ainda tem uma tabela anterior... Essa divergência não foi corrigida no repositório." Confirmo que a divergência persiste hoje, e que `CHANNEL` em `conferir-estocada-auditoria.py:17` segue exatamente o manual, não a peça 11.

**#12 — Falha de TR "de referência": 35% vs. 55%.** `vanguarda-precificacao-inicial.md:108` rotula "Referência: acerto 55%, falha de TR 35%" e "Precisão de Batedor: acerto 87,75%, falha de TR 55%". A partir de `conferir-vanguarda-v2.py`, o personagem chamado "referência" nas auditorias passa a usar exatamente os números que antes eram do "Batedor" (55% de falha). Os dois valores são deriváveis de fórmulas fechadas no repositório — CD=8+atributo+maestria (`01-atributos-acerto-defesa.md:85`) e a curva Destreza/Defesa do inimigo (`26-bestiario.md:57-64`, que publica "TR treinado falha 35%" para um PC, não para o inimigo sem treino) — mas nenhum documento publica "55%" verbatim para esse cenário específico. É uma troca silenciosa de qual personagem-hipotético conta como "referência" entre a auditoria v1 e a v2+.

**#21.5 — 182,5 não aparece em nenhum documento do repositório.** Busquei `182,5`/`182.5` em `sistema/` inteiro e nos `DESENHO-*.md` da raiz; não há ocorrência. `vanguarda-nao-cede.md` documenta 73, 67 e 167 na tabela de sensibilidade mas não lista nem explica 182,5. É reconstituível como 73×2,5 (aplicando a regra "Recarga = 2,5× o golpe" de `26-bestiario.md:576` ao golpe de 73 em vez do golpe de 67 do exemplo do bestiário) — conta correta, mas número não publicado.

## Observações gerais

- Itens 15–22 (régua de condições/cobertura, peça 19) e 23–29 (regras estruturais) bateram integralmente, com citação literal.
- Item 30 bate como valor **histórico** — é exatamente o que `conferir-fagulha.py` audita para propor correção, não uma afirmação de preço vigente.
- Constantes extras notadas nos scripts, fora da lista mínima, consistentes com o já verificado: `recoil_value=5.40` (`conferir-vanguarda-v2.py:65`) e `magnitudes['resposta']=36.5` (mesmo valor da "meia ação" do item 21.2).
