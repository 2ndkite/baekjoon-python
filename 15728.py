import sys
n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))
for i in range(k):
    tmp = -sys.maxsize
    dummy = 0
    for i in t:
        for j in s:
            if tmp <= i*j:
                tmp = i*j
                dummy = i
    t.remove(dummy)
ans = -sys.maxsize
for i in t:
    for j in s:
        ans = max(ans, i*j)
print(ans)
