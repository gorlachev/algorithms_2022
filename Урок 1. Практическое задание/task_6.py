"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskManager:
    def __init__(self):
        self.main_board = []
        self.rework_board = []
        self.done_board = []

    def is_empty(self, board):
        return board == []

    def to_main(self, item):
        self.main_board.insert(0, item)

    def to_rework(self, item_num):
        self.rework_board.insert(0, self.main_board.pop(item_num))

    def to_done(self, board, item_num):
        if board == "main_board":
            self.done_board.insert(0, self.main_board.pop(item_num))
        elif board == "rework_board":
            self.done_board.insert(0, self.rework_board.pop(item_num))
        else:
            return "Incorrect board."

    def size(self, board):
        return len(board)


my_obj = TaskManager()
my_obj.to_main("to do1")
my_obj.to_main("to do2")
my_obj.to_main("to do3")
my_obj.to_main("to do4")
my_obj.to_main("to do5")
my_obj.to_main("to do6")
my_obj.to_main("to do7")

my_obj.to_rework(1)
my_obj.to_rework(2)

my_obj.to_done("main_board", 0)
my_obj.to_done("rework_board", 0)

print(my_obj.main_board)
print(my_obj.rework_board)
print(my_obj.done_board)

print(my_obj.size(my_obj.main_board))
print(my_obj.is_empty(my_obj.rework_board))