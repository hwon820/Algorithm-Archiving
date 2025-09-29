def solution(lottos, win_nums):
    score = {
        0 : 6,
        1 : 6,
        2 : 5,
        3 : 4,
        4 : 3,
        5 : 2,
        6 : 1
    }
    
    return score[len(set(lottos) & set(win_nums)) + lottos.count(0)], score[len(set(lottos) & set(win_nums))]
    
    
