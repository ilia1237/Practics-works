def solve_5_9(weight, ticket_class):
  if ticket_class == "econom":
    limit = 20
  elif ticket_class == "business":
    limit = 30
  else:
    return "невідомий клас"

  excess = weight - limit
  fee = excess * 15 if excess > 0 else 0
  return int(fee) if fee.is_integer() else fee


# Тести:
print(solve_5_9(18, "econom"))  # Очікується: 0
print(solve_5_9(25, "econom"))  # Очікується: 75 (5 кг * 15 грн)
print(solve_5_9(35, "business"))  # Очікується: 75 (5 кг * 15 грн)
print(solve_5_9(30, "business"))  # Очікується: 0 (рівно ліміту)