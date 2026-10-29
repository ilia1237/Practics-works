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

  total_sum = 0
  best_max = a[0][0]
  max_pos = (0, 0)
  best_min = a[0][0]
  min_pos = (0, 0)

  for i in range(m):
    for j in range(n):
      val = a[i][j]
      total_sum += val
      if val > best_max:
        best_max = val
        max_pos = (i, j)
      if val < best_min:
        best_min = val
        min_pos = (i, j)

  print(
      f"max={best_max} {max_pos}, min={best_min} {min_pos}, сума={total_sum}"
  )


if __name__ == "__main__":
  solve()