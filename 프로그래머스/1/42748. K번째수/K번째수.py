def solution(array, commands):
    answer = []
    for cmd in commands:
        temp = sorted(array[cmd[0] - 1 : cmd[1]])
        answer.append(temp[cmd[2] - 1])
    return answer