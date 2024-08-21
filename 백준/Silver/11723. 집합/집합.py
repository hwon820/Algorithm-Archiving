import sys
input = sys.stdin.readline

m = int(input())
check = set()
for _ in range(m):
    cmd = input().split()
    if len(cmd) > 1:
        num = int(cmd[1])
    
    if cmd[0] == 'add':
        check.add(num)
    elif cmd[0] == 'remove':
        check.discard(num)
    elif cmd[0] == 'check':
        print(1 if num in check else 0)
    elif cmd[0] == 'toggle':
        if num in check:
            check.discard(num)
        else:
            check.add(num)
    elif cmd[0] == 'all':
        check = set(range(1, 21))
    elif cmd[0] == 'empty':
        check.clear()