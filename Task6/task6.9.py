n = int(input("n = "))

count = 0
output = ""

for num in range(2, n + 1):
    is_prime = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            is_prime = False
            break
        d += 1
        
    if is_prime:
        output += f"{num} "
        count += 1

print(f"{output.strip()} ({count} чисел)")