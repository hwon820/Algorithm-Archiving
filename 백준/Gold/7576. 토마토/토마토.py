from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 좌표
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

res = 0

# 토마토 위치 확인
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

# bfs. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 좌표 범위 내 & 익지 않은 토마토 존재
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)