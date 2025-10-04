# 1 2 3 4 5
# 2 1 2 3 2 4 2 5
# 3 3 1 1 2 2 4 4 5 5

def solution(answers):
    student_1 = [1, 2, 3, 4, 5]; n1 = len(student_1)
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]; n2 = len(student_2)
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; n3 = len(student_3)
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if student_1[i % n1] == answers[i]:
            cnt[0] += 1
        if student_2[i % n2] == answers[i]:
            cnt[1] += 1
        if student_3[i % n3] == answers[i]:
            cnt[2] += 1
        
    max_ = max(cnt); ans = []
    for j in range(len(cnt)):
        if cnt[j] == max_:
            ans.append(j+1)
            
    return ans 