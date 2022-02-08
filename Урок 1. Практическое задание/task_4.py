"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

users = [
    {
        "name": "John",
        "password": "sha256",
        "activated": True
    },
    {
        "name": "Sergey",
        "password": "qwerty",
        "activated": False
    },
    {
        "name": "Marie",
        "password": "123",
        "activated": True
    },
]


def check_user_var1(user):
    """ Итоговая сложность: O(n) """
    for item in users:                                              # O(n)
        if item["name"] == user and item["activated"] is True:      # O(1)
            return "You can login."                                 # O(1)
    return "You shall activate you account."                        # O(1)


def check_user_var2(user):
    """ Итоговая сложность: O(n) """
    for item in users:                                              # O(n)
        if item["name"] == user:                                    # O(1)
            if item["activated"] is True:                           # O(1)
                return "You can login."                             # O(1)
    return "You shall activate you account."                        # O(1)


print(check_user_var1("John"))
print(check_user_var1("Sergey"))
print(check_user_var1("Marie"))

print(check_user_var2("John"))
print(check_user_var2("Sergey"))
print(check_user_var2("Marie"))
