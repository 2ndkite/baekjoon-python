from itertools import combinations
import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
ans = sys.maxsize
member = combinations(range(n), n//2)
for i in member:
    a = set(i)
    b = list(set(range(n)) - a)
    a = list(a)
    start, link = 0, 0
    for i in range(n//2 - 1):
        for j in range(i+1, n//2):
            start += graph[a[i]][a[j]] + graph[a[j]][a[i]]
            link +=  graph[b[i]][b[j]] + graph[b[j]][b[i]]  
    ans = min(ans, abs(start - link))
print(ans)    
