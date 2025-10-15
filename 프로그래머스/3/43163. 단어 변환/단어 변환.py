from collections import deque
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    que = deque([[begin, 0]])
    
    while que:
        temp, step = que.popleft()
        
        if temp == target:
            return step
        
        for word in words:
            count = 0
            for i in range(len(word)):
                if temp[i] != word[i]:
                    count += 1
            if count == 1:
                que.append([word, step + 1])