# 최종 경우의 수: (각 의상 가짓수 + 1) 누적 곱 - 1 (안 입는 경우)
from functools import reduce
def solution(clothes):
    dic = {}; ans = 1
    
    for clo, typ in clothes:
        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 2
    ans = reduce(lambda x, y: x * y, dic.values(), 1)
    return ans - 1