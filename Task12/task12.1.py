from collections import Counter

text = "алгоритм це послідовність дій алгоритм має бути скінченним"
# Вилучаємо пробіли
chars = [ch for ch in text if ch != " "]
counter = Counter(chars)
top_3 = counter.most_common(3)
print(top_3)