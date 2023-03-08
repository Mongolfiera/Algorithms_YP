# ID 83625271
"""Поиск в сломанном массиве."""

from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Бинарный поиск значения в остортированном массиве со сдвигом.

    Args:
        nums: массив в котором производится поиск -
          список целочисленных значений.
        target: искомое значение - целочисленного типа.

    Returns:
        индекс искомого элемента - целочисленного типа или -1,
          если элемент не найден.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right - left) // 2 + left
        center = nums[middle]

        if target == center:
            return middle

        leftmost = nums[left]

        if (leftmost <= center and leftmost <= target < center) or (
            leftmost > center and (leftmost <= target or target < center)
        ):
            right = middle - 1
        else:
            left = middle + 1
    return -1


def test():
    """Тест корректности работы алгоритма."""
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
