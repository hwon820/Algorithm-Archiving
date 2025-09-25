# 50X50에 사각형 그리기
# 일단 사각형 그리고(1로 채우기) 테두리만 남기기 
# 그리고 최단 탐색 ㄱㄱ하면 될 듯

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # -1로 채우고 사각형 외부는 -1, 내부는 0, 테두리는 1
    mapp = [[-1] * 102 for _ in range(102)]
    
    for rec in rectangle:
        # 모든 값 X 2 해야 길이 밀접할 때 안 헷갈림ㅠ
        min_x, min_y, max_x, max_y = map(lambda x: x*2, rec)
        
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y +1):
                if min_x < x < max_x and min_y < y < max_y:  # 가장자리(min or max 포함) 아니면 0
                    mapp[x][y] = 0
                elif mapp[x][y] != 0:   # 다른 사각형이 이미 내부로 처리했다면 pass / 아니면 1
                    mapp[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
                    
    q = deque()
    q.append([characterX*2, characterY*2]) # 캐릭터 위치 
    
    visited = [[1] * 102 for _ in range(102)]   # 방문 여부 map: 방문 안 했으면 1
    visited[characterX * 2][characterY * 2] = 0 # 시작지점 0
    
    while q:
        x, y = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if mapp[nx][ny] == 1 and visited[nx][ny] == 1:  # 길이 있고 방문하지 않았다면
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer