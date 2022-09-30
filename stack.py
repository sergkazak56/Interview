# Класс Stack
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """
        Проверяет пустой ли стек
        :return: True - если пустой, False - если не пустой
        """
        if self.stack:
            return False
        return True

    def push(self, item):
        """
        Добавляет элемент в конец стека
        :param item: добавляемый элемент
        """
        self.stack.append(item)

    def pop(self):
        """
        Удаляет конечный элемент стека
        :return: removed - удаленный элемент стека
        """
        if self.isEmpty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        """
        Возвращает конечный элемент стека
        :return: self.stack[-1] - конечный элемент стека
        """
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        """
        Возвращает размер стека
        :return: len(self.stack) - размер стека
        """
        return len(self.stack)

    def __str__(self):
        """
        Перезагрузка метода __str__ для стека
        :return: str_ - стек в виде набора элементов
        """
        return str(self.stack).strip('[]')