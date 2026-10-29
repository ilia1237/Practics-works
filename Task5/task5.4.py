def solve_5_4(x, y):
  if x == 0 and y == 0:
    return "початок координат"
  elif x == 0 or y == 0:
    return "на осі"
  elif x > 0 and y > 0:
    return "I"
  elif x < 0 and y > 0:
    return "II"
  elif x < 0 and y < 0:
    return "III"
  else:
    return "IV"


# Тести:
print(solve_5_4(3, 4))  # Очікується: I
print(solve_5_4(-2, 5))  # Очікується: II
print(solve_5_4(0, 7))  # Очікується: на осі (на осі OY)
print(solve_5_4(0, 0))  # Очікується: початок координат