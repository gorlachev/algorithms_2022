"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

# Программа, которая считает самый высокий балл студентов из введенных в форме strings данных

from memory_profiler import memory_usage

math_scores = "".join(map(str, range(10000+1)))


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def count_score_1(student_scores):
    student_scores = student_scores.split(",")
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    highest_score = 0
    for score in student_scores:
        if highest_score < score:
            highest_score = score
    return highest_score


@decor
def count_score_2(student_scores):
    student_scores = map(int, set(student_scores.split(",")))  # профилирование памяти за счет использования кортежа
    return max(student_scores)


res, mem_diff = count_score_1(math_scores)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.01953125 Mib

res, mem_diff = count_score_2(math_scores)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.015625 Mib
