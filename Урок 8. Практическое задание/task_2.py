"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # def check_if_is_tree(self, obj):
    #     if obj is None or (obj.left_child is None and obj.right_child is None):
    #         return True
    #
    #     elif obj.right_child is None:
    #         print(obj.left_child.root)
    #         return obj.left_child.root < obj.root and self.check_if_is_tree(obj.left_child)
    #
    #     elif obj.left_child is None:
    #         print(obj.right_child.root)
    #         return obj.right_child.root >= obj.root and self.check_if_is_tree(obj.right_child)
    #
    #     return self.check_if_is_tree(obj.left_child) and self.check_if_is_tree(obj.right_child)

    def validate_tree(self, tree):
        return self.helper(tree, float('-inf'), float('inf'))

    def helper(self, tree, min_val, max_val):
        if tree is None:
            return True
        if tree.root < min_val or tree.root >= max_val:
            return False
        left_is_valid = self.helper(tree.left_child, min_val, tree.root)
        return left_is_valid and self.helper(tree.right_child, tree.root, max_val)


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.validate_tree(r))  # False

z = BinaryTree(10)
print(z.validate_tree(z))  # True

z.insert_left(12)
print(z.validate_tree(z))  # False

z.insert_right(3)
print(z.validate_tree(z))  # False
