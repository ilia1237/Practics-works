import math

# Введення списку цілих чисел одним рядком
a = list(map(int, input("Введіть список через пробіл: ").split()))

s = sum(a)
prod = math.prod(a) if a else 0
n = len(a)
mean = s / n if n > 0 else 0

print(f"Сума: {s}, добуток: {prod}, n={n}, середнє: {mean:.2f}")