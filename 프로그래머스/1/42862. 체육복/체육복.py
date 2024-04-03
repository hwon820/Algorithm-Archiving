def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()

    # 여벌이 있는 학생
    new_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
    lost = new_lost

    # 여벌이 없는 학생
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] - reserve[j] == 1 or lost[i] - reserve[j] == -1:
                answer += 1
                reserve[j] = -1    # 빌려줬으면 표시
                break

    return n - (len(lost) - answer)