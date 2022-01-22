# 4. Определить, какое число в массиве встречается чаще всего.

import random
a = [random.randint(1, 5) for i in range(12)]
print(a)
b = {el: a.count(el) for el in a }
print(b)
print(f'Самое частое число: {max(a, key=a.count)}')
