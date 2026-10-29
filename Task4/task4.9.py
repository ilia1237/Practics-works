n = int(input("Введіть двоцифрове число: "))
d1 = n // 10
d2 = n % 10
rev = d2 * 10 + d1
suma = n + rev

print(f"{rev}, сума = {suma}")