m = int(input("Введіть кількість хвилин: "))
days = m // 1440
hours = (m % 1440) // 60
minutes = m % 60

print(f"{days} діб {hours} год {minutes} хв")