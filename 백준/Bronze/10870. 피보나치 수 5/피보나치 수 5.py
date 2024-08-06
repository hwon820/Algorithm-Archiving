import sys
input = sys.stdin.readline

def fibo(n):
    if n > 1:
        return fibo(n-2) + fibo(n-1)
    else:
        return n

print(fibo(int(input())))