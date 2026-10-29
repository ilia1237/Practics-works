a = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Спосіб 1: Через множину (set) — порядок не гарантується
unique_set = list(set(a))

# Спосіб 2: Зі збереженням порядку першої появи через dict.fromkeys()
unique_ordered = list(dict.fromkeys(a))

print("Через set:", unique_set)
print("Зі збереженням порядку:", unique_ordered)