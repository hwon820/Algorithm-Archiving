import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  line = list(input().split())
  for i in range(len(line)):
    print(line[i][::-1], end = ' ')