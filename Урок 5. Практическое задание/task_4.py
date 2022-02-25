"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

import timeit

from collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

test_code_1 = '''
def get_dic_elements():
    for key, value in d.items():
        print(key, value)
'''

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

test_code_2 = '''
def get_od_elements():
    for key, value in od.items():
        print(key, value)
'''

print(timeit.timeit(stmt=test_code_1, number=100))
print(timeit.timeit(stmt=test_code_2, number=100))

# 7.278999999998925e-06
# 7.073999999999275e-06 - получение элементов словаря OD быстрее, исользование OD целесoобразно
