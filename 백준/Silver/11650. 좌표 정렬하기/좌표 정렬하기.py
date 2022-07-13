#11650

n = int(input())
tu_list = []
for i in range(n):
  a, b = map(int,input().split())
  tu_list.append((a,b))

lst = sorted(tu_list, key = lambda x : (x[0],x[1]))

for i in range(len(lst)):
  print(lst[i][0], lst[i][1])