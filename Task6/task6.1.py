n = int(input("Введіть натуральне число n: "))
s = 0
p = 1
m = n

while m > 0:
    digit = m % 10
    s += digit
    p *= digit
    m //= 10

print(f"Сума цифр = {s}, добуток цифр = {p}")