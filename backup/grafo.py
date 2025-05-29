
import heapq

# Grafo com distância e direção entre regiões
grafo = {
    'Base': {
        'Sul':   {'distancia': 5, 'direcao': 'Sul'},
        'Norte': {'distancia': 7, 'direcao': 'Norte'}
    },
    'Sul': {
        'Base':  {'distancia': 5, 'direcao': 'Norte'},
        'Oeste': {'distancia': 4, 'direcao': 'Oeste'}
    },
    'Norte': {
        'Base':  {'distancia': 7, 'direcao': 'Sul'},
        'Oeste': {'distancia': 3, 'direcao': 'Oeste'}
    },
    'Oeste': {
        'Sul':   {'distancia': 4, 'direcao': 'Sul'},
        'Norte': {'distancia': 3, 'direcao': 'Norte'},
        'Leste': {'distancia': 6, 'direcao': 'Leste'}
    },
    'Leste': {
        'Oeste': {'distancia': 6, 'direcao': 'Oeste'}
    }
}

def dijkstra(grafo, inicio, destino):
   
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

    # Reconstrução do caminho
    caminho = []
    atual = destino

    while atual in prev:
        caminho.insert(0, atual)
        atual = prev[atual]

    if caminho:
        caminho.insert(0, inicio)

    return dist.get(destino, float('inf')), caminho

def mostrar_rota(grafo, caminho, custo):
   
    if not caminho or len(caminho) == 1:
        print("\\nRota impossível ou já está na região de destino.")
        return

    print("\\n=== Melhor Rota ===")
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        dados = grafo[origem][destino]
        direcao = dados['direcao']
        distancia = dados['distancia']

        print(f"De {origem} → {destino} | Direção: {direcao} | Distância: {distancia}")

    print(f"\\nCusto total: {custo}")
