import pandas as pd
from readFile.excelRead import df as row
from readFile.readText import symbol
from makeTable.makeTable import makeTable
from drawGraph.drawGraphs import makeGraph, drawGraph

symbol = symbol
data = row[symbol].values.astype(str).tolist()
data = [str(i).replace('0', '0') for i in data]
data = [element.replace('–', '-') for element in data]
df = pd.DataFrame({'col': data}, index=range(1, len(data)+1))


makeTable()
drawGraph(df, makeGraph('+', df), '+', 'Positive')
drawGraph(df, makeGraph('-', df), '-', 'Negative')
drawGraph(df, makeGraph('0', df), '0', 'Neutral')
input('Нажмите Enter для выхода\n')
