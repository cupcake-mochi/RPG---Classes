"""Sequência de Combate no nível 2: a conta que a pasta não fez.

Reproduz o achado 7 de revisao-cetica.md. Toda a precificação da pasta é no
nível 30 (dois ataques, Mirar, 87,75% de acerto). Aqui é a ficha de nível 2:
um ataque por turno, 55% de acerto, katana 1d8 + 3 + 1d4 (escada do manual),
maestria 1 (abertura perde 1d4, condução custa 2 PE), erro encerra, sem
Persistência. Luta de três turnos, uma rota por vez, sem otimizador.

Nenhum número aqui é decisão: é o que a regra declarada rende no nível 2.
"""
HIT = .55              # acerto de referência (peça 26 §3.1)
FAIL_TR = .35          # falha no TR do alvo de referência, como na auditoria v1
DIE_WEAPON = 4.5       # 1d8
ATTR = 3
DIE_CHANNEL = 2.5      # 1d4 de Canalizar, refino 1 pela escada do MANUAL
DAMAGE = DIE_WEAPON + ATTR + DIE_CHANNEL          # 10,0
OPENING_LOSS = 2.5     # 1d4, maestria 1 (mínimo do golpe é 5, nunca clipa)
CONDUCT_PE = 2         # metade da maestria p/ cima + 1
PE_RATE = 5.14         # 1 PE em equivalentes (peça 5 §4)
DERRUBADA = 8.45 + .90 # condição + empurrão opcional (peça 19)
CRIT_STEP = .05        # margem 20 -> 19–20

def rota_derrubada():
    """T1 abrir, T2 conduzir se abriu, T3 concluir Derrubada se conduziu."""
    p_open = HIT
    p_conduct = p_open * HIT
    p_applied = p_conduct * HIT * FAIL_TR
    lost = p_open * OPENING_LOSS
    pe = p_open * CONDUCT_PE                     # pago antes de rolar, só se abriu
    benefit = p_applied * DERRUBADA
    net = benefit - lost
    print("Rota Abrir -> Conduzir -> Concluir Derrubada, luta de 3 turnos:")
    print(f"  P(abre)={p_open:.3f}  P(condução acerta)={p_conduct:.3f}  P(Derrubado aplicado)={p_applied:.3f}")
    print(f"  dano perdido esperado={lost:.2f}   PE esperado={pe:.2f} de 10   benefício esperado={benefit:.2f} equiv.")
    print(f"  líquido SEM cobrar PE = {net:+.2f} equiv por luta ; cobrando PE a {PE_RATE} = {net - pe*PE_RATE:+.2f}")
    return net

def rota_impacto(channel_doubles):
    """T1 abrir, T2 Golpe de Impacto se abriu (só melhora a margem crítica)."""
    extra_on_crit = DIE_WEAPON + (DIE_CHANNEL if channel_doubles else 0)
    gain_per_try = CRIT_STEP * extra_on_crit
    gain = HIT * gain_per_try                    # só tenta Impacto se abriu
    lost = HIT * OPENING_LOSS
    tag = "dados de Canalizar dobrando" if channel_doubles else "Canalizar NÃO dobra (regra da pasta)"
    print(f"Rota Abrir -> Golpe de Impacto, {tag}:")
    print(f"  ganho da margem crítica = {gain:+.2f} ; custo da abertura = {lost:.2f} ; líquido = {gain - lost:+.2f} por tentativa")
    normal = 2 * HIT * DAMAGE
    with_seq = HIT * (DAMAGE - OPENING_LOSS) + HIT * DAMAGE + gain
    print(f"  dois ataques normais nos mesmos 2 turnos: {normal:.2f} ; abrir + Impacto: {with_seq:.2f}")
    return gain - lost

if __name__ == "__main__":
    a = rota_derrubada()
    b = rota_impacto(channel_doubles=True)   # o número que o agente reportou (-1,18)
    c = rota_impacto(channel_doubles=False)  # com a regra declarada na pasta
    assert a < 0 and b < 0 and c < 0, "alguma rota do nível 2 ficou positiva — reveja"
    print("\nTodas as rotas negativas no nível 2, com ou sem Canalizar dobrando: OK.")
