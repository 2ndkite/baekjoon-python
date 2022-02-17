import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
visited = [False] * n
o = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, o)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            o.append(l[i])
            solve(depth+1, n, m)
            o.pop()
            visited[i] = False
solve(0, n, m)

