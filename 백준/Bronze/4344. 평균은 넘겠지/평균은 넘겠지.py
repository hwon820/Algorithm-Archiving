c = int(input())
for i in range(c):
  score = [*map(int,input().split())]
  n = score.pop(0)
  over = []
  for j in range(n):
    if score[j] > sum(score)/n:
      over.append(score[j])
    rate = len(over)/n*100
  print("%.3f" % rate + '%')