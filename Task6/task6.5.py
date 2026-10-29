n = int(input("n = "))
count = 0

divisors = ""
for d in range(1, n + 1):
    if n % d == 0:
        divisors += f"{d} "
        count += 1

print(f"{divisors.strip()} ({count} дільників)")