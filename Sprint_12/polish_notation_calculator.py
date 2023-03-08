# ID 82952173
"""Калькулятор для вычисления выражений в обратной польской нотации.

Ввод осуществляется из файла `input.txt`.

Вывод результатов вычислений осуществляется в файл `output.txt`.
"""

from operator import add, floordiv, mul, sub
from typing import Callable, List, Optional

OPERATORS = {
    '+': lambda x, y: add(x, y),
    '-': lambda x, y: sub(y, x),
    '*': lambda x, y: mul(x, y),
    '/': lambda x, y: floordiv(y, x)
}


class StackClaculator:
    """Реализация структуры данных Стек."""

    def __init__(self) -> None:
        """Инициализирует пустой экземпляр класса."""
        self.__items: List[int] = []

    def __empty(pop: Callable) -> Callable:
        def wrapper(self, *args) -> str:
            if not self.__items:
                raise IndexError('error')
            return pop(self, *args)
        return wrapper

    def push(self, item: int) -> None:
        """Добавляет элемент в стек.

        Args:
            item: добавляемый элемент целочисленного типа.
        """
        self.__items.append(item)

    @__empty
    def pop(self) -> Optional[int]:
        """Вынимает элемент из стека.

        Returns:
            Возвращаемый элемент целочисленного типа.
        """
        return self.__items.pop()


def calculate(polish_notation: List[str]) -> int:
    """Калькулятор для вычисления выражений в обратной польской нотации.

    Для реализации использован стек.
    Реализованы операции:
        '+' - сложение,
        '-' - вычитание,
        '*' - умножение,
        '/' - целочисленное деление.

    Args:
        polish_notation: список операндов и операторов в строковом формате.

    Returns:
        Результат вычислений целочисленного типа.
    """
    stack = StackClaculator()

    for element in polish_notation:
        if element.lstrip('-').isdigit():
            stack.push(int(element))
        else:
            try:
                stack.push(OPERATORS[element](stack.pop(), stack.pop()))
            except IndexError as error:
                return error

    return stack.pop()


if __name__ == '__main__':
    with open('input.txt', 'r') as reader, open('output.txt', 'w') as writer:
        polish_notation = reader.read().strip().split()
        writer.write(str(calculate(polish_notation)))
