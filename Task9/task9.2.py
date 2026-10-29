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

  row_sums = [sum(row) for row in a]
  col_sums = [sum(a[i][j] for i in range(m)) for j in range(n)]

  print("рядки:", " ".join(map(str, row_sums)))
  print("стовпці:", " ".join(map(str, col_sums)))


if __name__ == "__main__":
  solve()