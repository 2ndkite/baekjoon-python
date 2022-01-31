import sys
n = int(sys.stdin.readline())
cnt = 0
a = [False]*n
b = [False]*(2*n-1)
c = [False]*(2*n-1)

def solve(i):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(cnt)
