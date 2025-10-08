from collections import deque
from math import ceil
def solution(progresses, speeds):

    progresses = deque(progresses); speeds = deque(speeds)
    ans = []
    
    while progresses:
        prog = progresses.popleft(); sp = speeds.popleft()
        cnt = 1
        
        rounds = ceil((100 - prog) / sp) # 현재 prog가 완료되기 위해 필요한 days
        
        while progresses:
            n_prog = progresses.popleft(); n_sp = speeds.popleft()
            if n_prog + rounds * n_sp >= 100:
                cnt += 1
            else:
                progresses.appendleft(n_prog); speeds.appendleft(n_sp)
                break
        ans.append(cnt)
    
    return ans