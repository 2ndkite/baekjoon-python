import sys
for i in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    ans = 0
    for b in range(1, n):
        for a in range(1, b):
            if (a*a + b*b + m) % (a * b) == 0:
                ans += 1
    print(ans)
