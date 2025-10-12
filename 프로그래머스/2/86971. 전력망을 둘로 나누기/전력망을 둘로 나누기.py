from collections import deque

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    cnt = 0
    while que:
        
        temp = que.popleft()
        cnt +=1
        
        for i in graph[temp]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

    return cnt

def solution(n, wires):
    answer = n-2
    for i in range(len(wires)):
        temp = wires.copy()
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        temp.pop(i)
        for wire in temp:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
            
        for idx, g in enumerate(graph):
            if g != []:
                start = idx; break
        cnt = bfs(graph, start, visited)
        other = n - cnt
        if abs(cnt - other) < answer: # Worst Case
            answer = abs(cnt - other)
    
    
    return answer