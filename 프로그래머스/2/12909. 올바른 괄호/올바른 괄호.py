def solution(s):
    s = list(s); cand = []
    while s:
        temp = s.pop()
        if temp == ")":
            cand.append("(")
        else:
            if not cand:
                return False
            cand.pop()
    if cand:
        return False
    
    return True