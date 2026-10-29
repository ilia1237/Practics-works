import math

class Fraction:
    """Звичайний дріб з автоматичним скороченням."""
    
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        common = math.gcd(numerator, denominator)
        self.num = numerator // common
        self.den = denominator // common

    def to_float(self) -> float:
        """Перетворює дріб на число з плаваючою комою."""
        return self.num / self.den

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.num * other.num, self.den * other.den)

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.num == other.num and self.den == other.den

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.num * other.den < other.num * self.den

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

if __name__ == "__main__":
    f1 = Fraction(2, 4)
    f2 = Fraction(1, 3)
    assert f1.num == 1 and f1.den == 2
    assert f1 + f2 == Fraction(5, 6)
    assert f2 < f1