# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
a = [random.randint(0, 100) for i in range(10)]
print(a)
max = 0
min = 100
for el in a:
    if el >= max:
        max = el
    if el <= min:
        min = el
imax = a.index(max)
imin = a.index(min)
print(f'Индекс максимального элемента: {imax}, минимального: {imin}')
a[imin], a[imax] = a[imax], a[imin]
print(a)
