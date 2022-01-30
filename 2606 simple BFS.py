from collections import deque
n=int(input())
m=int(input())
graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start,graph):
    visited=[]
    queue=deque([start])
    visited.append(start)
    while queue:
        start=queue.popleft()
        for i in range(n+1):
            if i in graph[start] and i not in visited:
                queue.append(i)
                visited.append(i)
    return len(visited)-1

print(bfs(1, graph))
