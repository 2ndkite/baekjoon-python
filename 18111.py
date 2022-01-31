import sys
n, m, b = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
height = 0
ans = 199706061997060619970606
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if graph[j][k] < i:
                min += (i - graph[j][k])
            else:
                max += (graph[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i
print(ans, height)
