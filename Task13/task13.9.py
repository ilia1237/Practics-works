def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None


class InvalidGradeError(ValueError):
    """Виняток для балів, що виходять за межі діапазону 0..100."""
    pass


def check_grade(score):
    if not isinstance(score, (int, float)) or not (0 <= score <= 100):
        raise InvalidGradeError(f"Бал {score} є неприпустимим (має бути від 0 до 100).")
    return f"Бал {score} успішно перевірено."