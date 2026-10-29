n = int(input("n = "))

if n < 2:
    print("ні просте, ні складене")
else:
    is_prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            is_prime = False
            break
        d += 1

    if is_prime:
        print("просте")
    else:
        print("складене")