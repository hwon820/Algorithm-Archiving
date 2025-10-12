# bfs

from collections import deque

def solution(maps):
    route = deque([(0, 0)])
    n = len(maps); m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while route:
        nx, ny = route.popleft()
        
        for i in range(4):
            nxt_x, nxt_y = nx+dx[i], ny+dy[i]
            
            if -1 < nxt_x < n and -1 < nxt_y < m:
                if maps[nxt_x][nxt_y] == 1:
                    maps[nxt_x][nxt_y] = maps[nx][ny] + 1
                    route.append((nxt_x, nxt_y))
                elif maps[nxt_x][nxt_y] > 1:
                    if maps[nxt_x][nxt_y] > maps[nx][ny] + 1:
                        maps[nxt_x][nxt_y] = maps[nx][ny] + 1
                        route.append((nxt_x, nxt_y))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
                    
                