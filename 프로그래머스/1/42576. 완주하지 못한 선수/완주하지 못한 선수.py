def solution(participant, completion):
    answer = ''
    p = {}
    c = {}
    
    for i in participant:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1
    
    for i in completion:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    
    if set(participant) == set(completion):
        for i in p:
            if p[i] - c[i] == 1:
                return i
    else:
        answer += str(set(participant) - set(completion))[2:-2]
    
    return answer

## str.rstrip() : 문자열에서 필요없는 부분 지우기