a = list(map(int, input("Введіть список через пробіл: ").split()))

# Елементи з парними індексами (0, 2, 4...) та непарними (1, 3, 5...)
sum_even_idx = sum(a[0::2])
sum_odd_idx = sum(a[1::2])

print(f"парні індекси {sum_even_idx}, непарні {sum_odd_idx}")