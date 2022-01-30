import sys
n, m = map(int,sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(trees)
while left <= right:
    mid = (left + right)//2
    sum = 0 
    for i in trees:
        if i > mid:
            sum += i - mid
    if sum >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
