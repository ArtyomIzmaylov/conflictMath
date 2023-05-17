import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = [0, '–', 0, '+', '+', '+', '–', '–', '–', 0, '+', '+']
df = pd.DataFrame({'col': data}, index=range(1, len(data)+1))

G = nx.Graph()

# добавляем вершины в граф из индексов df
G.add_nodes_from(df.index)

# соединяем 0 с вершинами +/-/-
zero_nodes = [node for node in G.nodes() if df.loc[node, 'col']==0]
plus_nodes = [node for node in G.nodes() if df.loc[node, 'col']=='+']
minus_nodes = [node for node in G.nodes() if df.loc[node, 'col']=='–']

for zero_node in zero_nodes:
    for plus_node in plus_nodes:
        G.add_edge(zero_node, plus_node)
    for minus_node in minus_nodes:
        G.add_edge(zero_node, minus_node)


for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2 and df.loc[node1, 'col'] == df.loc[node2, 'col'] and df.loc[node1, 'col'] not in [0, '–', '+']:
            G.add_edge(node1, node2)

# рисуем граф
pos = nx.circular_layout(G)
labels = {i: str(i) + '(' + str(df.loc[i]['col']) + ')' for i in df.index}

nx.draw(G, pos, labels=labels, with_labels=True, font_size=16, node_size=1500)
plt.axis('on')
plt.savefig('my_plot.png')
plt.show()