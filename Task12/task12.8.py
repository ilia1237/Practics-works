# Сортуємо за балом спадання (-kv[1]), а при рівності — за прізвищем зростання (kv[0])
sorted_items = sorted(students, key=lambda kv: (-kv[1], kv[0]))
print(sorted_items)