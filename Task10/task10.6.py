from functools import lru_cache


def fib_iter(n: int) -> int:
    """Обчислює n-те число Фібоначчі ітеративно.

    Параметри:
        n (int): індекс числа Фібоначчі, n >= 0.
    Повертає:
        int: n-те число Фібоначчі.
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@lru_cache(maxsize=None)
def fib_rec(n: int) -> int:
    """Обчислює n-те число Фібоначчі рекурсивно з мемоізацією.

    Параметри:
        n (int): індекс числа Фібоначчі, n >= 0.
    Повертає:
        int: n-те число Фібоначчі.
    """
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# Тести
assert fib_iter(0) == 0 and fib_rec(0) == 0
assert fib_iter(1) == 1 and fib_rec(1) == 1
assert fib_iter(10) == 55 and fib_rec(10) == 55
assert fib_iter(30) == 832040 and fib_rec(30) == 832040