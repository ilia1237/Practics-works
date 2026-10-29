date_num = int(input("Введіть дату у форматі ДДММРР: "))
day = date_num // 10000
month = (date_num // 100) % 100
year = date_num % 100

print(f"{day:02d}.{month:02d}.20{year:02d}")