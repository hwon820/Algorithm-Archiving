a = int(input())
b = int(input())
c = int(input())

num = a*b*c
num = list(str(num))

for i in range(10):
  cnt = num.count(str(i))
  print(cnt)