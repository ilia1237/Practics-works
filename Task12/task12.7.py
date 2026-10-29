from collections import defaultdict


def get_ects(score):
  if score >= 90:
    return "A"
  elif score >= 82:
    return "B"
  elif score >= 75:
    return "C"
  elif score >= 68:
    return "D"
  elif score >= 60:
    return "E"
  else:
    return "FX"


groups = defaultdict(list)
for name, score in students:
  groups[get_ects(score)].append(name)

print(dict(groups))