def solve_5_10(age, gender):
  if age < 18:
    return "так"
  elif gender == "ж" and age >= 60:
    return "так"
  elif gender == "ч" and age >= 65:
    return "так"
  else:
    return "ні"


# Тести:
print(solve_5_10(12, "ч"))  # Очікується: так (дитина до 18 років)
print(solve_5_10(30, "ж"))  # Очікується: ні (доросла жінка до 60)
print(solve_5_10(62, "ж"))  # Очікується: так (жінка від 60)
print(solve_5_10(62, "ч"))  # Очікується: ні (чоловік ще не досяг 65)