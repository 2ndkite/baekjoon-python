import sys
t = int(sys.stdin.readline())
arr = [1, 2, 4]
for i in range(3, 11):
    arr.append(arr[i - 3] + arr[i - 2] + arr[i - 1])
for i in range(t):
    n = int(sys.stdin.readline())
    print(arr[n-1])
