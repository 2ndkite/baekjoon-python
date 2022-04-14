import sys
n, m = map(int,sys.stdin.readline().split())
before = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
after = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
diff = []

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    diff.append([x,y])
    for i in range(4):
        if (0 <= x+dx[i] < n) and (0 <= y+dy[i] < m):
            if [x+dx[i], y+dy[i]] not in diff:
                if before[x+dx[i]][y+dy[i]] == before[x][y]:
                    dfs(x+dx[i], y+dy[i])
                    
flag = False
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            dfs(i,j)
            flag = True
            break
    if flag:
        break

for i in diff:
    before[i[0]][i[1]] = after[diff[0][0]][diff[0][1]]

if before == after:
    print("YES")
else:
    print("NO")
