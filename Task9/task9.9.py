import sys


def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return
  n = int(lines[0])
  _ = int(lines[1])
  idx = 2
  a = []
  for i in range(n):
    row = [int(lines[idx + j]) for j in range(n)]
    idx += n
    a.append(row)

  b = [[a[n - 1 - j][i] for j in range(n)] for i in range(n)]

  for row in b:
    print(" ".join(f"{x:4d}" for x in row))


if __name__ == "__main__":
  solve()