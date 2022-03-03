"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

import statistics
import random
import timeit

numbers10 = [random.randint(0, 100) for i in range(2 * 10 + 1)]
numbers100 = [random.randint(0, 100) for _ in range(2 * 100 + 1)]
numbers1000 = [random.randint(0, 100) for _ in range(2 * 1000 + 1)]


def median(nums):
    return statistics.median(nums[:])


mdn10 = timeit.timeit("median(numbers10[:])", setup="from __main__ import median, numbers10", number=100)
mdn100 = timeit.timeit("median(numbers100[:])", setup="from __main__ import median, numbers100", number=100)
mdn1000 = timeit.timeit("median(numbers1000[:])", setup="from __main__ import median, numbers1000", number=100)

print(mdn10)    # 0.00014010700000000043
print(mdn100)   # 0.001147184999999995
print(mdn1000)  # 0.021677845000000008

# встроенная функция поиска медианы самая эффективная

