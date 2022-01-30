import sys
n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().split()))
nl = set(nl)
m = int(sys.stdin.readline())
ml = list(map(int,sys.stdin.readline().split()))
for i in ml:
    if i in nl:
        print("1")
    else:
        print("0")
