word = input()
word = word.upper()
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

_max = -1000000000000

for i in alp:
  if word.count(i) > _max:
    _max = word.count(i)
    can = i
  elif word.count(i) == _max:
    can = '?'

print(can)