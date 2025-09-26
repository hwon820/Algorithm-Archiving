# 대기 큐 원소 : (작업의 번호, 작업의 요청 시각, 작업의 소요 시간)
#    우선 순위 :      3            2              1

# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높
import heapq

def solution(jobs):
    jobs.sort()  # 요청 시각 기준 정렬
    n = len(jobs)
    heap = []
    time, total, i = 0, 0, 0
    
    while i < n or heap:
        # 현재 시간까지 들어온 작업을 힙에 넣기
        while i < n and jobs[i][0] <= time:
            req, dur = jobs[i]
            heapq.heappush(heap, (dur, req))
            i += 1
        
        if heap:  # 처리할 수 있는 작업이 있으면
            dur, req = heapq.heappop(heap)
            time += dur
            total += time - req  # 대기시간 + 실행시간
        else:  # 아직 도착 안 한 작업 있으면, 시간 점프
            time = jobs[i][0]
    
    return total // n
