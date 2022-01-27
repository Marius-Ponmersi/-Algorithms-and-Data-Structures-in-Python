# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

import cProfile
summa = 1
el = 1

def sum_el(n: int): # n - число элеметов списка
    global summa, el
    for i in range(1, n):
        el /= -2
        summa += el
    return f'Сумма элементов ряда: {summa}'


# "task_1b.sum_el(500)"
# 1000 loops, best of 5: 92.9 usec per loop

#  "task_1b.sum_el(900)"
# 1000 loops, best of 5: 180 usec per loop

# "task_1b.sum_el(5_000)"
# 1000 loops, best of 5: 949 usec per loop


# cProfile.run("sum_el(500)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1      0.000   0.000    0.000    0.000     task_1b.py:7(sum_el)

# cProfile.run("sum_el(900)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1      0.000   0.000    0.000    0.000     task_1b.py:7(sum_el)

# cProfile.run("sum_el(5000)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1     0.003    0.003    0.003    0.003     task_1b.py:7(sum_el)