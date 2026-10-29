def digit_sum_iter(n: int) -> int:
    """Обчислює суму цифр натурального числа ітеративно.

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        int: сума цифр числа.
    """
    if n == 0:
        return 0
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s


def digit_sum_rec(n: int) -> int:
    """Обчислює суму цифр натурального числа рекурсивно.

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        int: сума цифр числа.
    """
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + digit_sum_rec(n // 10)


# Тести
assert digit_sum_iter(0) == 0 and digit_sum_rec(0) == 0
assert digit_sum_iter(7) == 7 and digit_sum_rec(7) == 7
assert digit_sum_iter(12345) == 15 and digit_sum_rec(12345) == 15