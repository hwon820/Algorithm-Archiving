while True:
  num = int(input())
  if num == 0:
    break
  else:
    num = list(str(num))
  b = num.copy()
  b.reverse()
  if num == b:
   print("yes")
  else:
     print("no")