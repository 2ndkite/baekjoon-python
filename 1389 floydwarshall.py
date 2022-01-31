import sys
n,m = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n): 
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in graph:
    result.append(sum(i))
print(result.index(min(result)) + 1)
