s = "тел. 380-67-123"

replaced = "".join("#" if c.isdigit() else c for c in s)
count = sum(1 for c in s if c.isdigit())

print(f'"{replaced}", замін {count}')