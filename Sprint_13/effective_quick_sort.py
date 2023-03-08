# ID 83608955
"""Реализация алгоритма быстрой сортировки in-place.

(без использования дополнительной памяти)
"""


class Contestant:
    """Участник соревнований по спортивному программированию.

    Attributes:
        name (str): уникальный логин участника соревнования.
    """

    def __init__(self, name: str, score: str, penalty: str) -> None:
        """Инициализация участника.

        Args:
            name (str): уникальный логин участника соревнования.
            score (str): количество решённых задач.
            penalty (str): Количество штрафных баллов.
        """
        self.name = name
        self.__score = int(score)
        self.__penalty = int(penalty)

    def __str__(self):
        """Возвращает имя участника соревнований."""
        return self.name

    def __le__(self, other):
        """Сравнение - меньше - участника с другим участником.

        Меньший ранг (более высокое положение в турнирной таблице)
        имеет участник - в порядке понижения приоритета:
        - с бОльшим числом решенных задач,
        - меньшим штрафом и тот, у которого
        - логин идёт раньше в алфавитном (лексикографическом) порядке.

        Returns:
            True, если участник имеет меньший ранг, чем другой участник.
        """
        return (-self.__score, self.__penalty, self.name) <= (
            -other.__score, other.__penalty, other.name
        )


def partition(left: int, right: int) -> int:
    """Сортировка массива относительно опорного элемента.

    Часть массива от `left` до `right` указателей (включительно)
    сортируется относительно опорного элемента - меньшие элементы
    переносятся в левую часть, большие - в правую.
    В качесте опорного элемента выбирается крайний правый элемент.

    Args:
        left: левая граница сортируемой части массива -
          целочисленного типа.
        right: правая граница сортируемой части массива -
          целочисленного типа.

    Returns:
        индекс, разделяющий массив на элементы меньше опорного и больше
          опорного - целочисленного типа.
    """
    pivot = contestants[right]
    partition_index = left
    for j in range(left, right):
        if contestants[j] <= pivot:
            (contestants[partition_index], contestants[j]) = (
                contestants[j], contestants[partition_index]
            )
            partition_index += 1
    (contestants[partition_index], contestants[right]) = (
        contestants[right], contestants[partition_index]
    )
    return partition_index


def sort_winners(left: int = 0, right: int = 0) -> None:
    """Быстрая соритровка in-place.

    Массив делится на два подмассива:
      элементы меньше опорного, и больше опорного.
      К обеим частям применяется рекурсивная сортировка.
      Базовый случай - сортировка массива из одного элемента.

    Args:
        left: левая граница сортируемой части массива -
          целочисленного типа.
        right: правая граница сортируемой части массива -
          целочисленного типа.
    """
    if left < right:
        pivot = partition(left, right)
        sort_winners(left, pivot - 1)
        sort_winners(pivot + 1, right)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader, open('output.txt', 'w') as writer:
        n, *contestants_data = reader.readlines()
        number = int(n)
        #  В исходном файле есть лишняя информация, поэтому приходится использовать number
        contestants = [
            Contestant(*contestants_data[i].split()) for i in range(number)]
        sort_winners(right=number - 1)
        writer.write(
            "\n".join([str(contestant) for contestant in contestants])
        )
