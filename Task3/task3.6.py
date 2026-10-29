import math

a, b = map(float, input().split())

c = math.hypot(a, b)
p = a + b + c
s = 0.5 * a * b

print(f"c = {c:.2f}, P = {p:.2f}, S = {s:.2f}")