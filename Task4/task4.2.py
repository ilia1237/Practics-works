n = int(input("Введіть п'ятицифрове число: "))
d1 = n % 10
d2 = (n // 10) % 10
d3 = (n // 100) % 10
d4 = (n // 1000) % 10
d5 = n // 10000

suma = d1 + d2 + d3 + d4 + d5
dobutok = d1 * d2 * d3 * d4 * d5
print(f"сума = {suma}, добуток = {dobutok}")