def is_palindrome_iter(s: str) -> bool:
    """Перевіряє, чи є рядок паліндромом ітеративно (ігноруючи регістр та неалфавітні символи).

    Параметри:
        s (str): вхідний рядок.
    Повертає:
        bool: True, якщо паліндром, інакше False.
    """
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_rec(s: str) -> bool:
    """Перевіряє, чи є рядок паліндромом рекурсивно.

    Параметри:
        s (str): вхідний рядок.
    Повертає:
        bool: True, якщо паліндром, інакше False.
    """
    cleaned = "".join(c.lower() for c in s if c.isalnum())

    def helper(sub):
        if len(sub) <= 1:
            return True
        if sub[0] != sub[-1]:
            return False
        return helper(sub[1:-1])

    return helper(cleaned)


# Тести
assert is_palindrome_iter("ротатор") is True and is_palindrome_rec("ротатор") is True
assert is_palindrome_iter("програма") is False and is_palindrome_rec("програма") is False
assert is_palindrome_iter("") is True and is_palindrome_rec("") is True