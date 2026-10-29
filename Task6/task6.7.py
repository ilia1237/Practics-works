n = int(input("n = "))

a, b = 0, 1
total_sum = 0
output = ""

for _ in range(n):
    output += f"{a} "
    total_sum += a
    a, b = b, a + b

print(f"{output.strip()}, сума = {total_sum}")