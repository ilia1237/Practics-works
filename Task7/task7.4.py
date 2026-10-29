s = "я вивчаю алгоритмізацію"

words = s.split()
longest = max(words, key=len) if words else ""

print(f"{len(words)} слова, найдовше \"{longest}\"")