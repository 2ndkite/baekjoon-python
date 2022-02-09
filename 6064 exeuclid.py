import sys
def exEuclid(M, N):
    r = [M, N]
    s = [1, 0]
    while r[1] != 0:
        s = s[1], s[0] - s[1] * (r[0] // r[1])
        r = r[1], r[0] - r[1] * (r[0] // r[1])
    return r[0], s[0]

for i in range(int(sys.stdin.readline())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    lcm, s = exEuclid(M, N)
    if abs(x-y) % lcm:
        print(-1)
    else:
        print((x - M*s*(x-y)//lcm) % (M*N//lcm))
