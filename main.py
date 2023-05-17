import pandas as pd
import numpy as np

from excelRead import matrix #импортирую [[]]
lst = [['+', '+', '+'], ['0', '0', '-'], ['+', '0', '+'], ['-', '0', '+']]
lst = matrix

n = len(lst[0])
print(n)
# создаем пустой DataFrame с нужными заголовками столбцов
df = pd.DataFrame(columns=[chr(i) for i in range(65, 65+len(lst[0]))])


for i, row in enumerate(lst, 1):
    df.loc[i] = row

# задаем заголовки строк
df.index = range(1, len(lst)+1)

print(df)

#2)
import itertools
combos = list(itertools.combinations(df.index, 2))
result = []
for combo in combos:
    print(combo[0], combo[1])
    new_row = df.loc[combo[0]] + df.loc[combo[1]]
    result.append(new_row)
df_result = pd.DataFrame(result, columns=[chr(i) for i in range(65, 65+len(lst[0]))])
df_result.index = combos
print(df_result)

#3
temp_arr = []
c = 1
for combo in combos:
    new_row = df.loc[combo[0]] + df.loc[combo[1]]
    x = new_row.values
    print(x)
    temp_arr.append(list(new_row[new_row.isin(['0+','0-','+0','-0','+-','-+', '+–', '+–', '0–', '–0'])].index))
    c+=1
print(len(temp_arr), len(combos))


print(temp_arr)

#4
new_combos = []
for i in range(len(combos)):
    new_combos.append([combos[i], temp_arr[i]])

print(new_combos)

#5)


# создаем пустой DataFrame размером M*M
df_new = pd.DataFrame(np.zeros((len(df), len(df))))
df_new.index = range(1, len(lst)+1)
df_new.columns = range(1, len(lst)+1)

#6
df_new.loc[1,1] = None
for combo in new_combos:
    df_new.loc[combo[0][1], combo[0][0]] = ",".join(combo[1])
    df_new.loc[combo[0][0], combo[0][1]] = None
    df_new.loc[combo[0][1], combo[0][1]] = None
print(df_new)
df_new.to_excel('./templates/firstTable.xlsx')

#7
df_new.loc[1,1] = None
for combo in new_combos:
    df_new.loc[combo[0][1], combo[0][0]] = len(combo[1]) / n
    df_new.loc[combo[0][0], combo[0][1]] = None
    df_new.loc[combo[0][1], combo[0][1]] = None

print(df_new)
df_new.to_excel('./templates/secondTable.xlsx')

