s = "абракадабра"
char = "а"

indices = [i for i, c in enumerate(s) if c == char]

print(f"{len(indices)} разів, індекси {' '.join(map(str, indices))}")