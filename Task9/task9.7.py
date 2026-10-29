import sys


def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return
  m, n = int(lines[0]), int(lines[1])
  idx = 2
  a = []
  for i in range(m):
    row = [int(lines[idx + j]) for j in range(n)]
    idx += n
    a.append(row)

  r1, r2 = int(lines[idx]), int(lines[idx + 1])
  c1, c2 = int(lines[idx + 2]), int(lines[idx + 3])

  # Обмін рядків
  a[r1], a[r2] = a[r2], a[r1]

  # Обмін стовпців
  for r in range(m):
    a[r][c1], a[r][c2] = a[r][c2], a[r][c1]

  for row in a:
    print(" ".join(f"{x:4d}" for x in row))


if __name__ == "__main__":
  solve()