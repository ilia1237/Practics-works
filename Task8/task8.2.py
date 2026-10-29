a = list(map(int, input("Введіть список через пробіл: ").split()))

if a:
  mx = max(a)
  mx_idx = a.index(mx)
  mn = min(a)
  mn_idx = a.index(mn)
  print(f"max={mx} (індекс {mx_idx}), min={mn} (індекс {mn_idx})")
else:
  print("Список порожній.")