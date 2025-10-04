from itertools import permutations

def solution(numbers):
    nums = list(numbers)
    candi = []
    for i in range(1, len(numbers)+1):
        for j in permutations(nums, i):
            candi.append(int("".join(j)))
    candi = set(candi)
    cnt = 0
    for c in candi:
        now = True
        
        if c < 2:  # 2보다 작은 경우 pass
            continue
        
        for n in range(2, int(c**0.5) + 1):
            if c % n == 0:
                now = False
                break
                
        if now:
            cnt += 1
                
            
    return cnt