import sys


def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return
  n = int(lines[0])  # квадратна матриця (m = n)
  _ = int(lines[1])
  idx = 2
  a = []
  for i in range(n):
    row = [int(lines[idx + j]) for j in range(n)]
    idx += n
    a.append(row)

  main_diag = sum(a[i][i] for i in range(n))
  anti_diag = sum(a[i][n - 1 - i] for i in range(n))

  print(f"головна = {main_diag}, побічна = {anti_diag}")


if __name__ == "__main__":
  solve()