# -*- coding: utf-8 -*-
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
            if df.loc[node1, 'col'] == 0:  # если значение в ячейке равно "0", добавляем пунктирное ребро
                G.add_edge(node1, node2, color='yellow', style='dashed')
            if df.loc[node1, 'col'] == '+':  # если значение в ячейке равно "0", добавляем пунктирное ребро
                G.add_edge(node1, node2, color='green', style='dashed')
            if df.loc[node1, 'col'] == '–' or df.loc[node1, 'col'] == '-':
                G.add_edge(node1, node2, color='blue', style='dashed')


# рисуем граф
pos = nx.circular_layout(G)
labels = {i: str(i) + '(' + str(df.loc[i]['col']) + ')' for i in df.index}
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
styles = [G[u][v]['style'] for u,v in edges]
nx.draw(G, pos, labels=labels, with_labels=True, width = 3, font_size=16, node_size=1500, edge_color=colors, style=styles)
plt.axis('on')
plt.savefig('../templates/my_plotUnion.png')
plt.show()