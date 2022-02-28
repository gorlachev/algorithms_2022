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

Это файл для четвертого скрипта
"""


# Урок 9 - Задание 4. Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from pympler import asizeof


class Car1:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = "прямо"

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина едет {self.direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")


class TownCar1(Car1):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")
        if self.speed > 60:
            print("Вы превышаете допустимую скорость")


class SportCar1(Car1):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar1(Car1):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")
        if self.speed > 40:
            print("Вы превышаете допустимую скорость")


class PoliceCar1(Car1):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

# оптимизация памяти через слоты

class Car2:
    __slots__ = ("speed", "color", "name", "is_police")

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = "прямо"

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина едет {self.direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")


class TownCar2(Car2):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")
        if self.speed > 60:
            print("Вы превышаете допустимую скорость")


class SportCar2(Car2):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar2(Car2):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")
        if self.speed > 40:
            print("Вы превышаете допустимую скорость")


class PoliceCar2(Car2):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


print(asizeof.asizeof(PoliceCar1(60, "yellow", "Lexus")))  # 712
print(asizeof.asizeof(PoliceCar2(60, "yellow", "Lexus")))  # 512


