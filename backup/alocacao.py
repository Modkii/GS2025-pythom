def knapsack(focos, n_caminhoes, memo=None):
    """
    Resolve o problema da mochila (Knapsack) para alocar caminhões aos focos de incêndio.

    Args:
        focos (list): Lista de dicionários com 'gravidade' de cada foco.
        n_caminhoes (int): Número de caminhões disponíveis.
        memo (dict): Dicionário para memoização.

    Returns:
        int: A gravidade total máxima que pode ser atendida.
    """
    if memo is None:
        memo = {}

    key = (len(focos), n_caminhoes)

    if key in memo:
        return memo[key]

    if not focos or n_caminhoes == 0:
        return 0

    foco_atual = focos[0]

    # Não alocar neste foco
    sem = knapsack(focos[1:], n_caminhoes, memo)

    # Alocar neste foco
    com = foco_atual['gravidade'] + knapsack(focos[1:], n_caminhoes - 1, memo)

    memo[key] = max(sem, com)
    return memo[key]
