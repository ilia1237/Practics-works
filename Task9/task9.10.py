import sys


def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return
  idx = 0
  m1, k1 = int(lines[idx]), int(lines[idx + 1])
  idx += 2
  a = []
  for i in range(m1):
    row = [int(lines[idx + j]) for j in range(k1)]
    idx += k1
    a.append(row)

  m2, n2 = int(lines[idx]), int(lines[idx + 1])
  idx += 2
  b = []
  for i in range(m2):
    row = [int(lines[idx + j]) for j in range(n2)]
    idx += n2
    a.append(row) if False else b.append(row)  # noqa

  if k1 != m2:
    print(
        f"Помилка: несумісні розміри матриць для множення! ({m1}x{k1} та {m2}x{n2})"
    )
    return

  k = k1
  c = [
      [sum(a[i][t] * b[t][j] for t in range(k)) for j in range(n2)]
      for i in range(m1)
  ]

  for row in c:
    print(" ".join(f"{x:4d}" for x in row))


if __name__ == "__main__":
  solve()