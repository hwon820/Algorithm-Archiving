
import heapq

def solution(maps):

    R, C = len(maps), len(maps[0])  # 인덱스 최대값

    # 미방문 길을 전부 무한으로로 변환
    maps = [[float("inf") if maps[r][c] else 0 for c in range(C)] for r in range(R)]
    
    # 초기화
    maps[0][0] = 1
    queue = []
    heapq.heappush(queue, (1, 0, 0))  # (몇칸이동, r, c)

    while queue:
        cv, cr, cc = heapq.heappop(queue)
        
        # 동서남북 탐색
        for rd, cd, in ((-1, 0),(0, 1),(1, 0),(0,-1)):
            nr, nc = cr + rd, cc + cd

            # 탐색하려는 인덱스가 존재하고 길이 있을 때
            if nr in range(R) and nc in range(C) and maps[nr][nc]:  
                if cv + 1 < maps[nr][nc]:  # 탐색한 블럭의 값보다 현재 칸에서 1보 전진한 게 작으면(최단거리면)
                    maps[nr][nc] = cv + 1
                    heapq.heappush(queue, (maps[nr][nc], nr, nc))  # heapq 업데이트
    
    return -1 if maps[R-1][C-1] == float("inf") else maps[R-1][C-1]