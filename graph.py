import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
data = [0, '–', 0, '+', '+', '+', '–', '–', '–', 0, '+', '+']
df = pd.DataFrame({'col': data}, index=range(1, len(data)+1))

G = nx.Graph()

# добавляем вершины в граф из индексов df
G.add_nodes_from(df.index)
labels = {i: str(i) + '(' + str(df.loc[i]['col']) + ')' for i in df.index}
nx.draw(G, with_labels=True, labels=labels, font_size=16, node_size = 1500)
plt.show()
# рисуем граф