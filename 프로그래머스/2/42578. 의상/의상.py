# Counter 사용
from collections import Counter
from functools import reduce
def solution(clothes):
    c_map = Counter([typ for cloth, typ in clothes])
    ans = reduce(lambda x, y: x*(y+1), c_map.values(), 1) - 1
    return ans