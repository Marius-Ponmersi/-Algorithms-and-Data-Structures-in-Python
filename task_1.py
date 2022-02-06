# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

array_ = [random.randint(-100, 99) for _ in range(15)]
print(array_)
array_copy = array_.copy()


def sort_bubble(array: list):   # сортировка пузырьком
    n = 1
    outer_loop_iteration_count = 0  # счетчик количества итераций
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        outer_loop_iteration_count += 1
    return f'Cортировка пузырьком: {array}, количество итераций {outer_loop_iteration_count}'


print(sort_bubble(array_))


def sort_bubble_mod(array: list):   # улучшенная сортировка пузырьком
    n = 1
    has_swapped = False  # следит за тем был ли хотя бы один обмен на текущей итерации
    outer_loop_iteration_count = 0  # счетчик количества итераций
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                has_swapped = True
                array[i], array[i + 1] = array[i + 1], array[i]
        if not has_swapped:
            return f'Улучшенная сортировка пузырьком: {array}, количество итераций {outer_loop_iteration_count}'
        else:
            has_swapped = False
        outer_loop_iteration_count += 1
        n += 1
    return f'Улучшенная сортировка пузырьком: {array}, количество итераций {outer_loop_iteration_count}'


print(sort_bubble_mod(array_copy))

# Возьмем почти отсортированный массив: a = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]
a = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]
b = a.copy()
print(sort_bubble(a))
print(sort_bubble_mod(b))
