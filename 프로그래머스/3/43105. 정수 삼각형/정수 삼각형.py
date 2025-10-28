# 7
# 10  15
# 18  16  15
# 20  25  20  19
# 24  30  27  26  24

# 현재 인덱스에서 (+1, 0) & (+1, +1) 이동
# 같은 형태의 삼각형 생성 -> 누적합 저장 -> 이미 다른 값이 저장되어 있다면 비교해서 최대값으로 변경

def solution(triangle):
    
    depth = len(triangle)
    new_tri = [[0]*(n+1) for n in range(depth)]
    new_tri[0][0] = triangle[0][0]
    for i in range(depth - 1):
        for j in range(len(triangle[i])):
            new_tri[i+1][j] = max(new_tri[i][j] + triangle[i+1][j], new_tri[i+1][j])
            if j+1 < len(triangle[i+1]):
                new_tri[i+1][j+1] = max(new_tri[i][j] + triangle[i+1][j+1], new_tri[i+1][j+1])

    return max(new_tri[-1])