t = int(input())

for i in range(t):
  c = list(map(int,input().split()))
  c.sort(reverse = True)
  print(c[2])