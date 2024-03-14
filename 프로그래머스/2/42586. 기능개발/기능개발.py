# 기능개발
def solution(progresses, speeds):

    progresses.reverse()
    speeds.reverse()
    answer = []
    
    while len(progresses) != 0:

        cnt = 0
        
        progresses = [p + s for p, s in zip(progresses, speeds)]

        while progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            cnt += 1

            if len(progresses) == 0:
                break

        if cnt > 0:
              answer.append(cnt)
            
    return answer