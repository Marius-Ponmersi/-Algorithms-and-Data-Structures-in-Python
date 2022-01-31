# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

# num1 = [el for el in input('Введите первое шестнадцатиричное число: ').upper()]
# num2 = [el for el in input('Введите второе шестнадцатиричное число: ').upper()]

data1610 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

data1016 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', '-': '-'}


def num16_to_10(number16: list):   # преобразует шестнадцетиричные числа в десятичные

    for el in range(len(number16)):
        number16[el] = data1610[number16[el]]

    i = 0
    j = len(number16)
    while i < len(number16):
        number16[i] = number16[i]*16**(j-1)
        i = i + 1
        j = j - 1
    return sum(number16)

# print(num16_to_10(num1))


num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
summa = num1 + num2
multiply = num1 * num2


def num10_to16(number: int):   # преобразует десятичное чило шестнадцетиричное и выводит список
    number16 = []
    if abs(number) < 10:
        number16 = [el for el in str(number)]
    elif 10 <= abs(number) < 16:
        number16 = [data1016[abs(number)]]
        if number < 0:
            number16.insert(0, '-')
    else:
        spam = number
        while abs(number) // 16 > 0:
            number16.append(abs(number) % 16)
            number = number // 16
            if abs(number) < 16:
                number16.append(abs(number))
                break
        number16 = number16[::-1]
        if spam <= -16:
            number16.insert(0, '-')
        number16 = [data1016[el] for el in number16]
    return number16


print(f'{num10_to16(num1)} - первое число\n'
      f'{num10_to16(num2)} - второе число\n'
      f'{num10_to16(num1 + num2)} - сумма чисел\n'
      f'{num10_to16(num1 * num2)} - произведение чисел')
