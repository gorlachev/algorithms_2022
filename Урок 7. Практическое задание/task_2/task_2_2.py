"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
import timeit

numbers10 = [random.randint(0, 100) for i in range(2 * 10 + 1)]
numbers100 = [random.randint(0, 100) for _ in range(2 * 100 + 1)]
numbers1000 = [random.randint(0, 100) for _ in range(2 * 1000 + 1)]


def insertion(nums):
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


insrt10 = timeit.timeit("insertion(numbers10[:])", setup="from __main__ import insertion, numbers10", number=100)
insrt100 = timeit.timeit("insertion(numbers100[:])", setup="from __main__ import insertion, numbers100", number=100)
insrt1000 = timeit.timeit("insertion(numbers1000[:])", setup="from __main__ import insertion, numbers1000", number=100)

print(insrt10)    # 0.0016541140000000051
print(insrt100)   # 0.147888989
print(insrt1000)  # 13.524095202

