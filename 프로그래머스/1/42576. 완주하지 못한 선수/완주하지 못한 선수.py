from collections import Counter

def solution(participant, completion):
    
    part = Counter(participant)
    comp = Counter(completion)
    
    answer = part - comp
    
    return answer.most_common()[0][0]