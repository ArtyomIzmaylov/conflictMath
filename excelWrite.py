import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,3),(3,4),(4,1)])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[1], node_size=1000, edgecolors='black')

nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos)

plt.show()