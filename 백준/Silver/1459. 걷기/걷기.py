x, y, w, s = map(int, input().split())
#평행 이동
move1 = (x + y) * w
#대각선 이동
if (x + y) % 2 == 0:  
    move2 = max(x, y) * s
else:  
    move2 = (max(x, y) - 1) * s + w
    
#대각+평행 이동
move3 = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)

res = min(min(move1, move2), move3)
print(res)
