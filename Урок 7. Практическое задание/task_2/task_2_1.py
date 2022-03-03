"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import random
import timeit

numbers10 = [random.randint(0, 100) for i in range(2 * 10 + 1)]
numbers100 = [random.randint(0, 100) for _ in range(2 * 100 + 1)]
numbers1000 = [random.randint(0, 100) for _ in range(2 * 1000 + 1)]


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


qsort10 = timeit.timeit("quick_sort(numbers10[:])", setup="from __main__ import quick_sort, numbers10", number=100)
qsort100 = timeit.timeit("quick_sort(numbers100[:])", setup="from __main__ import quick_sort, numbers100", number=100)
qsort1000 = timeit.timeit("quick_sort(numbers1000[:])", setup="from __main__ import quick_sort, numbers1000", number=100)

print(qsort10)    # 0.002295358999999997
print(qsort100)   # 0.02263512699999999
print(qsort1000)  # 0.145302518


