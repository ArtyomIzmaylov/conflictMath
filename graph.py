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
        G.add_edge(zero_node, plus_node, color='#C10087')
    for minus_node in minus_nodes:
        G.add_edge(zero_node, minus_node, color='#C10087')


for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2 and df.loc[node1, 'col'] == df.loc[node2, 'col'] and df.loc[node1, 'col'] not in [0, '–', '+']:
            G.add_edge(node1, node2, color='F93E58')

# рисуем граф
pos = nx.circular_layout(G)
labels = {i: str(i) + '(' + str(df.loc[i]['col']) + ')' for i in df.index}
edge_colors = [G[u][v]['color'] for u,v in G.edges()]

node_colors = []
for node in G.nodes():
    if df.loc[node, 'col'] != 0:
        node_colors.append('#F93E58')
    else:
        node_colors.append('#9240D5')

nx.draw(G, pos, width=3, edgecolors='black', labels=labels, with_labels=True,
        font_size=16, edge_color=edge_colors,
        node_color=node_colors, node_size=2500, )
plt.axis('on')
plt.figtext(1, 0.01, 'Made by Artyom Gaibovich©', ha='right', va='bottom', size = 10)
plt.savefig('my_plot.png')
plt.show()