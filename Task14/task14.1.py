import math

class Rectangle:
    """Прямокутник зі сторонами a та b."""
    
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Сторони прямокутника повинні бути додатними")
        self.a = a
        self.b = b

    def area(self) -> float:
        """Обчислює площу прямокутника."""
        return self.a * self.b

    def perimeter(self) -> float:
        """Обчислює периметр прямокутника."""
        return 2 * (self.a + self.b)

    def is_square(self) -> bool:
        """Перевіряє, чи є прямокутник квадратом."""
        return self.a == self.b

    @property
    def diagonal(self) -> float:
        """Повертає довжину діагоналі прямокутника."""
        return math.hypot(self.a, self.b)

    def __str__(self) -> str:
        return f"Прямокутник({self.a} x {self.b})"

    def __repr__(self) -> str:
        return f"Rectangle(a={self.a}, b={self.b})"

if __name__ == "__main__":
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14
    assert not r.is_square()