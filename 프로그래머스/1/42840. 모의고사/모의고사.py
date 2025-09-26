## 1번 : 1, 2, 3, 4, 5                  (5)
## 2번 : 2, 1, 2, 3, 2, 4, 2, 5         (8)
## 3번 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5   (10)

# 문제 개수가 103개
# 문제 인덱스의 % size로 인덱싱

def solution(answers):
    
    id_1 = [i for i in range(1, 6)]; id_2 = [2, 1, 2, 3, 2, 4, 2, 5]; id_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    status = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == id_1[i % 5]:  status[0] += 1  # 1번
        if answers[i] == id_2[i % 8]:  status[1] += 1  # 2번
        if answers[i] == id_3[i % 10]: status[2] += 1  # 3번
        
    max_score = max(status); ans = []
    for i in range(3):
        if status[i] == max_score:
            ans.append(i + 1)
        
    return ans 