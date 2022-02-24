import sys
n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
left = 0
right = n-1
answer = liquid[left] + liquid[right]
idxl = left
idxr = right
while left < right:
    tmp = liquid[left] + liquid[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        idxl = left
        idxr = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(liquid[idxl], liquid[idxr])
