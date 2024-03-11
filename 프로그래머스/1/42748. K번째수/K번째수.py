def solution(array, commands):

    answer = []

    for c in commands:

        i, j, k = c
        
        if i == j:
            answer.append(array[i - 1])
            continue
        else:     
            ls = sorted(list(array[i-1:j]))
            answer.append(ls[k - 1])


    return answer