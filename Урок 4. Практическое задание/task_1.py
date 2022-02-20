"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

import timeit
test_code1 = ''' 
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
'''

print(timeit.timeit(stmt=test_code1))

test_code2 = '''
def func_2(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr
'''
print(timeit.timeit(stmt=test_code2))

# 0.061242340000000006
# 0.055089812000000016 - второй пример по наполнению пустого словаря через list comprehensions работает быстрее
