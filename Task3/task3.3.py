n = int(input())

d1 = n // 100
d2 = (n // 10) % 10
d3 = n % 10
s = d1 + d2 + d3

print(f"{d1} {d2} {d3}, сума = {s}")