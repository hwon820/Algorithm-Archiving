import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v); graph[v].append(u)

count = 0
visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
       if not visited[i]:
          dfs(graph, i, visited)

for node in range(1, n+1):
    if not visited[node]:
        dfs(graph, node, visited)
        count += 1

print(count)