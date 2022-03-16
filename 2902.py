import sys
n = list(map(str, sys.stdin.readline().split("-")))
for i in range(len(n)) :
    print(n[i][0], end = "")
