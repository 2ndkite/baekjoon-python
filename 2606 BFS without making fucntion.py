from collections import deque
n=int(input())
m=int(input())
graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
cnt = 0
q = deque()
q.append(1)
visited[1] = 1
while q:
    now=q.popleft()
    for i in range(1,n+1):
        if i in graph[now] and visited[i] == 0:
            visited[i]=1
            q.append(i)
            cnt+=1
print(cnt)
