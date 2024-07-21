import sys
input = sys.stdin.readline

sales = {}

for _ in range(int(input())):
    temp = input()
    if temp not in sales.keys():
        sales[temp] = 1
    else:
        sales[temp] += 1
final = sorted(sales.items(), key = lambda x : (-x[1], x[0]))
print(final[0][0])