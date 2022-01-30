import sys
n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def sol(x, y, n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[x][y] != graph[i][j]:
                print('(', end='')
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2,y,n//2)
                sol(x+n//2,y+n//2,n//2)
                print(')', end='')
                return
 
    if graph[x][y] == 1:
        print('1',end='')
        return
    else:   
        print('0',end='')
        return

sol(0,0,n)
