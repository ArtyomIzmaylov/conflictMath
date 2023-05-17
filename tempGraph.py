import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5)])

# Расположение вершин по кругу
pos = nx.circular_layout(G)

# Рисование графа
nx.draw(G, pos, with_labels=True)
plt.show()