s = "організація об'єднаних націй"

words = s.split()
titled = " ".join(w.capitalize() for w in words)
acronym = "".join(w[0].upper() for w in words if w)

print(f'"{titled}", {acronym}')