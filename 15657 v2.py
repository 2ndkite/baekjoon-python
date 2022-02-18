import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def sol(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, n):
        ans.append(arr[i])
        sol(depth+1, i,)
        ans.pop()
sol(0, 0)
