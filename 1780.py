import sys
n = int(sys.stdin.readline())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rsplit())))
def sol(x, y, n):
    global minus_cnt, zero_cnt, plus_cnt
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != graph[x][y]:
                for i in range(3):
                    for j in range(3):
                        sol(x+n//3*i,y+n//3*j,n//3)
                return
    if graph[x][y] == -1:
        minus_cnt += 1
    elif graph[x][y] == 0:
        zero_cnt += 1
    elif graph[x][y] == 1:
        plus_cnt += 1
    return

sol(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
