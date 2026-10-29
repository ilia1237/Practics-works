import math

class Vector:
    """Двовимірний вектор (x, y)."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1 + v2 == Vector(4, 6)
    assert v1 * v2 == 11
    assert abs(Vector(3, 4)) == 5.0