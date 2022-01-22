#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []
for i in range(5):
    line = []
    for j in range(1, 4):
        line.append(int(input('Введите челое число: ')))
        if j == 3:
            line.append(sum(line))
    matrix.append(line)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

