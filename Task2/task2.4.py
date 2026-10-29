# Задача 2.4: Сума цифр натурального числа (з вводом)
n = int(input("Введіть натуральне число: "))
sum_digits = 0
temp = n

while temp > 0:
  sum_digits += temp % 10
  temp //= 10

print(f"Сума цифр числа {n} = {sum_digits}")