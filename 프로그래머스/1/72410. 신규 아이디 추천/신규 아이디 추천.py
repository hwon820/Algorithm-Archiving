# 3 ~ 15글자
# 알파벳 소문자, 숫자, -, _, .  /  .은 연속, 처음, 끝 X

import re

def solution(new_id):
    
    #1
    answer = new_id.lower()
    #2
    answer = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]', '', answer)
    print(answer)
    #3
    while ".." in answer:
        answer = answer.replace('..', '.')
    print(answer)
    #4
    answer = answer.strip('.')
    print(answer)
    #5
    if len(answer) == 0:
        answer += 'a'
        print(answer)
    #6
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        print(answer)
    #7
    while len(answer) < 3:
        temp = answer[-1] 
        answer += temp
        print(answer)
    
    return answer