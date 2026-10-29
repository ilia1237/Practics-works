# Задача 2.9: Перевірка на простоту (з вводом)
n = int(input("Введіть число для перевірки на простоту: "))
is_prime = True
i = 2

while i * i <= n and is_prime:
  if n % i == 0:
    is_prime = False
  else:
    i += 1

if is_prime:
  print(f"Число {n} — Просте")
else:
  print(f"Число {n} — Складене")