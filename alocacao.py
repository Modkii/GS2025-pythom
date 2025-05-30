def melhor_alocacao(chamados, n_caminhoes):
    """
    Seleciona os chamados mais prioritários com base em um score calculado.

    O score é calculado pela fórmula:
        score = (gravidade * 1.2) / distancia

    Args:
        chamados (list): Lista de dicionários contendo chamados com 'gravidade' e 'distancia'.
        n_caminhoes (int): Número de caminhões disponíveis para atendimento.

    Returns:
        tuple:
            - lista de chamados selecionados (os com maior score)
            - soma das gravidades atendidas
            - soma dos scores dos chamados alocados
    """
    if not chamados or n_caminhoes <= 0:
        return [], 0, 0.0

    chamados_com_score = []

    for chamado in chamados:
        gravidade = chamado.get('gravidade', 0)
        distancia = chamado.get('distancia', 1)
        score = (gravidade * 1.2) / distancia
        chamado_score = chamado.copy()
        chamado_score['score'] = score
        chamados_com_score.append(chamado_score)

    chamados_ordenados = sorted(chamados_com_score, key=lambda x: x['score'], reverse=True)
    selecionados = chamados_ordenados[:n_caminhoes]
    soma_gravidade = sum(c['gravidade'] for c in selecionados)
    soma_score = sum(c['score'] for c in selecionados)

    return selecionados, soma_gravidade, soma_score
