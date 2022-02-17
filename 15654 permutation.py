from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = map(str, arr)
print('\n'.join(list(map(' '.join, permutations(arr, M)))))
