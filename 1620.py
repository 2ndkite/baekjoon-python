import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}
for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    dict[i] = a
    dict[a] = i
for i in range(m):
    prob = sys.stdin.readline().rstrip()
    if prob.isdigit():
        print(dict[int(prob)])
    else:
        print(dict[prob])
