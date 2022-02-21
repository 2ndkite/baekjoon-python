import sys
a, b = map(int, sys.stdin.readline().split())
al = list(map(int, sys.stdin.readline().split()))
bl = list(map(int, sys.stdin.readline().split()))
ans = al + bl
ans.sort()
print(' '.join(map(str, ans)))
