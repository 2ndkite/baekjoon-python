import sys
import heapq
heap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x))
