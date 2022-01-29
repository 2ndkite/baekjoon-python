import sys
K, N = map(int, sys.stdin.readline().split())
l = []
for i in range(K):
    l.append(int(sys.stdin.readline()))
left = 1
right = max(l)
while left <= right: 
    mid = (left + right) // 2
    wire = 0
    for i in l:
        wire += i // mid
    if wire >= N:
        left = mid + 1
    else:
        right = mid - 1
print(right)
