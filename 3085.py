import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for i in range(n)]
cnt = 1
def sol():
    global cnt
    for i in range(n):
        t = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                t += 1
                cnt = max(cnt, t)
            else:
                t = 1
    for i in range(n):
        t = 1
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                t += 1
                cnt = max(cnt, t)
            else:
                t = 1
for i in range(n):
    for j in range(n-1):
        graph[i][j],graph[i][j+1] = graph[i][j+1],graph[i][j]
        sol()
        graph[i][j],graph[i][j+1] = graph[i][j+1],graph[i][j]

for i in range(n):
    for j in range(n-1):
        graph[j][i],graph[j+1][i] = graph[j+1][i],graph[j][i]
        sol()
        graph[j][i],graph[j+1][i] = graph[j+1][i],graph[j][i]
print(cnt)                
