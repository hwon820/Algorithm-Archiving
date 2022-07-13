a, b = input().split()
a = list(a)
b = list(b)

a.reverse()
b.reverse()

_a = int(a[0])*100+int(a[1])*10+int(a[2])
_b = int(b[0])*100+int(b[1])*10+int(b[2])

if _a > _b:
  print(_a)
else:
  print(_b)