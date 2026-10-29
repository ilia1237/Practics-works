set_a, set_b = set(a), set(b)

common = set_a & set_b  # Спільні елементи
only_a = set_a - set_b  # Лише в першому
only_b = set_b - set_a  # Лише в другому
union = set_a | set_b  # Об'єднання

print("Спільні:", common)
print("Лише в a:", only_a)
print("Лише в b:", only_b)
print("Об'єднання:", union)