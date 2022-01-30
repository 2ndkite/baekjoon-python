dic = {}
n = int(input())
m = int(input())
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    a, b = map(int, input().split())
    dic[a]. add(b)
    dic[b]. add(a)

cnt = 0
visited = [0] * (n+1)

def dfs(n, dic):
    global cnt
    visited[n] = 1
    for i in dic[n]:
        if visited[i] == 0:
            dfs(i, dic)
            cnt += 1
dfs(1, dic)
print(cnt)
