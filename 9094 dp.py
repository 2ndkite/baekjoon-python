#dynamic programming
import sys
t = int(sys.stdin.readline())
dp = [[0 for i in range(101)] for j in range(101)]
for b in range(1, 101):
    for m in range(1, 101):
        dp[b][m] = dp[b - 1][m]
        for a in range(1, b):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                dp[b][m] += 1

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n - 1][m])
