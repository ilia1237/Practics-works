n = int(input("n = "))
m = n

max_digit = m % 10
min_digit = m % 10
m //= 10

while m > 0:
    digit = m % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    m //= 10

print(f"max = {max_digit}, min = {min_digit}")