#2798

n, key = map(int,input().split())
lst = list(map(int,input().split()))

from itertools import *
#combinations -> 조합!

can = list(combinations(lst,3)) #리스트 내 원소 조합
can_ = []
for i in can:
  can_.append(sum(i))

_max = 0
for i in can_:
  if i > key:
    continue
  else:
    _max = max(_max,i)

print(_max)