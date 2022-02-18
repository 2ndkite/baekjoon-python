import sys

n = int(sys.stdin.readline())
visited = [False] * n
ans = []

def sol(cnt):
  global ans
  if cnt == n:
      print(' '.join(ans))
      return
  else:
    for i in range(n):
      if visited[i] == False:
        visited[i] = True
        ans.append(str(i+1))
        sol(cnt+1)
        ans.pop()
        visited[i] = False
sol(0)
