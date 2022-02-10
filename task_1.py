# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n_ = int(input('Введите количество друзей: '))


def graf(n: int):
    '''Ориентированный граф'''

    g = [[1] * len(range(n)) for _ in range(n)]
    summa = []

    for i in range(n):
        for j in range(n):
            if i >= j:
                g[i][j] = 0

    for el in g:
        summa.append(sum(el))
        print(el)

    return f'Число рукопожатий: {sum(summa)}'


print(graf(n_))
