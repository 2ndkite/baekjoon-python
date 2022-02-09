import sys
for i in range(int(sys.stdin.readline())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    flag = True
    while(x <= M*N):
        if x%N == y%N:
            print(x)
            flag = False
            break
        x += M
    if flag:
        print(-1)
