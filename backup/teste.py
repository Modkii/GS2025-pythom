import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo não-direcionado
G = nx.Graph()

# Adicionando nós
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Adicionando arestas
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# Desenhando o grafo
nx.draw(G, with_labels=True)
plt.show()
