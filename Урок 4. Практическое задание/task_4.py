"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

import timeit

array = [1, 3, 1, 3, 4, 5, 1]

test_code1 = '''
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
'''

test_code2 = '''
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
'''

test_code3 = '''
def func_3():
    return f'Чаще всего встречается число {max(set(array), key=array.count)}, ' \
           f'оно появилось в массиве {array.count(max(set(array), key=array.count))} раз(а)'
'''

print(timeit.timeit(stmt=test_code1))  # 0.06499102500000001
print(timeit.timeit(stmt=test_code2))  # 0.060570578
print(timeit.timeit(stmt=test_code3))  # 0.05373261899999998 - получилось ускорить задачу
