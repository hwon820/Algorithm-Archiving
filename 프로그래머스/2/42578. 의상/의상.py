# 경우의 수 정의
# 한 카테고리에 r 개: r + 1 개의 경우의 수(안 입는 거 포함) 
# 전체 카테고리 (r+1)을 곱하고 -1 (nothing)

def solution(clothes):
    maps = {}
    for c in clothes:
        if c[1] in maps.keys():
            maps[c[1]] += 1
        else:
            maps[c[1]] = 1
    ans = 1
    for i in maps.values(): ans *= i + 1
    return ans - 1