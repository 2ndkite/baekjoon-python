from collections import Counter
N, M, B = map(int, input().split())
graph = []
for i in range(N):
    graph.extend(list(map(int, input().split())))


gg = Counter(graph)
arr = []
for h in range(max(gg.keys()), -1, -1):
    gt = 0
    inventory = B
    needed = 0
    for gh, gc in gg.items():
        if h < gh:
            inventory += (gh - h) * gc
            gt += 2 * (gh - h) * gc
        elif h > gh:
            needed += (h - gh) * gc
            gt += (h - gh) * gc
    if inventory >= needed:
        arr.append([gt, h])
arr.sort(key=lambda x: (x[0], -x[1]))
print(arr[0][0], arr[0][1])
