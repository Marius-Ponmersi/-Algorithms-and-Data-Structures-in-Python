# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

matrix = [[random.randint(1, 100) for i in range(m)] for j in range(n)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

min_col = []
for i in range(m):
    min_col.append(sorted([line[i] for line in matrix])[0])
print(f'{min_col} - минимумы столбцов')
print(max(min_col))
