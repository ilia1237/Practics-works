def digit_count_iter(n: int) -> int:
    """Обчислює кількість цифр натурального числа ітеративно.

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        int: кількість цифр.
    """
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count


def digit_count_rec(n: int) -> int:
    """Обчислює кількість цифр натурального числа рекурсивно.

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        int: кількість цифр.
    """
    n = abs(n)
    if n < 10:
        return 1
    return 1 + digit_count_rec(n // 10)


# Тести
assert digit_count_iter(0) == 1 and digit_count_rec(0) == 1
assert digit_count_iter(7) == 1 and digit_count_rec(7) == 1
assert digit_count_iter(70500) == 5 and digit_count_rec(70500) == 5