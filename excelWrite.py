import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
data = [0, '–', 0, '+', '+', '+', '–', '–', '–', 0, '+', '+']
df = pd.DataFrame({'col': data}, index=range(1, len(data)+1))

G = nx.Graph()

# добавляем вершины в граф из индексов df
G.add_nodes_from(df.index)


for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2 and df.loc[node1, 'col'] == df.loc[node2, 'col']:
            G.add_edge(node1, node2)

# рисуем граф
pos = nx.circular_layout(G)
labels = {i: str(i) + '(' + str(df.loc[i]['col']) + ')' for i in df.index}

nx.draw(G, pos, labels=labels, with_labels=True, font_size=16, node_size=1500)
plt.axis('on')
plt.savefig('my_plot.png')
plt.show()