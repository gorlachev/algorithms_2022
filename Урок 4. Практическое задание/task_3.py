"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit

test_code1 = '''
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
'''

test_code2 = '''
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
'''

test_code3 = '''
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
'''

test_code4 = '''
def revers_4(enter_num):
    li_num = list(str(n))
    li_num.reverse()
    return "".join(li_num)
'''

print(timeit.timeit(stmt=test_code1))  # 0.163839038
print(timeit.timeit(stmt=test_code2))  # 0.107850903
print(timeit.timeit(stmt=test_code3))  # 0.10575788199999997 - наиболее эффективная реализация,
# так как использует встроенный в Python метод обратного среза списка, позволяющий сразу выводить список
# в обратном порядкее
print(timeit.timeit(stmt=test_code4))  # 0.10685223299999996

