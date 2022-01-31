import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
graph = []
graph = [list(sys.stdin.readline()) for i in range(n)]
visited = [[0] * n for i in range(n)]
    
count1 = 0
count2 = 0

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    for i in range(4):
        if (0 <= x+dx[i] < n) and (0 <= y+dy[i] < n):
            if visited[x+dx[i]][y+dy[i]] == 0:
                if graph[x+dx[i]][y+dy[i]] == graph[x][y]:
                    dfs(x+dx[i], y+dy[i])

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            count1 += 1
           
for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'
            
visited = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            count2 += 1

            
print(count1, count2)
