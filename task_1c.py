# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

import cProfile
import functools

@ functools.lru_cache()
def sum_el(n: int):  # n - число элеметов списка
    def el(n):
        if n == 1:
            return n
        return (el(n - 1)) * (-0.5)
    return sum(el(i) for i in range(1, n+1))

# без декоратора

# "task_1c.sum_el(500)"
# 1000 loops, best of 5: 29.4 msec per loop

#  "task_1c.sum_el(900)"
# 1000 loops, best of 5: 103 msec per loop

#cProfile.run("sum_el(500)")
#  ncalls      tottime  percall  cumtime  percall filename:lineno(function)
# 125250/500    0.424    0.000    0.424    0.001      task_1c.py:6(el)

#cProfile.run("sum_el(900)")
#  ncalls      tottime  percall  cumtime  percall filename:lineno(function)
# 405450/900    1.409    0.000    1.409    0.002    task_1c.py:6(el)


# c декоратором

#  "task_1c.sum_el(500)"
# 1000 loops, best of 5: 326 nsec per loop

# "task_1c.sum_el(900)"
# 1000 loops, best of 5: 309 nsec per loop

#cProfile.run("sum_el(500)")
#  ncalls      tottime  percall  cumtime  percall filename:lineno(function)
# 125250/500    0.399    0.000    0.399    0.001      task_1c.py:8(el)

#cProfile.run("sum_el(900)")
#  ncalls      tottime  percall  cumtime  percall filename:lineno(function)
# 405450/900    1.578    0.000    1.578    0.002       task_1c.py:8(el)

