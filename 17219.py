import sys
N, M = map(int, sys.stdin.readline().split())
add = {}
for i in range(N):
    site, ps = sys.stdin.readline().split()
    add[site] = ps
for i in range(M):
    print(add[sys.stdin.readline().rstrip()])
