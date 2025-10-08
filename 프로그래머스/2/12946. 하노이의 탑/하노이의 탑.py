# 하노이의 탑
# 1번 -> 3번 옮기기
##      1번 -> 2번으로 n-1개 옮기고
##      1번 -> 3번으로 1개 옮기고
##      2번 -> 3번으로 n-1개 옮기기
## n=1일 때 이동 경로 append하면서 종료

def solution(n):
    answer = []
    
    def hanoi(start, end, mid, n):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start, mid, end, n-1)
            hanoi(start, end, mid, 1)
            hanoi(mid, end, start, n-1)
    
    hanoi(1, 3, 2, n)
    
    return answer