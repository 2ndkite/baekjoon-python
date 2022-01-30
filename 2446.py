import sys
n = int(sys.stdin.readline())
for i in range(0, n-1):
    print(' ' * (i) +'*'*((2*(n-i))-1))
for j in range(1, n+1):
    print(' ' * (n-j) +'*'*((2*j)-1))
