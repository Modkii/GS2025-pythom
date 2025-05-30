import heapq

# Mapa de regiões interligadas com distâncias e direções
# Utilizado para calcular a rota mais curta entre duas localidades

grafo = {
    'Base': {
        'Norte': {'distancia': 7, 'direcao': 'Norte'},
        'Sul': {'distancia': 5, 'direcao': 'Sul'},
        'Leste': {'distancia': 6, 'direcao': 'Leste'},
        'Oeste': {'distancia': 6, 'direcao': 'Oeste'},
        'Nordeste': {'distancia': 8, 'direcao': 'Nordeste'},
        'Noroeste': {'distancia': 8, 'direcao': 'Noroeste'},
        'Sudeste': {'distancia': 10, 'direcao': 'Sudeste'},
        'Sudoeste': {'distancia': 10, 'direcao': 'Sudoeste'}
    },

    'Norte': {
        'Base': {'distancia': 7, 'direcao': 'Sul'},
        'Nordeste': {'distancia': 4, 'direcao': 'Leste'},
        'Noroeste': {'distancia': 4, 'direcao': 'Oeste'}
    },

    'Sul': {
        'Base': {'distancia': 5, 'direcao': 'Norte'},
        'Sudeste': {'distancia': 4, 'direcao': 'Leste'},
        'Sudoeste': {'distancia': 4, 'direcao': 'Oeste'}
    },

    'Leste': {
        'Base': {'distancia': 6, 'direcao': 'Oeste'},
        'Nordeste': {'distancia': 5, 'direcao': 'Norte'},
        'Sudeste': {'distancia': 5, 'direcao': 'Sul'}
    },

    'Oeste': {
        'Base': {'distancia': 6, 'direcao': 'Leste'},
        'Noroeste': {'distancia': 5, 'direcao': 'Norte'},
        'Sudoeste': {'distancia': 5, 'direcao': 'Sul'}
    },

    'Nordeste': {
        'Base': {'distancia': 8, 'direcao': 'Sudoeste'},
        'Norte': {'distancia': 4, 'direcao': 'Oeste'},
        'Leste': {'distancia': 5, 'direcao': 'Sul'}
    },

    'Noroeste': {
        'Base': {'distancia': 8, 'direcao': 'Sudeste'},
        'Norte': {'distancia': 4, 'direcao': 'Leste'},
        'Oeste': {'distancia': 5, 'direcao': 'Sul'}
    },

    'Sudeste': {
        'Base': {'distancia': 10, 'direcao': 'Noroeste'},
        'Sul': {'distancia': 4, 'direcao': 'Norte'},
        'Leste': {'distancia': 5, 'direcao': 'Norte'}
    },

    'Sudoeste': {
        'Base': {'distancia': 10, 'direcao': 'Nordeste'},
        'Sul': {'distancia': 4, 'direcao': 'Norte'},
        'Oeste': {'distancia': 5, 'direcao': 'Norte'}
    }
}

def dijkstra(grafo, inicio, destino):
    """
    Algoritmo de Dijkstra.
    Usa 'distancia' como custo e mantém 'direcao' para exibir o caminho.
    """

    heap = [(0, inicio)]
    dist = {inicio: 0}
    prev = {}

    while heap:
        custo_atual, atual = heapq.heappop(heap)

        if atual == destino:
            break

        for vizinho, dados in grafo.get(atual, {}).items():
            distancia = dados['distancia']
            novo_custo = custo_atual + distancia

            if vizinho not in dist or novo_custo < dist[vizinho]:
                dist[vizinho] = novo_custo
                prev[vizinho] = atual
                heapq.heappush(heap, (novo_custo, vizinho))

    caminho = []
    atual = destino

    while atual in prev:
        caminho.insert(0, atual)
        atual = prev[atual]

    if caminho:
        caminho.insert(0, inicio)

    return dist.get(destino, float('inf')), caminho


def mostrar_rota(grafo, caminho, custo):
    """
    Exibe o caminho mostrando direção e distância.
    """

    if not caminho or len(caminho) == 1:
        print("\nRota impossível ou já está na região de destino.")
        return

    print("\n=== Melhor Rota ===")

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        dados = grafo[origem][destino]
        direcao = dados['direcao']
        distancia = dados['distancia']

        print(f"De {origem} → {destino} | Direção: {direcao} | Distância: {distancia} km")

    print(f"\nCusto total da rota: {custo} km")
