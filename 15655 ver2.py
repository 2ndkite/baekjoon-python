import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False] * n
ans = []

def solve(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            solve(i + 1)
            ans.pop()
            visited[i] = False

solve(0)
