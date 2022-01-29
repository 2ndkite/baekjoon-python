import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]

visited_bfs = [0] * (n+1)
visited_dfs = [0] * (n+1)

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v) :
    visited_dfs[v] = 1
    print(v, end=" ")

    for i in range(1, n+1):
        if visited_dfs[i] == 0 and graph[v][i] == 1 :
            dfs(i)


def bfs(v) :
    q = deque()
    q.append(v)
    visited_bfs[v] = 1

    while(q) :
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1) :
            if visited_bfs[i] == 0 and graph[v][i] == 1 :
                q.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)
