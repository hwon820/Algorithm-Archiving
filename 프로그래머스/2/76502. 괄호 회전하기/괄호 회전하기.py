#5:01

## deque 사용

# 원본 s의 정상 여부부터 파악한다 하면
## popleft - 열린 괄호일 때: stack에 append
##         - 닫힌 괄호일 때: stack top이 대응하는 열.괄이 아니면 비정상
from collections import deque
def solution(s):
    w = deque(s); cnt = 0
    maps = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for i in range(len(s)):
        # print(f"Now w:{w}")
        backup = w.copy()
        check = deque([]); cnt += 1
        while w:
            temp = w.popleft()
            if temp in maps.values():
                check.append(temp)
            else:
                if len(check) != 0 and maps[temp] == check[-1]:
                    check.pop()
                else:
                    cnt -= 1; check = deque([])
                    break
        if len(check) != 0:
            cnt -= 1
        w = backup; w.append(w.popleft())
        
    return cnt