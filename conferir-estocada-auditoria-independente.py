"""Sensibilidades da Estocada no commit de referência, sem mudar habilidades.

As premissas editáveis ficam no RASCUNHO-revalidacao-estocada.md. Este script
recalcula os blocos publicados; --publicar só atualiza essas tabelas.
"""
from dataclasses import replace
from itertools import combinations
from pathlib import Path
import json
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parent
DOC = ROOT / 'RASCUNHO-revalidacao-estocada.md'
PUBLICAR = sys.argv[1:] == ['--publicar']
assert len(sys.argv) == 1 or PUBLICAR
old_argv = sys.argv
sys.argv = [sys.argv[0]]
m = runpy.run_path(str(ROOT / 'conferir-estocada-rotina.py'))
sys.argv = old_argv
text = DOC.read_text()
source = text


def block(start, end, rows):
    global text
    a, b = f'<!-- {start} -->', f'<!-- {end} -->'
    assert text.count(a) == text.count(b) == 1
    current = text.split(a)[1].split(b)[0]
    wanted = '\n' + '\n'.join(rows) + '\n'
    if PUBLICAR:
        text = text.replace(a + current + b, a + wanted + b)
    else:
        assert current == wanted, f'Divergência nas contas: {start}'


def num(x):
    return f'{x + 1e-10:.3f}'.replace('.', ',')


profiles = []
for name, weapon, p, adv, move, fixar in re.findall(
        r'^\| ([^|]+) \| (Yumi|Lâmina Longa|Lâmina Curta) \| (0\.\d+) \| (sim|não) \| (\d+) \| (sim|não) \|$', source, re.M):
    base = m['MELEE'] if weapon == 'Lâmina Longa' else m['REFERENCIA']
    if weapon == 'Lâmina Curta':
        base = replace(base, weapon_mean=m['MELEE'].weapon_mean - 2,
                       damage_normal=m['MELEE'].damage_normal - 2)
    cfg = replace(base, p_die=float(p), advantage=adv == 'sim', movement=float(move),
                  external_slow=fixar == 'sim', recovery=True, recovery_uses=3, capstone=True)
    profiles.append((name, cfg))
assert len(profiles) >= 5 and len({name for name, _ in profiles}) == len(profiles)

rows = ['| Cenário | Ataques | Interações com o Caminho | Total condicionado |',
        '|---|---:|---:|---:|']
results = {}
for name, cfg in profiles:
    raw = m['A_ataque_de_bonus_cru'](cfg, m['CONJURACOES_DIA'])
    interaction = m['A_dia'](cfg, m['CONJURACOES_DIA'], True) - m['A_dia'](cfg, m['CONJURACOES_DIA'], False)
    results[name] = {'ataques': raw, 'interacoes': interaction, 'total': raw + interaction}
    rows.append(f'| {name} | {num(raw)} | {num(interaction)} | {num(raw + interaction)} |')
block('inicio-auditoria-perfis', 'fim-auditoria-perfis', rows)

# A chance do feitiço usa a referência sem o +2 de Mirar do Batedor.
spell = json.loads((ROOT / 'estocada-troca-feitico-contas.json').read_text())
spell_value = spell['perfis']['corpo_a_corpo']['dano_feitico_esperado']
spell_mean = spell['fonte_feitico']['media_exata']
base_spell_p = m['MELEE'].p_die
spell_crit = m['NS']['module'].critical_chance(20, False)
assert abs(spell_value - (base_spell_p + spell_crit) * spell_mean) < 1e-9
tr_half = spell_mean * (base_spell_p + (1 - base_spell_p) / 2)
rows = ['| Resolução do feitiço `21d8` | Dano esperado por alvo |', '|---|---:|',
        f'| Ataque: {num(base_spell_p * 100)}% acerto, {num(spell_crit * 100)}% crítico | {num(spell_value)} |',
        f'| TR: {num(base_spell_p * 100)}% falha, metade no sucesso, sem crítico | {num(tr_half)} |']
block('inicio-auditoria-feitico', 'fim-auditoria-feitico', rows)

# O valor da condição é uma premissa de sensibilidade, não o preço de Bote.
neutral = next(cfg for name, cfg in profiles if name == 'Sem Batedor, com Fixar')
weapon_value = m['attack'](neutral)[1]
fights = []
for turns, casts, weight in m['_mistura'](m['CONJURACOES_DIA']):
    best_by_uses = {}
    for spell_turns in combinations(range(1, turns + 1), casts):
        for uses in range(casts + 1):
            for bote_turns in combinations(spell_turns, uses):
                half = tuple(t for t in spell_turns if t not in bote_turns)
                r = m['A_solve'](neutral, turns, 0., half_turns=half)
                value = r['benefit'] - r['opening_loss'] + (casts + uses) * weapon_value
                best_by_uses[uses] = max(best_by_uses.get(uses, float('-inf')), value)
    fights.append((weight, best_by_uses))
baseline = sum(weight * values[0] for weight, values in fights)


def bote(control, alternative):
    delta = min(0., control - alternative)  # sem Bote também escolhe a condição
    choices = [(weight, max(((v + uses * delta, uses) for uses, v in values.items())))
               for weight, values in fights]
    return (sum(weight * choice[0] for weight, choice in choices) - baseline) / m['DAY'] / m['SLICE'], \
        sum(weight * choice[1] for weight, choice in choices)


condition_values = [float(x) for x in re.findall(r'^\| (\d+(?:\.\d+)?) \|$', source, re.M)]
assert len(condition_values) >= 4
rows = ['| Valor esperado da condição | Bote incremental, fatias | Usos no dia |',
        '|---:|---:|---:|']
for control in condition_values:
    gain, uses = bote(control, spell_value)
    rows.append(f'| {num(control)} | {num(gain)} | {num(uses)} |')
block('inicio-auditoria-bote', 'fim-auditoria-bote', rows)
tr_case = bote(condition_values[-1], tr_half)
block('inicio-auditoria-bote-tr', 'fim-auditoria-bote-tr',
      ['| Condição esperada | Alternativa de dano com TR | Bote incremental | Usos no dia |',
       '|---:|---:|---:|---:|',
       f'| {num(condition_values[-1])} | {num(tr_half)} | {num(tr_case[0])} | {num(tr_case[1])} |'])

# Três combates concretos: gasto por luta, teto de reserva e descanso em ordem.
ledger_inputs = []
for label, casts_text, conducts_text in re.findall(
        r'^\| (Distribuído|Conjuração tardia) \| ([0-9, ]+) \| ([0-9, ]+) \|$', source, re.M):
    casts, conducts = [tuple(int(x) for x in s.split(',')) for s in (casts_text, conducts_text)]
    assert len(casts) == len(conducts) == 3
    assert sum(casts) == m['CONJURACOES_DIA']
    assert all(0 <= n <= 4 for n in conducts)
    ledger_inputs.append((label, casts, conducts))
assert len(ledger_inputs) == 2
cost = (m['REFERENCIA'].mastery + 1) // 2 + 1
spell_pe = spell['fonte_feitico']['pe_classe_7']
pe_rows = json.loads((ROOT / 'estocada-compasso-pe-contas.json').read_text())['orcamento_nivel_30']
base_max = next(row['pe_maximo_antes'] for row in pe_rows if row['descansos_curto_25_porcento'] == 0)
extra_max = next(row['pe_maximo_depois'] for row in pe_rows if row['descansos_curto_25_porcento'] == 0)


def ledger(cap, rests, casts_by_fight, conducts_by_fight):
    balance = cap
    spent, recovered, states = 0, 0, []
    for index, (casts, attempts) in enumerate(zip(casts_by_fight, conducts_by_fight)):
        debit = casts * spell_pe + attempts * cost
        balance -= debit
        spent += debit
        states.append(balance)
        if index + 1 in rests:
            heal = min(cap - balance, cap // 4)
            balance += heal
            recovered += heal
            states.append(balance)
    return {'spent': spent, 'recovered': recovered, 'states': states,
            'balance': balance, 'feasible': min(states) >= 0}


rows = ['| Plano | Reserva | Descanso após combate | Gasto | Recuperado | Saldo final | Viável |',
        '|---|---|---|---:|---:|---:|---|']
ledgers = {}
for plan, casts_by_fight, conducts_by_fight in ledger_inputs:
    for label, cap in (('Base', base_max), ('Com PE de Compasso', extra_max)):
        for rest_label, rests in (('nenhum', ()), ('1º', (1,)), ('2º', (2,)), ('1º e 2º', (1, 2))):
            row = ledger(cap, rests, casts_by_fight, conducts_by_fight)
            ledgers[(plan, label, rest_label)] = row
            rows.append(f"| {plan} | {label} | {rest_label} | {row['spent']} | {row['recovered']} | {row['balance']} | {'sim' if row['feasible'] else 'não'} |")
block('inicio-auditoria-pe', 'fim-auditoria-pe', rows)

uses_per_rest = m['REFERENCIA'].mastery // 2 + 1
assert 'Uma vez por cena, ao Concluir' in (ROOT / 'vanguarda-completo.md').read_text()
scenes_if_separate = len(ledger_inputs[0][1])
rows = ['| Descansos curtos | Teto de Persistência no dia | Teto de Conclusão Dupla, uma cena | Teto, três cenas |',
        '|---:|---:|---:|---:|']
for rest_count in range(3):
    rows.append(f'| {rest_count} | {(rest_count + 1) * uses_per_rest} | 1 | {scenes_if_separate} |')
block('inicio-auditoria-usos', 'fim-auditoria-usos', rows)

# Ferrão: Classe 0 resolve seu próprio acerto e crítico. Os dois tratamentos
# de Canalizar correspondem às passagens conflitantes da fonte.
manual_refino = (ROOT / 'referencia-jjk-project/sistema/05-material/livro/manual/45-aptidoes-e-refino.md').read_text()
dice = re.search(r'No refino `10` os dados viram `d6`: `(\d+)d6`', manual_refino)
assert dice
channel = int(dice.group(1)) * 3.5
from estocada_missao import sources
_, current_spells, _ = sources(m)
c0 = current_spells[0][1]
p_weapon = m['attack'](neutral)[0]
crit_weapon = m['NS']['module'].critical_chance(20, neutral.advantage)
c0_expected = (base_spell_p + spell_crit) * c0
gate = base_spell_p
ferrao_keep = gate * p_weapon * c0_expected
channel_expected = weapon_value - m['attack'](replace(neutral,damage_normal=neutral.damage_normal-channel))[1]
ferrao_replace = ferrao_keep - gate * channel_expected
rows = [f'| Leitura de Canalizar | Acréscimo por conclusão elegível | Teto se ocorrer {m["CONJURACOES_DIA"]} vezes, fatias |',
        '|---|---:|---:|',
        f'| Exclui dano na rodada de conjuração | {num(ferrao_keep)} | {num(m["CONJURACOES_DIA"] * ferrao_keep / m["DAY"] / m["SLICE"])} |',
        f'| Exclui apenas no golpe que carrega feitiço de dano | {num(ferrao_replace)} | {num(m["CONJURACOES_DIA"] * ferrao_replace / m["DAY"] / m["SLICE"])} |']
block('inicio-auditoria-ferrao', 'fim-auditoria-ferrao', rows)

attack_action = 2 * weapon_value
bonus_without_channel = weapon_value - channel_expected
turns = [('Atacar: dois ataques', attack_action, attack_action, 0),
         ('Conjurar Classe 0 + Compasso', c0_expected + bonus_without_channel,
          c0_expected + weapon_value, 0),
         ('Conjurar Classe 7, ataque + Compasso', spell_value + bonus_without_channel,
          spell_value + weapon_value, spell_pe),
         ('Conjurar Classe 7, TR com metade + Compasso', tr_half + bonus_without_channel,
          tr_half + weapon_value, spell_pe)]
rows = ['| Escolha no turno | PE | Dano, exclusão por rodada | Δ contra Atacar | Dano, exclusão só no golpe | Δ contra Atacar |',
        '|---|---:|---:|---:|---:|---:|']
for label, early, strike, pe in turns:
    rows.append(f'| {label} | {pe} | {num(early)} | {num(early - attack_action)} | '
                f'{num(strike)} | {num(strike - attack_action)} |')
block('inicio-auditoria-rotina', 'fim-auditoria-rotina', rows)

conclusions = json.loads((ROOT / 'estocada-conclusoes-magicas-contas.json').read_text())
rows = ['| Conclusão | Fatias por acionamento condicionado |', '|---|---:|']
for name, value in conclusions['em_fatias'].items():
    rows.append(f'| {name.replace("_", " ").title()} | {num(value)} |')
rows += ['', '| Dupla | Teto aditivo, fatias | Chance de ambas aplicarem |',
         '|---|---:|---:|']
assert len(conclusions['duplas_por_acionamento']) == 15
for name, value in conclusions['duplas_por_acionamento'].items():
    rows.append(f'| {name.replace("_", " ").replace("+", " + ").title()} | '
                f'{num(value)} | {num(100 * conclusions["duplas_chance_ambas"][name])}% |')
block('inicio-auditoria-conclusoes', 'fim-auditoria-conclusoes', rows)

short_cfg = m['Config'](**neutral.__dict__)
rows = ['| Opções no modelo curto | Conclusões de feitiço escolhidas no dia |',
        '|---|---:|']
for label, flags in (
        ('Só conclusões de arma', {}),
        ('Seis conclusões de feitiço disponíveis', {'magicas': True}),
        ('Conclusões de feitiço e Ferrão', {'magicas': True, 'ferrao': True}),
        ('Conclusões, Bote e Ferrão', {'magicas': True, 'bote': True, 'ferrao': True})):
    row = m['B_dia'](replace(short_cfg, compasso=True, **flags), m['CONJURACOES_DIA'])
    rows.append(f'| {label} | {num(row["magic_finishes"])} |')
block('inicio-auditoria-escolha-conclusao', 'fim-auditoria-escolha-conclusao', rows)

if PUBLICAR:
    DOC.write_text(text)
else:
    assert text == source
print('TUDO OK — perfis, Bote, PE, feitiço e Ferrão conferidos.')
