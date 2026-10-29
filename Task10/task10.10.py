def binary_iter(n: int) -> str:
    """Повертає двійкове подання натурального числа як рядок ітеративно (без bin()).

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        str: двійковий рядок.
    """
    if n == 0:
        return "0"
    res = []
    while n > 0:
        res.append(str(n % 2))
        n //= 2
    return "".join(reversed(res))


def binary_rec(n: int) -> str:
    """Повертає двійкове подання натурального числа як рядок рекурсивно.

    Параметри:
        n (int): натуральне число, n >= 0.
    Повертає:
        str: двійковий рядок.
    """
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_rec(n // 2) + str(n % 2)


# Тести
assert binary_iter(0) == "0" and binary_rec(0) == "0"
assert binary_iter(1) == "1" and binary_rec(1) == "1"
assert binary_iter(10) == "1010" and binary_rec(10) == "1010"
assert binary_iter(255) == "11111111" and binary_rec(255) == "11111111"