# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

m = random.randint(1, 5)
n = 2 * m + 1
array = [random.randint(1, 50) for _ in range(n)]
print(array)

def sort_bubble(array: list):   # сортировка пузырьком
    k = 1
    while k < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        k += 1
    return array


print(sort_bubble(array))
print(f'{array[len(array) // 2]} - медиана')
