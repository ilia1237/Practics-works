n = int(input("n = "))
reversed_n = 0

m = n
while m > 0:
    digit = m % 10
    reversed_n = reversed_n * 10 + digit
    m //= 10

print(reversed_n)