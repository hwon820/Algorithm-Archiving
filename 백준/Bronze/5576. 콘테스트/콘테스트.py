a = []
b = []
for i in range(20):
  if i < 10:
    a.append(int(input()))
  else:
    b.append(int(input()))

a.sort(reverse = True)
b.sort(reverse = True)

print(a[0]+a[1]+a[2], b[0]+b[1]+b[2])