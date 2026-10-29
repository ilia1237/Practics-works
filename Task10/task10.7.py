def reverse_number_iter(n: int) -> int:
    """Повертає число, записане цифрами у зворотному порядку, ітеративно.

    Параметри:
        n (int): ціле невід'ємне число.
    Повертає:
        int: перевернуте число.
    """
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev * sign


def reverse_number_rec(n: int) -> int:
    """Повертає число, записане цифрами у зворотному порядку, рекурсивно.

    Параметри:
        n (int): ціле невід'ємне число.
    Повертає:
        int: перевернуте число.
    """

    def helper(val, rev):
        if val == 0:
            return rev
        return helper(val // 10, rev * 10 + val % 10)

    sign = -1 if n < 0 else 1
    return helper(abs(n), 0) * sign


# Тести
assert reverse_number_iter(12345) == 54321 and reverse_number_rec(12345) == 54321
assert reverse_number_iter(7) == 7 and reverse_number_rec(7) == 7
assert reverse_number_iter(1200) == 21 and reverse_number_rec(1200) == 21