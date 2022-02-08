"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class PileOfPlates:
    def __init__(self):
        self.piles = [[]]

    def push_in(self, el):
        for i in self.piles:
            if len(i) > 2:
                self.piles.append([])

            if len(i) <= 2:
                i.append(el)
                break


a = PileOfPlates()
a.push_in("plate1")
a.push_in("plate2")
a.push_in("plate3")
a.push_in("plate4")
a.push_in("plate5")
a.push_in("plate6")
a.push_in("plate7")
a.push_in("plate8")
a.push_in("plate9")
a.push_in("plate10")

print(a.piles)
