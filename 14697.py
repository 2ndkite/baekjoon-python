import sys
a,b,c,n = map(int, sys.stdin.readline().split())
flag = False
for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):
            if a * i + b * j + c * k == n:
                flag = True
if flag:
    print(1)
else:
    print(0)
