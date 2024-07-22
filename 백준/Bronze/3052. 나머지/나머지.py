import sys
input = sys.stdin.readline

results = set([])

for _ in range(10):
    temp = int(input())
    results.add(temp%42)

print(len(results))