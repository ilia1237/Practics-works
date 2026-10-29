total = int(input("Введіть суму в копійках: "))
hryvnia = total // 100
kopiyka = total % 100

print(f"{hryvnia} грн {kopiyka:02d} коп")