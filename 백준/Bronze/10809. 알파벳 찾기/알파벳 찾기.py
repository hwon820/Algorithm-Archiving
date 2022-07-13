s = list(input())
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp:
  if i in s:
    print(s.index(i), end = ' ')
  else:
    print(-1, end = ' ')      
        