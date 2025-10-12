# dfs

def solution(numbers, target):
    results = []
    def dfs(now_idx, now_result):
        if now_idx > len(numbers) - 1:
            if now_result == target:
                results.append(now_result)
        else:
            dfs(now_idx + 1, now_result + numbers[now_idx])
            dfs(now_idx + 1, now_result - numbers[now_idx])
    
    dfs(1, numbers[0])
    dfs(1, -1 * numbers[0])
    
    return len(results)