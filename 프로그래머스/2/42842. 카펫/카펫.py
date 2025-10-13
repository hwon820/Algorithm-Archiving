# 전체 개수 = (yellow 가로 + 2) * (yelllow 세로 + 2) = 12
# yellow 개수 24 -> 24 / 1, 12 / 2, 6 / 4
#                   26 * 3, 14 * 4, 8 * 6

def solution(brown, yellow):
    
    total = brown + yellow
    
    for i in range(1, yellow + 1):
        if yellow % i == 0 and (i + 2) * (yellow//i + 2) == total:
            row = min(i, yellow//i) + 2; col = max(i, yellow//i) + 2
            return [col, row]