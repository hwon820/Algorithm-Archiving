# bfs
from collections import deque
def solution(n, computers):
    now_net = deque([(computers[0], 0)]); cnt = 0
    visited = [0] * n; visited[0] = 1
    
    while now_net:
        temp, idx = now_net.popleft()
        
        for i in range(n):
            if temp[i] == 1 and visited[i] == 0:
                now_net.append((computers[i], i))
                visited[i] = 1
                
        if not now_net:
            cnt += 1
            for c in range(n):
                if visited[c] == 0:
                    now_net.append((computers[c], c)); visited[c] = 1
                    break
                    
    return cnt
                
                