# -*- coding: utf-8 -*-
import pandas as pd

# Укажите путь к вашему файлу Excel
path = 'C:/Саморазвитие/Программирование/Python course/conflictMath/table.xlsx'

df = pd.read_excel(path)
print(df)
matrix = df.iloc[:, 1:].values.astype(str).tolist()
print(df['A'].tolist())
print(matrix)



