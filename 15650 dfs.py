import sys

n, m = map(int, sys.stdin.readline().split())

visit = [False]*n
result = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            result.append(i+1)
            dfs(depth+1,n,m)
            result.pop()
            for j in range(i+1, n):
                visit[j] = False

dfs(0, n, m)
