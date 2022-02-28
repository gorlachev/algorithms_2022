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

Это файл для третьего скрипта
"""

# Урок 9 - Задание 3. Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

from pympler import asizeof


class Worker1:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

        position_income = {
            "ceo": {"wage": 1_000_000, "bonus": 500_000},
            "manager": {"wage": 250_000, "bonus": 50_000},
            "worker": {"wage": 100_000, "bonus": 15_000}
        }

        self._income = position_income.get(self.position)["wage"] + position_income.get(self.position)["bonus"]


class Position1(Worker1):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        name = self.name
        surname = self.surname
        print(f"{name} {surname}")

    def get_total_income(self):
        income = self._income
        print(income)


# оптимизация памяти через слоты

class Worker2:
    __slots__ = ("name", "surname", "position")

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

        position_income = {
            "ceo": {"wage": 1_000_000, "bonus": 500_000},
            "manager": {"wage": 250_000, "bonus": 50_000},
            "worker": {"wage": 100_000, "bonus": 15_000}
        }

        self._income = position_income.get(self.position)["wage"] + position_income.get(self.position)["bonus"]


class Position2(Worker2):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        name = self.name
        surname = self.surname
        print(f"{name} {surname}")

    def get_total_income(self):
        income = self._income
        print(income)


print(asizeof.asizeof(Position1("Ivan", "Ivanov", "worker")))  # 584
print(asizeof.asizeof(Position2("Ivan", "Ivanov", "worker")))  # 432
