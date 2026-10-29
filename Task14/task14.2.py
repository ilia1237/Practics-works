import math

class Circle:
    """Коло з радіусом r."""
    
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("Радіус кола повинен бути додатним")
        self.r = r

    def area(self) -> float:
        """Обчислює площу кола."""
        return math.pi * self.r ** 2

    def circumference(self) -> float:
        """Обчислює довжину кола."""
        return 2 * math.pi * self.r

    def scale(self, k: float):
        """Збільшує або зменшує радіус кола у k разів."""
        if k <= 0:
            raise ValueError("Коефіцієнт масштабування має бути додатним")
        self.r *= k

    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.r == other.r

    def __lt__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.r < other.r

    def __str__(self) -> str:
        return f"Коло(r={self.r})"

    def __repr__(self) -> str:
        return f"Circle(r={self.r})"

if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(10)
    assert c1.area() == math.pi * 25
    assert c1 < c2
    assert not (c1 == c2)