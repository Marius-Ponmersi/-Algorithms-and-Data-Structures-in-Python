# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#  «Решето Эратосфена».

def prime_number(i: int, n: int):    # i - номер простого числа, n - до какого числа получать простые числа
    n = n
    sieve = [num for num in range(n)]
    sieve[1] = 0
    for s in range(2, n):
        if sieve[s] != 0:
            j = s * 2
            while j < n:
                sieve[j] = 0
                j = j + s
    prime = [el for el in sieve if el != 0]
    try:
        return prime[i-1]
    except IndexError:
        return f'Нет столько простых чисел в диапазоне от 2 до {n}'


# "task_2a.prime_number(10, 100)"
# 1000 loops, best of 5: 31.9 usec per loop

# "task_2a.prime_number(10, 200)"
# 1000 loops, best of 5: 67 usec per loop

#  "task_2a.prime_number(10, 500)"
# 1000 loops, best of 5: 190 usec per loop

