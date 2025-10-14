# 각 인적사항을 key로 해시맵 생성
# {
#   "이름": ["a", "b", "c", "d", "e", "b"]
#   "전공": ["ㄱ","ㄴ","ㄷ", "ㄷ", "ㄱ","ㄱ"]
#   "학년": [2, 1, 3, 1, 3, 2]
# }


from itertools import combinations

def solution(relation):
    
    n = len(relation[0])
    cand_key = []
    key_idx = list(range(n))
    
    for i in range(1, n+1):
        for combi in combinations(key_idx, i):
            history = []
            for rel in relation:
                now_key = [rel[c] for c in combi]
                # 유일성 확인 - 같은 조합이 있다면 break
                if now_key in history:
                    break
                else:
                    history.append(now_key)
            else:
                # 최소성 확인
                for cand in cand_key:
                    if set(cand).issubset(set(combi)):  # for-else 부문. break 이후에는 else가 실행되지 X
                        break
                else:
                    cand_key.append(combi)
                    
    return len(cand_key)