import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
queue = deque(list(range(n, 0, -1)))
for _ in range(n-1):
    queue.pop()
    top = queue.pop()
    queue.appendleft(top)

print(queue[0])