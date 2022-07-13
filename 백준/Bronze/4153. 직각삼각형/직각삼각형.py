while True:
  lst = list(map(int,input().split()))
  
  if sum(lst) == 0:
    break
  else:
    a = max(lst)
    lst.remove(a)
    s = 0
    for i in lst:
     s += i**2
    if a**2 == s:
       print("right")
    else: 
       print("wrong")