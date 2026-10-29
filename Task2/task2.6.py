# Задача 2.6: Обчислення a^n (з вводом)
a = int(input("Введіть основу (а): "))
n = int(input("Введіть показник степеня (n): "))
res = 1

for i in range(1, n + 1):
  res *= a

print(f"{a}^{n} = {res}")