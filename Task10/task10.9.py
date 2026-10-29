def list_sum_iter(a: list) -> int:
    """Обчислює суму елементів списку ітеративно (без sum()).

    Параметри:
        a (list): список чисел.
    Повертає:
        int/float: сума елементів.
    """
    s = 0
    for x in a:
        s += x
    return s


def list_sum_rec(a: list) -> int:
    """Обчислює суму елементів списку рекурсивно через перший елемент і решту.

    Параметри:
        a (list): список чисел.
    Повертає:
        int/float: сума елементів.
    """
    if not a:
        return 0
    return a[0] + list_sum_rec(a[1:])


# Тести
assert list_sum_iter([]) == 0 and list_sum_rec([]) == 0
assert list_sum_iter([5]) == 5 and list_sum_rec([5]) == 5
assert list_sum_iter([1, 2, 3, 4]) == 10 and list_sum_rec([1, 2, 3, 4]) == 10