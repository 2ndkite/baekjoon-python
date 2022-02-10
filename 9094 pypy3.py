import sys
for i in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    ans = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2+b**2+m)%(a*b) == 0:
                ans += 1
    print(ans)
