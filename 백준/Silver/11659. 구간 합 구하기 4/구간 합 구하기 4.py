import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

for k in range(1, n + 1):
    nums[k] += nums[k-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(nums[j] - nums[i-1])