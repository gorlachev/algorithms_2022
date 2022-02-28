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

Это файл для второго скрипта
"""


# Урок 9 - Задание 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

from memory_profiler import profile

from pympler import asizeof


class Road1:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_mass(self):
        result = self.length * self.width * 25 * 5 / 1000
        print(f"{result} т.")


old_road = Road1(20, 5000)

# оптимизация памяти через слоты


class Road2:
    __slots__ = ["width", "length"]

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_mass(self):
        result = self.length * self.width * 25 * 5 / 1000
        print(f"{result} т.")


print(asizeof.asizeof(Road1(20, 5000)))  #328
print(asizeof.asizeof(Road2(20, 5000)))  #112

