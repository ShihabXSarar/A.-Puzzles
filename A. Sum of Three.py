def solve(n):

  for x in range(1, n // 3 + 1):

    for y in range(x + 1, n // 2 + 1):
      z = n - x - y

      if z > y and z % 3 != 0 and y % 3 != 0 and x % 3 != 0:
        return "YES\n" + str(x) + " " + str(y) + " " + str(z)

  return "NO"

t = int(input())

for i in range(t):

  n = int(input())

  print(solve(n))


