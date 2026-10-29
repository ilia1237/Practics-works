print("Введіть перший відсортований список:")
a = list(map(int, input().split()))

print("Введіть другий відсортований список:")
b = list(map(int, input().split()))

res = []
i, j = 0, 0

# Двопотокове злиття (Merge двох відсортованих послідовностей)
while i < len(a) and j < len(b):
  if a[i] <= b[j]:
    res.append(a[i])
    i += 1
  else:
    res.append(b[j])
    j += 1

# Додаємо залишки, якщо один зі списків добіг кінця
res.extend(a[i:])
res.extend(b[j:])

print(f"Злитий відсортований список: {res}")