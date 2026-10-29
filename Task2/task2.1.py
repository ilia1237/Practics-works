# Задача 2.1: Максимум із трьох чисел (з вводом)
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
c = int(input("Введіть третє число (c): "))

if a > b:
  if a > c:
    m = a
  else:
    m = c
else:
  if b > c:
    m = b
  else:
    m = c

print(f"Максимум із ({a}, {b}, {c}) = {m}")