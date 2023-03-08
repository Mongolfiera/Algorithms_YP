# ID 83626377
"""Реализация структуры данных Дек."""

from typing import Callable, Optional

COMMANDS = {
    'push_back': lambda dequeue, args: dequeue.push_back(args[0]),
    'push_front': lambda dequeue, args: dequeue.push_front(args[0]),
    'pop_back': lambda dequeue, args: dequeue.pop_back(),
    'pop_front': lambda dequeue, args: dequeue.pop_front(),
}


class Dequeue:
    """Дек - двусторонняя очередь.

    Дек реализован с использованием кольцевого буффера в двумя указателями.
    Добавление и извлечение элементов возможно с обоих концов.

    Attributes:
        capacity: Целочисленный размер Дека.
    """

    def __init__(self, capacity: int) -> None:
        """Инициализирует экземпляр класса.

        Args:
          capacity: Определяет размер экземпляра.
        """
        self.queue = [None] * capacity
        self.__capacity = capacity
        self.__head = 0
        self.__tail = capacity - 1
        self.__size = 0

    def __str__(self) -> str:
        """Возвращает заполненную часть Дека в виде строки."""
        result = self.queue[self.__tail+1:self.__tail+1+self.__size]
        if self.__size > self.__capacity - (self.__tail + 1):
            result.extend(self.queue[: self.__head])
        return str(result)

    def __empty(pop: Callable) -> Callable:
        def wrapper(self, *args) -> str:
            if not self.__size:
                raise IndexError('error')
            return pop(self, *args)
        return wrapper

    def __overflow(push: Callable) -> Callable:
        def wrapper(self, *args) -> None:
            if self.__size >= self.__capacity:
                raise IndexError('error')
            push(self, *args)
        return wrapper

    @__overflow
    def push_back(self, item: str) -> None:
        """Добавляет элемент в конец дека.

        Args:
            item: добавляемый элемент строкового типа.

        Raises:
            IndexError: в случае, если дек полон.
        """
        self.queue[self.__tail] = item
        self.__tail = (self.__tail - 1) % self.__capacity
        self.__size += 1

    @__overflow
    def push_front(self, item: str) -> None:
        """Добавляет элемент в начало дека.

        Args:
            item: добавляемый элемент строкового типа.

        Raises:
            IndexError: в случае, если дек полон.
        """
        self.queue[self.__head] = item
        self.__head = (self.__head + 1) % self.__capacity
        self.__size += 1

    @__empty
    def pop_back(self) -> Optional[str]:
        """Возвращает элемент из конца дека.

        Выводит последний элемент дека и удаляет его.

        Returns:
            Возвращаемый элемент.

        Raises:
            IndexError: в случае, если дек пуст.
        """
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__size -= 1
        return self.queue[self.__tail]

    @__empty
    def pop_front(self) -> Optional[str]:
        """Возвращает элемент из начала дека.

        Выводит первый элемент дека и удаляет его.

        Returns:
            Возвращаемый элемент.

        Raises:
            IndexError: в случае, если дек пуст.
        """
        self.__head = (self.__head - 1) % self.__capacity
        self.__size -= 1
        return self.queue[self.__head]


def main() -> None:
    """Реализация работы со структурой данных Дек.

    Ввод осуществляется из файла input.txt.
    Формат ввода:
        В первой строке записано количество команд.
        Во второй строке записан максимальный размер дека.
        В следующих строках записана одна из выполняемых команд.

    Вывод результатов выполнения команд осуществляется в файл output.txt.
    В случае, если команду выполнить невозможно, выводится сообщение 'error'.
    """
    with open('input.txt', 'r') as reader, open('output.txt', 'w') as writer:
        n, capacity, *commands = reader.read().splitlines()
        dequeue = Dequeue(int(capacity))

        commands = [command.split() for command in commands]
        for func, *args in commands:
            try:
                result = COMMANDS[func](dequeue, args)
                if result is not None:
                    writer.write(f'{result}\n')
            except IndexError as error:
                writer.write(f'{error}\n')


if __name__ == '__main__':
    main()
