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

  above = sum(a[i][j] for i in range(n) for j in range(n) if i < j)
  below = sum(a[i][j] for i in range(n) for j in range(n) if i > j)

  print(f"вище = {above}, нижче = {below}")


if __name__ == "__main__":
  solve()