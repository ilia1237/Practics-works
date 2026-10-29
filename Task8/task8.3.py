a = list(map(int, input("Введіть список через пробіл: ").split()))

pos = sum(1 for x in a if x > 0)
neg = sum(1 for x in a if x < 0)
zero = sum(1 for x in a if x == 0)

print(f"додатних {pos}, від'ємних {neg}, нулів {zero}")