# Counter 차집합 후 남은 0에 대해 번호를 맞추면 최대, 안 맞추면 최소
# 6 - (sum(temp.values())-temp[0]) = 0을 전부 일치시켰을 때의 일치개수 
# 6 - sum(temp.values()) = 0을 전부 불일치 시켰을 떄의 일치 개수
from collections import Counter
def solution(lottos, win_nums):
    temp = Counter(lottos) - Counter(win_nums)  
     # n이 일치 개수일때 순위: 6 - (n-1) = -n+7,  2<=n<=6
    if temp[0]: 
        min_ = 6 - (sum(temp.values())-temp[0])
        max_ = 6 - sum(temp.values())
        return [7 - min_ if min_ > 1 else 6, 7 - max_ if max_ > 1 else 6] 
    else:
        cnt = 6 - len(temp)
        return [7 - cnt, 7 - cnt] if cnt > 1 else [6, 6]
    
    
    
