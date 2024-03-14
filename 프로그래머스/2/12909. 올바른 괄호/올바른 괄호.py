def solution(s):
    answer = True
    stay = []
    for i in s:
      # 열린 괄호는 무조건 append
        if i == '(':
            stay.append(i)
        else:
        # stay가 비었거나 최근에 추가된 열린 괄호가 없다면
            if len(stay) == 0 or stay.pop() != '(':
                return False
    # 여기가 문젠가
    if len(stay) > 0:
        return False

    return True