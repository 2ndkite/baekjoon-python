import sys
a = 100
b = 100
n = int(sys.stdin.readline())
for i in range(n):
    aa, bb = map(int, sys.stdin.readline().split())
    if aa > bb:
        b -= aa
    elif aa < bb:
        a -= bb
    else:
        a += 0
        b += 0
print(a)
print(b)
