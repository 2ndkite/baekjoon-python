import sys
num = int(sys.stdin.readline())
for i in range(num):
    a,b = map(int, sys.stdin.readline().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a   
    gcd = b
    lcm = A * B //b
    print(lcm)
