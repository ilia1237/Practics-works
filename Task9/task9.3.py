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

  t = [[a[i][j] for i in range(m)] for j in range(n)]

  for row in t:
    print(" ".join(f"{x:4d}" for x in row))


if __name__ == "__main__":
  solve()