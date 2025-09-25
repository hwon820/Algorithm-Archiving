import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer = 0
    while True:
        temp = heapq.heappop(scoville)
        if temp >= K:
            heapq.heappush(scoville, temp)
            break
        else:
            if len(scoville) != 0:
                num = heapq.heappop(scoville)
                heapq.heappush(scoville, temp + (num*2))
                answer += 1
            else:
                answer = -1
                break
    return answer