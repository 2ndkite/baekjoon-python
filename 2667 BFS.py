from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
apt = []
cnt = 0

def bfs(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    count += 1
    apt.append(count)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
        bfs(i, j)
        cnt += 1
apt.sort()
print(cnt)
for i in apt:
    print(i)
