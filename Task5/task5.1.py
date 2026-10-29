def solve_5_1(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c


# Тести:
print(solve_5_1(5, 9, 2))  # Очікується: 9
print(solve_5_1(7, 7, 7))  # Очікується: 7 (межовий випадок рівності)
print(solve_5_1(-1, -5, -3))  # Очікується: -1 (від'ємні числа)
print(solve_5_1(10, 3, 10))  # Очікується: 10 (рівність двох максимальних)