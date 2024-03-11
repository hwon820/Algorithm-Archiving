# 같은 숫자는 싫어
def solution(arr):

    arr.reverse()
    answer = []
    
    while len(arr) != 0:
        num = arr.pop()
    
        if  len(answer) == 0 or num != answer[-1]:
            answer.append(num)
        else:
            continue
    
    return answer