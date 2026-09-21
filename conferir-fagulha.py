#!/usr/bin/env python3
"""Correção isolada do preço histórico de Fagulha; não altera fontes.

Premissas históricas, preservadas para comparar na mesma base:
- DESENHO-trilhas.md, linhas 800–810: dano 27, frequência 56%,
  pelo menos um soco acertando em 75% das rodadas elegíveis.
- DESENHO-trilhas.md, linha 835: a vantagem depende do soco acertar;
  lançar o Classe 0 exige a Ação de Atacar, não acertar o soco.
- Fatia 5,08; acerto 50%; vantagem eleva acerto a 75% nessa base.

Esta conta conserva o dano médio sem modelar dano adicional de críticos,
resistências, sobreposição de vantagem ou competição pela Ação Bônus.
Não atualiza simultaneamente o acerto para 55% nem o dia de 13 para
10,5 rodadas. Não é uma auditoria completa da Brasa publicada.
"""

from fractions import Fraction as F
from itertools import product


def conferir():
    fatia = F(508, 100)
    dano = F(27)
    frequencia = F(56, 100)
    acerto = F(1, 2)
    gatilho_vantagem = 1 - (1 - acerto) ** 2
    acerto_vantagem = 1 - (1 - acerto) ** 2

    base_antiga = dano * frequencia
    extra_antigo = dano * F(1, 2) * gatilho_vantagem * frequencia
    base_correta = dano * acerto * frequencia
    extra_correto = dano * (acerto_vantagem - acerto) * gatilho_vantagem * frequencia
    total = base_correta + extra_correto

    print('FAGULHA — correção isolada na base histórica')
    for nome, valor in (
        ('Base antiga', base_antiga),
        ('Vantagem antiga', extra_antigo),
        ('Total antigo reconstruído', base_antiga + extra_antigo),
        ('Base corrigida', base_correta),
        ('Vantagem corrigida', extra_correto),
        ('Total corrigido', total),
    ):
        print(f'{nome}: {float(valor):.6f} dano/rodada; {float(valor / fatia):.8f} fatias')

    # Dois dados para os socos e dois para o feitiço. Sem vantagem,
    # apenas o primeiro dado do feitiço conta. O segundo é marginalizado.
    sucessos = 0
    for soco1, soco2, feitico1, feitico2 in product(range(1, 21), repeat=4):
        dado = max(feitico1, feitico2) if soco1 >= 11 or soco2 >= 11 else feitico1
        sucessos += dado >= 11
    enumeracao = F(sucessos, 20**4)
    if enumeracao * dano * frequencia != total:
        raise AssertionError('A enumeração divergiu da fórmula.')
    if base_antiga + extra_antigo != 2 * total:
        raise AssertionError('A reprodução do erro histórico divergiu.')
    if total / fatia == (base_antiga + extra_antigo) / fatia:
        raise AssertionError('O preço sem desconto de acerto foi aceito como corrigido.')

    print(f'Enumeração: {sucessos}/{20**4} = {float(enumeracao):.6f} de acerto nas rodadas elegíveis')
    print(f'Preço corrigido, arredondado ao final: {float(total / fatia):.2f} fatias')
    print(f'Metade do valor publicado já arredondado: {float(F(408, 100) / 2):.2f} fatias')
    atalho_zip = dano * acerto * F(3, 4) / fatia
    print(f'Atalho do zip (75% de frequência, sem vantagem): {float(atalho_zip):.8f} fatias')

    # Conferência de que Retaliação já contém seu fator de acerto.
    dia = F(21, 2)
    usos_dia = F(6)
    forca = F(6)
    pe_dano = F(514, 100)
    retaliacao = (dano * acerto * usos_dia / dia + forca * pe_dano / dia) / fatia
    print(f'Retaliação reformada: {float(retaliacao):.8f} fatias')
    print('OK: fórmula e enumeração concordam; o preço histórico sem correção foi rejeitado.')


if __name__ == '__main__':
    conferir()
