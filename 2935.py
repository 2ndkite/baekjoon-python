import sys
A = int(sys.stdin.readline())
cal = str(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline())

if cal == '*':
    print(A*B)
else:
    print(A+B)
