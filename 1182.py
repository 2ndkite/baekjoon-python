import sys
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += l[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - l[idx])
    dfs(idx + 1, sum)
n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
dfs(0, 0)
print(cnt)
