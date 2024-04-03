import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        min_ = heapq.heappop(scoville)
        if min_ < K:
            if len(scoville) == 0:
                return -1
            else:
                heapq.heappush(scoville, min_ + heapq.heappop(scoville) * 2)
                answer += 1
        else:
            break

    return answer