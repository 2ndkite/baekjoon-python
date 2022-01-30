import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    dic = dict()
    for i in range(n):
        a, b = sys.stdin.readline().split()
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
    cnt = 1
    for n in dic.values():
        cnt *= (n + 1)
    print(cnt-1)
