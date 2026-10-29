cm = int(input("Введіть кількість сантиметрів: "))
meters = cm // 100
rem_cm = cm % 100
inches = int(cm / 2.54)

print(f"{meters} м {rem_cm} см, {inches} дюймів")