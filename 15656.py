import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []

def sol(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans.append(arr[i])
        sol(depth+1)
        ans.pop()

sol(0)
