from collections import deque

dic = {} 
n = int(input())
m = int(input())
visited = [0] * (1 + n)
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    a, b = map(int, input().split())
    dic[a]. add(b)
    dic[b]. add(a)

count = 0 
def bfs(dic, visited, start):
  global count
  q = deque([start])
  visited[start] = 1
  while q:
    v = q.popleft()
    for i in dic[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1
        count += 1
 

bfs(dic, visited, 1)
print(count)
