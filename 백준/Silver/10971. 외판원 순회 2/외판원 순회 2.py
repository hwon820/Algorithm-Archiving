n = int(input())

distance = []
for _ in range(n):
    distance.append(list(map(int, input().split())))

visited = [False] * n
min_cost = float('inf')

def back(current_city, count, cost):
    global min_cost
    
    if count == n:
        if distance[current_city][start] != 0:
            min_cost = min(min_cost, cost + distance[current_city][start])
        return
    
    for next_city in range(n):
        if not visited[next_city] and distance[current_city][next_city] != 0:
            visited[next_city] = True
            back(next_city, count + 1, cost + distance[current_city][next_city])
            visited[next_city] = False

for start in range(n):
    visited[start] = True
    back(start, 1, 0)
    visited[start] = False

print(min_cost)