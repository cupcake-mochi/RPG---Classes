"""Bote: comparar a escolha de feitiço de dano com feitiço de condição sem dano.

Usa o mesmo otimizador de arma do Caminho completo. O valor próprio da condição
é um parâmetro de sensibilidade, não um preço criado por este validador.
"""
from dataclasses import replace
from itertools import combinations
from pathlib import Path
import json
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parent
PUBLICAR = sys.argv[1:] == ['--publicar']
assert len(sys.argv) == 1 or PUBLICAR, 'Uso: conferir-estocada-troca-feitico.py [--publicar]'
original_argv = sys.argv
sys.argv = [sys.argv[0]]  # O script da rotina tem opções próprias.
model = runpy.run_path(str(ROOT / 'conferir-estocada-rotina.py'))
sys.argv = original_argv
previous = json.loads((ROOT / 'estocada-orcamento-cenarios-contas.json').read_text())
path_value = json.loads((ROOT / 'estocada-rotina-contas.json').read_text())
pe_rows = json.loads((ROOT / 'estocada-compasso-pe-contas.json').read_text())['orcamento_nivel_30']
manual = (ROOT / 'referencia-jjk-project/sistema/05-material/livro/manual/40-fundamento.md').read_text()
row = next(line for line in manual.splitlines() if re.match(r'^\| \*\*7\*\* \|', line))
cells = [cell.strip().replace('**', '') for cell in row.strip('|').split('|')]
spell_pe = int(cells[2])
match = re.search(r'(\d+)d(\d+) = (\d+)', row)
assert match, 'Dano cheio da Classe 7 ausente na fonte'
dice, faces, printed = map(int, match.groups())
spell_mean = dice * (faces + 1) / 2
assert abs(spell_mean - printed) <= .5, 'Média de dados não reproduz o arredondamento do manual'
day, slice_value, casts = model['DAY'], model['SLICE'], model['CONJURACOES_DIA']
assert casts == 7
pe_max = model['PE_POR_NIVEL_VANGUARDA'] * model['NIVEL']
short_rest_base = pe_max // 4
pe_zero = next(row for row in pe_rows if row['descansos_curto_25_porcento'] == 0)
assert pe_zero['pe_maximo_antes'] == pe_max
assert pe_zero['recuperacao_antes'] == short_rest_base
conduct_pe = (model['REFERENCIA'].mastery + 1) // 2 + 1
one_rest_max_cost = casts * spell_pe + 3 * 4 * conduct_pe
assert one_rest_max_cost <= pe_max + short_rest_base
assert 5 * spell_pe + 2 * 4 * conduct_pe <= pe_max  # descanso após a segunda luta

output = {
    'fonte_feitico': {'dados': f'{dice}d{faces}', 'media_exata': spell_mean,
                      'media_arredondada_manual': printed, 'pe_classe_7': spell_pe},
    'missao': {'conjuracoes_referencia': casts, 'rodadas_referencia': day,
               'pe_base': pe_max, 'pe_recuperado_um_descanso': short_rest_base,
               'pe_maximo_sete_feiticos_e_doze_conducoes': one_rest_max_cost,
               'um_descanso_suficiente': True},
    'perfis': {},
}

for profile, original in (('distancia', model['REFERENCIA']), ('corpo_a_corpo', model['MELEE'])):
    cfg = replace(original, recovery=True, recovery_uses=3, capstone=True)
    weapon_hit, weapon_value = model['attack'](cfg)
    spell_hit, spell_value = model['attack'](replace(cfg, spell_damage=spell_mean), spell=True)
    compasso = previous['cenarios']['Compasso atual'][profile]['marginal_fatias']
    both = previous['cenarios']['Ambos atuais'][profile]['marginal_fatias']
    fixed_spell_bote = both - compasso
    raw_bonus = path_value['caminho_completo'][profile]['compasso_ataque_cru']
    assert abs(raw_bonus - casts * weapon_value / day / slice_value) < 1e-9
    assert abs(compasso - (raw_bonus + model['A_dia'](cfg, casts, True)
                           - model['A_dia'](cfg, casts, False))) < 1e-9
    conduct_pe_expected = 0.
    for turns, spells, weight in model['_mistura'](casts):
        options = []
        for spell_turns in combinations(range(1, turns + 1), spells):
            result = model['A_solve'](cfg, turns, 0., half_turns=spell_turns)
            options.append((result['benefit'] - result['opening_loss'], result['pe']))
        conduct_pe_expected += weight * max(options)[1]

    # Sem Bote, escolhe-se o melhor feitiço. Com Bote, trocar por controle
    # pode custar o dano que o feitiço anterior causaria.
    fights = []
    for turns, spells, weight in model['_mistura'](casts):
        best_by_bote = {n: None for n in range(spells + 1)}
        for spell_turns in combinations(range(1, turns + 1), spells):
            for n in range(spells + 1):
                for bote_turns in combinations(spell_turns, n):
                    half = tuple(t for t in spell_turns if t not in bote_turns)
                    result = model['A_solve'](cfg, turns, 0., half_turns=half)
                    value = (result['benefit'] - result['opening_loss']
                             + (spells + n) * weapon_value)
                    if best_by_bote[n] is None or value > best_by_bote[n]:
                        best_by_bote[n] = value
        fights.append((weight, best_by_bote))
    no_bote = sum(weight * best[0] for weight, best in fights)

    def gain(condition_value):
        # Quando o controle já vale mais que o dano, o feitiço sem dano seria
        # escolhido até sem Bote. Só há perda de alternativa no caso oposto.
        spell_difference = min(0., condition_value - spell_value)
        best = [(weight, max((value + n * spell_difference, n)
                             for n, value in choices.items()))
                for weight, choices in fights]
        value = sum(weight * chosen[0] for weight, chosen in best)
        uses = sum(weight * chosen[1] for weight, chosen in best)
        return {'marginal_fatias': (value - no_bote) / day / slice_value,
                'usos_dia': uses}

    assert abs(gain(spell_value)['marginal_fatias'] - fixed_spell_bote) < 1e-9
    cases = {label: gain(value) for label, value in
             (('zero', 0), ('20', 20), ('40', 40), ('50', 50), ('igual_ao_dano', spell_value))}
    extra_initial = pe_zero['pe_extra_disponivel']
    pe_left_no_rest = pe_max + extra_initial - casts * spell_pe
    upper_no_rest = (raw_bonus + model['A_dia'](cfg, casts, True, pe_rate=10)
                     + 10 * pe_left_no_rest / day / slice_value)
    if profile == 'distancia':
        assert upper_no_rest < 5.50
    output['perfis'][profile] = {
        'chance_arma': weapon_hit, 'dano_arma_esperado': weapon_value,
        'chance_feitico': spell_hit, 'dano_feitico_esperado': spell_value,
        'compasso_ataque_cru_fatias': raw_bonus,
        'compasso_interacao_caminho_fatias': compasso - raw_bonus,
        'compasso_total_fatias': compasso,
        'bote_mesmo_feitico_fatias': fixed_spell_bote,
        'cenarios': cases,
        'pe_conducoes_esperado_sem_cota': conduct_pe_expected,
        'limite_superior_compasso_sem_descanso': upper_no_rest,
    }

pe_two = next(row['fatias_nominais'] for row in pe_rows if row['descansos_curto_25_porcento'] == 2)
output['pe_nominal_dois_descansos_fatias'] = pe_two
assert output['perfis']['distancia']['compasso_total_fatias'] > 5.50

def comma(n):
    return f'{n:.3f}'.replace('.', ',')

lines = ['| Valor esperado do feitiço de condição sem dano | Bote: distância | Usos/dia | Bote: corpo a corpo | Usos/dia |',
         '|---|---:|---:|---:|---:|']
for label, display in (('zero', '0'), ('20', '20'), ('40', '40'), ('50', '50'),
                       ('igual_ao_dano', 'Igual ao feitiço de dano')):
    ranged = output['perfis']['distancia']['cenarios'][label]
    melee = output['perfis']['corpo_a_corpo']['cenarios'][label]
    lines.append(f"| {display} | {comma(ranged['marginal_fatias'])} | {comma(ranged['usos_dia'])} | "
                 f"{comma(melee['marginal_fatias'])} | {comma(melee['usos_dia'])} |")
report = ROOT / 'RASCUNHO-revalidacao-estocada.md'
start, end = '<!-- inicio-contas-troca-feitico -->', '<!-- fim-contas-troca-feitico -->'
text = report.read_text()
assert text.count(start) == text.count(end) == 1
current = text.split(start)[1].split(end)[0]
expected = '\n' + '\n'.join(lines) + '\n'
if PUBLICAR:
    report.write_text(text.replace(start + current + end, start + expected + end))
else:
    assert current == expected, 'Tabela da troca de feitiço diverge da conta'
output['checagem'] = 'Fonte do feitiço, regressão do Caminho e troca de feitiço: OK.'
(ROOT / 'estocada-troca-feitico-contas.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(output['checagem'])
