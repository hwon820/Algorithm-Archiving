n = int(input())
score = [*map(int, input().split())]

m = max(score)
avr = (sum(score)*100/m) / len(score)
print(avr) 