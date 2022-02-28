"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile

@profile
def wrapper(number):  # профилирование памяти через обертывание рекурсивной функции
    def count_down(input_number):
        """ Count down from a number  """
        print(input_number)
        next = input_number - 1
        if next > 0:
            count_down(next)

    return count_down(number)


wrapper(5)