num = int(input())
lst = sorted(list(map(int,input().split())), key = lambda x : abs(x))

val = 100000000000
temp = []

for i in range(len(lst)-1):
    can = lst[i] + lst[i+1]
    temp.append((min(abs(can), val), (lst[i], lst[i+1])))
temp.sort()

_min, _max = min(temp[0][1][0], temp[0][1][1]), max(temp[0][1][0], temp[0][1][1])
print(_min, _max)