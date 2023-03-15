#10828

import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
  com = input().rstrip()
  #push
  if len(com.split()) == 2:
    stack.append(int(com.split()[1]))
  #pop
  elif com == 'pop':
    if len(stack) != 0:
      print(stack.pop())
    else:
      print(-1)
  #size
  elif com == 'size':
    print(len(stack))
  #empty
  elif com == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  #top
  elif com == 'top':
    if len(stack) != 0:
      print(stack[-1])
    else:
      print(-1)