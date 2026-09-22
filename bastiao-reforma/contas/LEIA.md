# As contas, uma por rodada de decisão

Estes scripts são o rastro do trabalho, não uma sequência para rodar. Cada um
responde **uma** pergunta que apareceu numa rodada, e vários foram escritos
antes de um achado que mudou a base — então alguns estão **superados de
propósito**, e ficam aqui para que a correção seja auditável.

O que vale como verdade é o `conferir-dano-movido.py`, na pasta acima: ele
reproduz todo número do documento e falha se algum deixar de bater.

- `nv15-bastiao.py` · `menu-nv15.py` · `pecas-nv2.py` · `custo-no-corpo.py`
  As primeiras rodadas, quando o nível 2 ainda era a `Interposição`.
- `encarar.py` · `converter-mover-dano.py`
  A rota longa, que tentava preçar por **queda evitada**. **Abandonada**, e o
  `converter-mover-dano.py` usa a `Rotina` de `108` onde o certo era o `78,75`
  contra chefe — é o erro de coluna descrito no LEIA-PRIMEIRO.
- `corpo-de-pe.py` · `tanque-direto.py`
  Onde a unidade trocou de *queda* para *golpe tancado* e a taxa de `0,30` saiu.
- `encarar-nv2.py` · `preco-nv2-final.py` · `degraus-15-23-30.py` ·
  `degraus-verbos.py` · `nv15-bloquear.py` · `nv15-frontier-nv30.py` ·
  `bloquear-frequencia.py` · `conserto-bloquear.py` · `bloquear-sozinho.py` ·
  `nv15-grade.py` · `kit-final.py`
  O fechamento do Caminho.
- `muro.py` · `rerrolar.py`
  A Trilha `Muro`, e a rerrolagem forçada que foi **descartada** por custar
  `5,34` no nível 2 sozinho.
