from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0; now_weight = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    while truck_weights:
        answer += 1
        now_weight -= bridge.popleft()
        
        if now_weight + truck_weights[0] <= weight:
            temp = truck_weights.popleft()
            now_weight += temp; bridge.append(temp)
        else:
            bridge.append(0)
    
    
    return answer + bridge_length