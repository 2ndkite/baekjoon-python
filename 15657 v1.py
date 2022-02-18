import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []

def sol(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, n):
            ans.append(arr[i])
            sol(i)
            ans.pop()
sol(0)
