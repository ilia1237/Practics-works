# Задача 2.8: Усі дільники числа n (з вводом)
n = int(input("Введіть натуральне число n: "))
divisors = []

for i in range(1, n + 1):
  if n % i == 0:
    divisors.append(i)

print(f"Дільники числа {n}: {divisors}")