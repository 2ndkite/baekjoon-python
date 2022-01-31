import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x = int(sys.stdin.readline())
    if  x == 0:
        arr.pop()
    else:
        arr.append(x)
print(sum(arr))
