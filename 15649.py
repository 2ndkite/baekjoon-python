import sys
n, m = map(int, sys.stdin.readline().split())
visit = [False] * n
result = []

def dfs(depth, n, m):
    if depth == m:  
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if not visit[i] == True:
            visit[i] = True
            result.append(i+1)
            dfs(depth+1, n, m)
            visit[i] = False
            result.pop()
dfs(0, n, m)
