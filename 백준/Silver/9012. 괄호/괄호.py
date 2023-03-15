import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  vps = input()
  stack = []
  for v in vps:
    if v == '(':
      stack.append(v)
    elif v == ')':
      if stack:
        stack.pop()
      else:
        print("NO")
        break
  else:
    if len(stack) == 0:
      print('YES')
    else:
      print('NO')