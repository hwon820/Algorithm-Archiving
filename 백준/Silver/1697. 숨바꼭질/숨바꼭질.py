import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
queue = deque([(n, 0)])
visited = [False] * 100001

while True:
    val, sec = queue.popleft()
    
    if val == k:
        print(sec)
        break  
        
    if not visited[val]:
        visited[val] = True
        if val - 1 >= 0:
            queue.append((val - 1, sec + 1))
        if val + 1 <= 100000:
            queue.append((val + 1, sec + 1))
        if val * 2 <= 100000:
            queue.append((val * 2, sec + 1))