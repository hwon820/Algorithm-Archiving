def solution(numbers):
    new_num = list(map(str, numbers))
    new_num.sort(key = lambda x : x*4, reverse = True)
    
    return str(int("".join(new_num)))