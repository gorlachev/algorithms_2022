"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
import timeit

li = [x for x in range(1, 101)]
queue = deque([x for x in range(1, 101)])

test_code_1_1 = '''
def append_li():
    [li.append(x) for x in range(1, 101)]
'''

test_code_1_2 = '''
def append_queue():
    [queue.append(x) for x in range(1, 101)]
'''

print(timeit.timeit(stmt=test_code_1_1, number=100))  # 7.268000000001246e-06
print(timeit.timeit(stmt=test_code_1_2, number=100))  # 6.980999999999654e-06 - append в деке работает немного быстрее


test_code_1_3 = '''
def pop_li():
    for x in range(len(li)):
        print(li.pop())
'''

test_code_1_4 = '''
def pop_queue():
    for x in range(len(queue)):
        print(queue.pop())
'''

print(timeit.timeit(stmt=test_code_1_3, number=100))  # 7.250999999999785e-06 pop в списках на замерах работает незначительно быстрее
print(timeit.timeit(stmt=test_code_1_4, number=100))  # 7.263000000000408e-06

test_code_1_5 = '''
def extend_li():
    for x in range(len(li)):
        li.extend([x])
'''

test_code_1_6 = '''
def extend_queue():
    for x in range(len(queue)):
        queue.extend([x])
'''

print(timeit.timeit(stmt=test_code_1_5, number=100))  # 7.446999999997234e-06 extend в списках на замерах работает незначительно быстрее
print(timeit.timeit(stmt=test_code_1_6, number=100))  # 7.515999999999079e-06


test_code_1_7 = '''
def insert_li():
    for x in range(len(li)):
        li.insert(x)
'''

test_code_1_8 = '''
def appendleft_queue():
    for x in range(len(queue)):
        queue.appendleft(x)
'''

print(timeit.timeit(stmt=test_code_1_7, number=100))  # 6.814999999996824e-06
print(timeit.timeit(stmt=test_code_1_8, number=100))  # 6.5349999999984865e-06 appendleft в деке на замерах работает незначительно быстрее


test_code_1_9 = '''
def popleft_queue():
    for _ in range(len(queue)):
        queue.pop(0)
'''

test_code_1_10 = '''
def popleft_queue():
    for x in range(len(queue)):
        queue.popleft(x)
'''

print(timeit.timeit(stmt=test_code_1_9, number=100))   # 7.436999999999028e-06 pop(0) в списке работает быстрее
print(timeit.timeit(stmt=test_code_1_10, number=100))  # 7.369999999999599e-06

test_code_1_11 = '''
def insert_li():
    for x in range(len(li)):
        li.insert(x)
'''

test_code_1_12 = '''
def extendleft_queue():
    for x in range(len(queue)):
        queue.extendleft([x])
'''

print(timeit.timeit(stmt=test_code_1_11, number=100))   # 7.352000000002135e-06 insert в списке работает быстрее
print(timeit.timeit(stmt=test_code_1_12, number=100))   # 7.500000000000562e-06

test_code_1_14 = '''
def get_li():
    for x in range(len(queue)):
        print(li[x])
'''

test_code_1_15 = '''
def get_queue():
    for x in range(len(queue)):
        print(queue[x])
'''

print(timeit.timeit(stmt=test_code_1_14, number=100))  # 7.19599999999751e-06
print(timeit.timeit(stmt=test_code_1_15, number=100))  # 7.1050000000003055e-06 получение элемента в деке незначительно быстрее