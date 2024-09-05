import heapq

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) 
    graph[b].append((c, a))  

visited = [False] * (v + 1) 
min_heap = [(0, 1)] 
total_weight = 0

while min_heap:
    weight, u = heapq.heappop(min_heap)
    
    if visited[u]:
        continue
    
    visited[u] = True
    total_weight += weight

    for edge in graph[u]:
        if not visited[edge[1]]:
            heapq.heappush(min_heap, edge)

print(total_weight)