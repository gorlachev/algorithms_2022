"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce
"""

from collections import defaultdict

hex_signs = '0123456789ABCDEF'
table = defaultdict(int)
count = 0
for i in hex_signs:
    table[i] += count
    count += 1


def get_num(string):
    dex = 0
    num = list(string)
    num.reverse()
    for n in range(len(num)):
        dex += table[num[n]] * 16 ** n
    return dex


def get_hex(numb):
    num = []
    while numb > 0:
        d = numb % 16
        [num.append(i) for i in table if table[i] == d]
        numb //= 16
    num.reverse()
    return list(num)


num_1 = get_num(input('Первое число : ').upper())
num_2 = get_num(input('Второе число: ').upper())

print(f'Сумма: {get_hex(num_1 + num_2)}')
print(f'Произведение: {get_hex(num_1 * num_2)}')

"""
2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""