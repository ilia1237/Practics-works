def solve_5_7(month):
  if month in (12, 1, 2):
    return "зима"
  elif month in (3, 4, 5):
    return "весна"
  elif month in (6, 7, 8):
    return "літо"
  elif month in (9, 10, 11):
    return "осінь"
  else:
    return "помилка"


# Тести:
print(solve_5_7(1))  # Очікується: зима
print(solve_5_7(4))  # Очікується: весна
print(solve_5_7(13))  # Очікується: помилка (більше 12)
print(solve_5_7(0))  # Очікується: помилка (менше 1)