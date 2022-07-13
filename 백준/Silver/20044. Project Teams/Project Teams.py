n = int(input())
abi = sorted([*map(int,input().split())])
minsum = 1000000

for i in range(len(abi)//2):
    minsum = min(minsum, abi[i] + abi[len(abi)-1-i])

print(minsum)