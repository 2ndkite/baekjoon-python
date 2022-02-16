import sys

def dfs(depth, idx):
    global ans
    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        ans = min(ans, abs(start - link))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(sys.stdin.readline())

visited = [False] * n
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = sys.maxsize

dfs(0, 0)
print(ans)
