n = int(input())

for i in range(n):
  a, b = input().split()
  al = list(a)
  bl = list(b)
  al.sort()
  bl.sort()
  if al == bl:
    print(a + ' & ' + b + ' are anagrams.')
  else:
    print(a + ' & ' + b + ' are NOT anagrams.')   