# [0, 3, 3, 5, 6]
# 0 -> 0번 이상 인용 (5-0)편 / 0번 이하 인용 1편
# 1 -> 3번 이상 인용 (5-1)편 / 3번 이하 인용 2편  (지금까진)
# 2 -> 3번 이상 인용 (5-2)편 / 3번 이하 인용 3편   h = h

# 3 -> 5번 이상 인용 (5-3)편 / 5번 이하 인용 4편
# 4 -> 6번 이상 인용 (5-4)편 / 6번 이하 인용 5편


def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for idx, c in enumerate(citations, start = 1):
        if c >= idx:
            h = idx
    
    return h