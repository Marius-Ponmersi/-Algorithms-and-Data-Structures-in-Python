# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

n = int(input('Введите количество чисел, которые нужно будет ввести: '))

sum_dig_max = 0
right_number = 0
for i in range(n):
    number = input('Введите натуральное число: ')
    sum_dig_number = 0
    for digit in number:
        sum_dig_number += int(digit)
    print(f'Сумма цифр: {sum_dig_number}')
    if sum_dig_number >= sum_dig_max:
        sum_dig_max = sum_dig_number
        right_number = number

sum_dig_right_number = 0
for digit in right_number:
    sum_dig_right_number += int(digit)
print(f'Наибольшее по сумме цифр число {right_number}, сумма его цифр {sum_dig_right_number}')
