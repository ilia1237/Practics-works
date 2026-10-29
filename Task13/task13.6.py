def read_int(prompt: str = "Введіть ціле число: ") -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Неправильне значення. Введіть ціле число.")

def read_int_mock(inputs: list) -> int:
    """Імітація введення через список тестових значень."""
    iterator = iter(inputs)
    while True:
        try:
            val = next(iterator)
            return int(val)
        except StopIteration:
            raise ValueError("Тестовий список введень вичерпано, а коректне число не знайдено.")
        except ValueError:
            # Ігноруємо некоректне значення і переходимо до наступного в ітераторі
            continue