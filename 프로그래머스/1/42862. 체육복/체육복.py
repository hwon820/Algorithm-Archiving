def solution(n, lost, reserve):
    reserve_ = list(set(reserve) - set(lost))
    lost_ = list(set(lost) - set(reserve))
    lst = 0
    for i in lost_:
        if i - 1 in reserve_:
            reserve_.remove(i-1)
        elif i + 1 in reserve_:
            reserve_.remove(i+1)
        else:
            lst += 1
    
    return n - lst
