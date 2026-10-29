n = int(input("n = "))

sum_divisors = 0
for d in range(1, n):
    if n % d == 0:
        sum_divisors += d

if sum_divisors == n and n > 0:
    print("досконале")
else:
    print("не досконале")