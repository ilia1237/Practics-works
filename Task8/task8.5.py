a = list(map(int, input("Введіть список через пробіл: ").split()))

res = []
for i in range(len(a) - 1, -1, -1):
  res.append(a[i])

print(res)