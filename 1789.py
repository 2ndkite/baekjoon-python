import sys
n = int(sys.stdin.readline())
m = 1
while m * (m + 1) / 2 <= n:
    m += 1
print(m - 1)
