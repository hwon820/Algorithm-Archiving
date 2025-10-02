#  0  1  2  3  4
#  1  2  3  4  5
# [0, 1, 3, 5, 6]
# h = 6, 개수: idx + 1 개


def solution(citations):
    citations = sorted(citations, reverse = True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return len(citations)
            
