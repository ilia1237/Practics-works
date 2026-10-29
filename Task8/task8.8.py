a = list(map(int, input("Введіть список через пробіл: ").split()))
k = int(input("Введіть кількість позицій для зсуву (k): "))

if a:
  k = k % len(a)  # Захист, якщо k перевищує довжину списку
  shifted = a[k:] + a[:k]
  print(f"Результат зсуву на k={k}: {shifted}")
else:
  print([])