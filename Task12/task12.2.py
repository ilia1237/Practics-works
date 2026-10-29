words = text.split()
counts = {}
for w in words:
  counts[w] = counts.get(w, 0) + 1

# Фільтруємо слова, що зустрічаються більше одного разу
duplicates = {w: cnt for w, cnt in counts.items() if cnt > 1}
print(duplicates)