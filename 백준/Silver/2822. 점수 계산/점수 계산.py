score = []
for _ in range(8):
  s = int(input())
  score.append(s)

rescore = sorted(score, reverse = True)
sum = 0
total = []

for i in range(5):
  sum += rescore[i]
  total.append(score.index(rescore[i]))
  total.sort()

print(sum)
for i in total:
  print(i+1, end = ' ')