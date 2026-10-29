def gcd_iter(a: int, b: int) -> int:
    """Знаходить НСД двох чисел за алгоритмом Евкліда ітеративно.

    Параметри:
        a (int): перше ціле число.
        b (int): друге ціле число.
    Повертає:
        int: найбільший спільний дільник.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def gcd_rec(a: int, b: int) -> int:
    """Знаходить НСД двох чисел за алгоритмом Евкліда рекурсивно.

    Параметри:
        a (int): перше ціле число.
        b (int): друге ціле число.
    Повертає:
        int: найбільший спільний дільник.
    """
    if b == 0:
        return abs(a)
    return gcd_rec(b, a % b)


# Тести
assert gcd_iter(48, 18) == 6 and gcd_rec(48, 18) == 6
assert gcd_iter(17, 5) == 1 and gcd_rec(17, 5) == 1
assert gcd_iter(12, 0) == 12 and gcd_rec(12, 0) == 12