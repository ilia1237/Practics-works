n = int(input("n = "))
count_all = 0
count_even = 0

m = n
while m > 0:
    digit = m % 10
    count_all += 1
    if digit % 2 == 0:
        count_even += 1
    m //= 10

print(f"цифр = {count_all}, парних = {count_even}")