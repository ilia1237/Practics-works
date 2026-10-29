def solve_5_6(score):
  if 90 <= score <= 100:
    return "A"
  elif 82 <= score <= 89:
    return "B"
  elif 74 <= score <= 81:
    return "C"
  elif 64 <= score <= 73:
    return "D"
  elif 60 <= score <= 63:
    return "E"
  elif 35 <= score <= 59:
    return "FX"
  elif 0 <= score <= 34:
    return "F"
  else:
    return "помилка (бал поза межами 0-100)"


# Тести:
print(solve_5_6(95))  # Очікується: A
print(solve_5_6(60))  # Очікується: E (межовий випадок)
print(solve_5_6(40))  # Очікується: FX
print(solve_5_6(12))  # Очікується: F