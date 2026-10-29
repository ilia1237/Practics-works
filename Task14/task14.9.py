from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Абстрактний базовий клас геометричної фігури."""
    
    @abstractmethod
    def area(self) -> float:
        """Площа фігури."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Периметр фігури."""
        pass

class RectangleShape(Shape):
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0: raise ValueError("Сторони мають бути додатними")
        self.a, self.b = a, b
    def area(self): return self.a * self.b
    def perimeter(self): return 2 * (self.a + self.b)
    def __str__(self): return f"Rectangle(S={self.area()})"
    def __repr__(self): return f"RectangleShape({self.a}, {self.b})"

class CircleShape(Shape):
    def __init__(self, r: float):
        if r <= 0: raise ValueError("Радіус має бути додатним")
        self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r
    def __str__(self): return f"Circle(S={self.area():.2f})"
    def __repr__(self): return f"CircleShape({self.r})"

class TriangleShape(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Некоректні сторони трикутника")
        self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def __str__(self): return f"Triangle(S={self.area():.2f})"
    def __repr__(self): return f"TriangleShape({self.a}, {self.b}, {self.c})"

if __name__ == "__main__":
    shapes = [RectangleShape(2, 3), CircleShape(2), TriangleShape(3, 4, 5)]
    sorted_shapes = sorted(shapes, key=lambda s: s.area())
    assert len(sorted_shapes) == 3
    assert isinstance(sorted_shapes[0], Shape)
    assert sorted_shapes[0].area() <= sorted_shapes[1].area()