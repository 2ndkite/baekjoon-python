from collections import Counter
import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    wear = []
    for j in range(n):
        a, b = sys.stdin.readline().split()
        wear.append(b)
    dic = Counter(wear)
    cnt = 1
    for key in dic:
        cnt *= dic[key] + 1
    print(cnt-1)
