import sys
arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(sys.stdin.readline().rstrip())
arr = list(set(arr))
arr.sort()
arr.sort(key = len)
for i in arr:
    print(i)
