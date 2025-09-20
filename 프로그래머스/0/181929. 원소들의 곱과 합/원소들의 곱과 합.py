def solution(num_list):
    if eval("*".join(str(s) for s in num_list)) < (sum(num_list) ** 2):
        return 1
    else:
        return 0