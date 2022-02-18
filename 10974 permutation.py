import sys
from itertools import permutations
n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]
for i in permutations(arr):
    for j in i:
        print(j, end=' ')
    print()
