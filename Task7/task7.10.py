s = "абракадабра"

filtered = [c for c in s if c != " "]
most_common = max(set(filtered), key=filtered.count) if filtered else ""
count = filtered.count(most_common)

print(f"'{most_common}', {count} разів")