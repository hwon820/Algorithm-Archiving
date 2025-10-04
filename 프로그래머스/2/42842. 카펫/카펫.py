# 가로 길이*2 + 세로 길이*2 + 4

def solution(brown, yellow):
    
    ans = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_x = i; y_y = yellow // i
            if y_x*2 + y_y*2 + 4 == brown:
                ans.append(y_x + 2); ans.append(y_y + 2)
                ans.sort(reverse = True)
                return ans