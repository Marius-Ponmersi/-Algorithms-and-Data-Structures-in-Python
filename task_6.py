# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
a = [random.randint(-50, 50) for i in range(10)]
print(a)

max = -50
min = 50
for el in a:
    if el >= max:
        max = el
    if el <= min:
        min = el
print(f'min: {min}, max: {max}')

if a.index(min) < a.index(max):
    srez = a[a.index(min)+1:a.index(max)]
    print(srez)
    print(sum(srez))
else:
    srez = a[a.index(max) + 1:a.index(min)]
    print(srez)
    print(sum(srez))
