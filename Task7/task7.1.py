s = "програма"

length = len(s)
first = s[0] if length > 0 else ""
last = s[-1] if length > 0 else ""
reversed_s = s[::-1]

print(f"{length}, '{first}', '{last}', \"{reversed_s}\"")