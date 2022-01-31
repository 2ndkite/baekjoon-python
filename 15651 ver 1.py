import sys
n, m = map(int, sys.stdin.readline().split())
result = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(i+1)
        dfs(depth+1, n, m)
        result.pop()
dfs(0, n, m)
