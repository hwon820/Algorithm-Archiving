from collections import deque

def solution(arr):
    arr = deque(arr)
    
    fst = arr.popleft()
    answer = [fst]

    while arr:
        temp = arr.popleft()
        if temp != fst:
            answer.append(temp)
            fst = temp

    return answer