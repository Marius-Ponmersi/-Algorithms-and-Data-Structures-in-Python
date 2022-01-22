# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

count_num = {}

for num in range(2, 10):
    count_num[num] = []
    for n in range(2, 100):
        if n % num == 0:
            count_num[num].append(n)
    count_num[num] = {len(count_num[num]): count_num[num]}

for key in count_num:
    print(key, count_num[key])
