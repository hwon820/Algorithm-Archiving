from collections import deque

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0; speeds = deque(speeds)
        while progresses[0] < 100:
            progresses = deque([progresses[i]+speeds[i] for i in range(len(progresses))])
        while len(progresses) != 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        answer.append(cnt)

    return answer