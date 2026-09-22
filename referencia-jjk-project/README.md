# Referência — cópia parcial do JJK---Project

Esta pasta é uma **fotografia somente-leitura** de 22 arquivos do repositório principal do sistema, [cupcake-mochi/JJK---Project](https://github.com/cupcake-mochi/JJK---Project), tirada em **21/09/2026 na v0.263** (commit `ec25975`).

Ela existe por um motivo só: os documentos da raiz deste repositório citam esses arquivos como fonte de número e de regra, e quem lê a releitura precisa conseguir abrir a fonte sem clonar o projeto inteiro. **Nada aqui é editado**. Se um arquivo daqui discordar do JJK---Project, o JJK---Project vence — ele é o dono; isto é cópia.

Os links internos desses arquivos apontam para a estrutura do repositório original, então muitos não vão resolver daqui. É esperado.

## O que tem, e por que

**Raiz**

| Arquivo | Por que está aqui |
|---|---|
| `README-jjk-project.md` | o README do projeto principal. A seção *"Nove lições que custaram erro"* é o que mais importa — ela explica o jeito de trabalhar que a releitura tenta seguir. Renomeado pra não virar o README desta pasta no GitHub. |
| `DESENHO-caminhos.md` | a régua dos Caminhos: **3 fatias, degraus em 2 · 7 · 15 · 30**. A reforma sobe pra 5 fatias e acrescenta o nível 23 — decisão de 17/09, em `bastiao-reforma/`; o porte reescreve esta linha. |
| `DESENHO-trilhas.md` | a régua das Trilhas, 5 fatias. A conta histórica de Fagulha está na linha ~800. |
| `DESENHO-manhas.md` | as treze Manhas originais da Escola de Arma, que a releitura reduz a quatro. |

**`sistema/03-mecanica/` — as peças técnicas**

| Peça | O que a releitura tira dela |
|---|---|
| `01-atributos-acerto-defesa.md` | PE por nível (5 × nível na Vanguarda), energia temporária (§5.1.2), arredondamento (§5.4), CD = 8 + atributo + maestria, e a regra *"PE sem atributo"* que o Compasso reformado contraria |
| `05-caminho-e-combate-sem-feitico.md` | 1 PE = 5,14 equivalentes; +1 de Defesa = 3,39 por rodada; o soco cru de 11,50 = 2,26 fatias |
| `06-caminhos-e-trilhas.md` | a regra vigente dos Caminhos e a tabela do nível 7 (onde Não Pega aparece na Vanguarda) |
| `10-descanso-e-recuperacao.md` | descanso curto = 25%; definição de *cena* (§5) e a regra *"gatilho de combate desce para por descanso curto"* |
| `11-aptidoes-e-refino.md` | a escada de Refino (§6.9) — que diverge da do manual |
| `14-equipamento.md` | dados das armas e as treze categorias |
| `18-progressao.md` | tabela de nível: o que chega em cada degrau |
| `19-dano-e-condicoes.md` | **a régua de condições**: Lento 39,20 · Impedido 132,15 · Derrubado 8,45 · Desarmado 3,45 · 1 m = 0,60 · cobertura |
| `23-bloquear.md` | Bloquear rola 2d10 e não é Reação |
| `26-bestiario.md` | o inimigo de referência: Defesa 20, golpe de chefe 73 |
| `RASCUNHO-trilhas.md` | a régua de Trilhas e a taxa de disparo por entrada |

**`sistema/05-material/livro/manual/` — o texto publicado pro jogador**

| Capítulo | O que a releitura tira dele |
|---|---|
| `07-glossario.md` | termos fechados — é contra isso que o `conferir-nomes.py` mata nome |
| `10-como-jogar.md` | crítico próprio do feitiço que acompanha a arma |
| `11-o-turno.md` | ações, Agarrar e Derrubar |
| `35-caminhos-e-trilhas.md` | **o texto atual de Bastião, Vanguarda e Estocada** — o que a releitura substitui |
| `40-fundamento.md` | Classe 0 = 6d8 no nível 30; Melhorias `Precisão` e `Guarda`, que colidem com as Manhas novas |
| `45-aptidoes-e-refino.md` | escada de Refino do manual; *"golpe que carrega feitiço não soma Canalizar"* |
| `47-bencaos-e-lapidacao.md` | Estímulo Muscular |

## O que ficou de fora, de propósito

- `sistema/ESTADO-ATUAL.md` e `logs/CHANGELOG.md` — são o ponto de retomada e o histórico do projeto principal. Grandes, e só fazem sentido lá. As versões citadas na releitura (v0.147, ataque extra exige a Ação de Atacar; v0.221, categoria Dupla morreu) estão no CHANGELOG de lá.
- `sistema/03-mecanica/conferir-nomes.py` — o validador de nomes lê um `.docx` do manual e o glossário por caminho relativo. Não roda fora do repositório principal. Pra triar nome, rode lá.
- `sistema/99-arquivo/` — material morto. O projeto pede pra não ler de lá.
- Os outros validadores (`conferir-*.py`) — mesma razão do de nomes.
