a = list(map(int, input("Введіть список через пробіл: ").split()))

seen = set()
res = []
for x in a:
  if x not in seen:
    seen.add(x)
    res.append(x)

print(res)