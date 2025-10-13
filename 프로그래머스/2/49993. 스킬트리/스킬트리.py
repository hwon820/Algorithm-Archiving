def solution(skill, skill_trees):
    ans = 0; sub_tree = []
    for tree in skill_trees:
        temp = ''
        for s in tree:
            if s in skill: temp += s
        if temp == skill[:len(temp)]:
            ans += 1
    
        
    return ans