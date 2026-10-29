def factorial_iter(n: int) -> int:
    """Обчислює факторіал n! ітеративно.

    Параметри:
        n (int): ціле число, n >= 0.
    Повертає:
        int: значення n!.
    """
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_rec(n: int) -> int:
    """Обчислює факторіал n! рекурсивно.

    Параметри:
        n (int): ціле число, n >= 0.
    Повертає:
        int: значення n!.
    """
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


# Тести
assert factorial_iter(0) == 1 and factorial_rec(0) == 1
assert factorial_iter(1) == 1 and factorial_rec(1) == 1
assert factorial_iter(5) == 120 and factorial_rec(5) == 120
assert factorial_iter(10) == 3628800 and factorial_rec(10) == 3628800