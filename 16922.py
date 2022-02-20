import sys
n = int(sys.stdin.readline())
s = set()
for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            t = n-i-j-k
            m = i + 5*j + 10*k  + 50*t
            s.add(m)

print(len(s))
