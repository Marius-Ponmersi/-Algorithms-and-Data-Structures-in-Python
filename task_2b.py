# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Второй способ — без использования «Решета Эратосфена».


def prime_number(i: int, n: int):    # i - номер простого числа, n - до какого числа получать простые числа
    n = n
    numbers = {num for num in range(2, n)}
    not_prime = set()    # не простые числа
    for num in numbers:
        spam = [s for s in range(2, num)]
        for el in spam:
            if num % el == 0:
                not_prime.add(num)
    prime = sorted(list(numbers - not_prime))
    try:
        return prime[i - 1]
    except IndexError:
        return f'Нет столько простых чисел в диапазоне от 2 до {n}'


#  "task_2b.prime_number(10, 100)"
# 1000 loops, best of 5: 570 usec per loop

#  "task_2b.prime_number(10, 200)"
# 1000 loops, best of 5: 2.12 msec per loop

#  "task_2b.prime_number(10, 500)"
# 1000 loops, best of 5: 13.5 msec per loop
