def power_iter(a: int, n: int) -> int:
    """Обчислює a^n без оператора ** ітеративно.

    Параметри:
        a (int): основа степеня.
        n (int): показник степеня, n >= 0.
    Повертає:
        int: результат a^n.
    """
    res = 1
    base = a
    power_val = n
    while power_val > 0:
        if power_val % 2 == 1:
            res *= base
        base *= base
        power_val //= 2
    return res


def power_rec(a: int, n: int) -> int:
    """Обчислює a^n рекурсивно за O(log n).

    Параметри:
        a (int): основа степеня.
        n (int): показник степеня, n >= 0.
    Повертає:
        int: результат a^n.
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power_rec(a, n // 2)
        return half * half
    else:
        return a * power_rec(a, n - 1)


# Тести
assert power_iter(2, 10) == 1024 and power_rec(2, 10) == 1024
assert power_iter(5, 0) == 1 and power_rec(5, 0) == 1
assert power_iter(3, 4) == 81 and power_rec(3, 4) == 81