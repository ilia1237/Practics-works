import sys


def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return
  m, n = int(lines[0]), int(lines[1])
  idx = 2
  pos = neg = zero = 0

  for i in range(m * n):
    val = int(lines[idx + i])
    if val > 0:
      pos += 1
    elif val < 0:
      neg += 1
    else:
      zero += 1

  print(f"додатних {pos}, від'ємних {neg}, нулів {zero}")


if __name__ == "__main__":
  solve()