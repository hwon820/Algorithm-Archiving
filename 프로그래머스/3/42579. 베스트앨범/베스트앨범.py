import heapq
def solution(genres, plays):
    music = {}; cnt = {}
    ans = []
    for idx in range(len(genres)):
        if genres[idx] in music.keys():
            heapq.heappush(music[genres[idx]],(-plays[idx], idx))
            cnt[genres[idx]] += plays[idx]
        else:
            music[genres[idx]] = [(-plays[idx], idx)]
            heapq.heapify(music[genres[idx]])
            cnt[genres[idx]] = plays[idx]
    
    
    orders = [(-v, k) for k, v in cnt.items()]
    heapq.heapify(orders)
    
    while orders:
        temp_genre = heapq.heappop(orders)[1]
        temp_lst = music[temp_genre]; top = 0
        while temp_lst and top < 2:
            ans.append(heapq.heappop(temp_lst)[1]); top += 1
            
    return ans