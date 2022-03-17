import sys
a, b, c, m = map(int, sys.stdin.readline().split())
work = 0
exh = 0
for i in range(24):
    if exh + a <= m:
        exh += a
        work += b
    else:
        if exh - c >= 0:
            exh -= c
        else:
            exh = 0
print(work)
