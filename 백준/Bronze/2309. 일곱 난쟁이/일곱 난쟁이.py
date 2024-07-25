from itertools import combinations
import sys
input = sys.stdin.readline

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

comb = list(combinations(dwarf, 7))

for one in comb:
  if sum(one) == 100:
    result = list(one)
    result.sort()
    for i in result:
        print(i)
    break