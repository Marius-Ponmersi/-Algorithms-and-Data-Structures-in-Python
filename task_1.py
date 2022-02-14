# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.

import hashlib


def count_subs(line: str):
    assert len(line) > 0, 'Пустая строка'

    subs = {}
    summa = 0

    def get_hash(subs_: str):
        return hashlib.sha1(subs_.encode('utf-8')).hexdigest()

    for i in range(len(line) + 1):
        for j in range(len(line) + 1):
            if 0 < len(line[i:j]) < len(line):
                subs[line[i:j]] = get_hash(line[i:j])
                summa += 1

    return f'Количество подстрок: {summa}\n'\
           f'Количество уникальных подстрок: {len(subs)}'


s = 'aaa'
print(s, count_subs(s), sep='\n')
