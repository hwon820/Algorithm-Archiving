n, m = map(int, input().split())
memo = {}
srch = []
for i in range(n+m):
  if i < n:
    a, b = input().split()
    memo[a] = b
  else:
    c = input()
    srch.append(c)

for i in srch:
  if i in memo.keys():
    print(memo[i])