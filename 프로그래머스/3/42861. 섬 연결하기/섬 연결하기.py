# Kruskal
def solution(n, costs):
    
    visited = [0]*n
    costs = sorted(costs, key = lambda x: x[2]) # 최소 비용 순으로 정렬
    
    total_cost, path_move = 0, 0
    visited[0] = 1 # start node: 0번
    
    while path_move != n-1:
        for st, en, c in costs:
            if visited[st] + visited[en] == 1:
                visited[st] = 1
                visited[en] = 1
                total_cost += c
                path_move += 1
                break
    
    return total_cost