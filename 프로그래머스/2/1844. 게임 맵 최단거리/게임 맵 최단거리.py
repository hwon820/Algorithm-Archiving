from collections import deque

def solution(maps):
    
    n = len(maps); m = len(maps[0])
    que = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]; visited[0][0] = 1
    
    while que:
        temp = que.popleft()
        dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in dr:
            nx = temp[0] + dx; ny = temp[1] + dy
            
            if -1 < nx < n and -1 < ny < m and maps[nx][ny] > 0 and visited[nx][ny] == 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[temp[0]][temp[1]] + 1
                else:
                    maps[nx][ny] = min(maps[nx][ny], maps[temp[0]][temp[1]] + 1)
                visited[nx][ny] = 1
                que.append((nx, ny))
                
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]