import sys
dp = [1]*1000001
sum = [0]*1000001
for i in range(2, 1000001):
    j = 1
    while i*j <= 1000000:
        dp[i*j] += i
        j += 1
for i in range(1, 1000001):
    sum[i] = sum[i-1] + dp[i]
t = int(sys.stdin.readline())
ans = []
for i in range(t):
    n = int(sys.stdin.readline())
    ans.append(sum[n])
for i in range(t):
    print(ans[i])
