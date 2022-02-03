import sys
dish = list(sys.stdin.readline().rstrip())
height = 10
for i in range(1, len(dish)):
    if dish[i-1] != dish[i]:
        height += 10
    else:
        height += 5
print(height)
