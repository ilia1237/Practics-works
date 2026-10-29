sum_dep, rate = map(float, input().split())

total = sum_dep * (1 + rate / 100) ** 3

print(f"{total:.2f}")