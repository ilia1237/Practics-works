import math

a, b = map(int, input().split())

gcd_val = math.gcd(a, b)
lcm_val = (a * b) // gcd_val

print(f"НСД = {gcd_val}, НСК = {lcm_val}")