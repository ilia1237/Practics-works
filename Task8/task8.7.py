a = list(map(int, input("Введіть список через пробіл: ").split()))
original_len = len(a)

# Формування нового списку без від'ємних елементів
a_filtered = [x for x in a if x >= 0]
removed_count = original_len - len(a_filtered)

print(f"Результат: {a_filtered}, видалено {removed_count}")