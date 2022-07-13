import sys
input=sys.stdin.readline
n = int(input())
tu_list = []
for i in range(n):
  a, b = input().split()
  tu_list.append((int(a), b))

lst = sorted(tu_list, key = lambda x : x[0])
for i in range(len(lst)):
  print(lst[i][0], lst[i][1])