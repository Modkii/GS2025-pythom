def melhor_alocacao(chamados, n_caminhoes):
    """
    Seleciona os melhores chamados com base em:
        pontuação = (gravidade × 1.2) / distancia

    Args:
        chamados (list): Lista de dicionários contendo 'gravidade' e 'distancia'
        n_caminhoes (int): Número máximo de caminhões disponíveis

    Returns:
        selecionados (list): Lista de chamados escolhidos
        soma_gravidade (int): Soma das gravidades dos chamados escolhidos
        soma_score (float): Soma da pontuação total (score) dos escolhidos
    """

    if not chamados or n_caminhoes <= 0:
        return [], 0, 0.0

    chamados_com_score = []

    for chamado in chamados:
        gravidade = chamado.get('gravidade', 0)
        distancia = chamado.get('distancia', 1)  # Evita divisão por zero

        # Calcula a pontuação com base na fórmula
        score = (gravidade * 1.2) / distancia

        chamado_score = chamado.copy()
        chamado_score['score'] = score

        chamados_com_score.append(chamado_score)

    # Ordena os chamados com base no maior score
    chamados_ordenados = sorted(chamados_com_score, key=lambda x: x['score'], reverse=True)

    # Seleciona os n primeiros (melhores)
    selecionados = chamados_ordenados[:n_caminhoes]

    soma_gravidade = sum(c['gravidade'] for c in selecionados)
    soma_score = sum(c['score'] for c in selecionados)

    return selecionados, soma_gravidade, soma_score