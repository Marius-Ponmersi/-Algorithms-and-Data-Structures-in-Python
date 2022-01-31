# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict
n = int(input('Введите количество предприятий: '))

def av_profit(n=n):

    titles = defaultdict(list)
    data = {input('Введите название предприятия: '): int(input('Введите прибыль предприятия: ')) for i in range(n)}
    profit_av = sum(data[k] for k, v in data.items())/n

    for k, v in data.items():

        if data[k] < profit_av:
            titles['less'].append(k)
        if data[k] > profit_av:
            titles['more'].append(k)

    return f'\n' \
           f'Средняя прибыль предприятий: {profit_av } \n' \
           f'{titles}' \

print(av_profit())
