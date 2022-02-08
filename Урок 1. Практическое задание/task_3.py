"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies = {
    "ShellCo1": 100000,
    "ShellCo2": 300000,
    "ShellCo3": 200000
}


def find_co_var1(company_dict):
    return max(company_dict, key=company_dict.get)
    # O(n)


def find_co_var2(company_dict):
    return [key for (key, value) in company_dict.items() if value == max(company_dict.values())]
    # O(1) + O(n) + O(1) + O(n)


def find_co_var3(company_dict):
    min_val = 0                                 # O(1)
    winner = None                               # O(1)
    for (key, value) in company_dict.items():   # O(n)
        if value > min_val:                     # O(1)
            min_val = value                     # O(1)
            winner = key                        # O(1)
    return winner                               # O(1)


print(find_co_var1(companies))
print(find_co_var2(companies))
print(find_co_var3(companies))

