# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

import cProfile
summa = 0

def sum_el(n: int): # n - число элеметов списка
    global summa
    n_first = n
    while True:
        el = (-0.5) ** (n - 1)
        summa = summa + el
        n -= 1
        if n == 0:
            return f'Сумма {n_first} элементов ряда равна: {summa}'


# "task_1a.sum_el(500)"
# 1000 loops, best of 5: 270 usec per loop

# "task_1a.sum_el(900)"
# 1000 loops, best of 5: 462 usec per loop

# "task_1a.sum_el(5_000)"
# 1000 loops, best of 5: 2.83 msec per loop


# cProfile.run("sum_el(500)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1      0.000    0.000    0.000    0.000    task_1a.py:6(sum_el)

# cProfile.run("sum_el(900)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1      0.001    0.001    0.001    0.001    task_1a.py:6(sum_el)

# cProfile.run("sum_el(5000)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.006    0.006    0.006    0.006    task_1a.py:6(sum_el)

