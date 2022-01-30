import sys
t = int(sys.stdin.readline())
for i in range(t):
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    arr = list(map(int, sys.stdin.readline().split(' ')))
    idx = list(range(len(arr)))
    order = 0
    while True:
        if arr[0] == max(arr):
            order += 1

            if idx[0] == m:
                print(order)
                break
            else:
                arr.pop(0)
                idx.pop(0)

        else:
            arr.append(arr.pop(0))
            idx.append(idx.pop(0))
