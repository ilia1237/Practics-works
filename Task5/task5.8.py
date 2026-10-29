import math


def solve_5_8(a, b, c):
  if a == 0:
    if b == 0:
      return "безліч розв'язків" if c == 0 else "коренів немає"
    else:
      x = -c / b
      return f"лінійне: x={x}"
  else:
    D = b**2 - 4 * a * c
    if D > 0:
      x1 = (-b + math.sqrt(D)) / (2 * a)
      x2 = (-b - math.sqrt(D)) / (2 * a)
      return f"x1={x1}, x2={x2}"
    elif D == 0:
      x = -b / (2 * a)
      return f"x={x}"
    else:
      return "коренів немає"


# Тести:
print(solve_5_8(1, -3, 2))  # Очікується: x1=2.0, x2=1.0
print(solve_5_8(1, 2, 1))  # Очікується: x=-1.0 (D = 0)
print(solve_5_8(1, 0, 1))  # Очікується: коренів немає (D < 0)
print(solve_5_8(0, 2, 4))  # Очікується: лінійне: x=-2.0 (a = 0)