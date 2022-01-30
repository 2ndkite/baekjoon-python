import sys
n, m = map(int, sys.stdin.readline().split())
a = set() # Eliminate Duplicates
for i in range(n):
    a.add(sys.stdin.readline().rstrip())
b = set() # Eliminate Duplicates
for i in range(m):
    b.add(sys.stdin.readline().rstrip())
c = sorted(list(a & b))
print(len(c))
for i in c:
    print(i)
