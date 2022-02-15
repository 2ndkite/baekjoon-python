import sys
a, b = map(int, sys.stdin.readline().split())
n1 = min(a, b)
n2 = max(a, b)
n = n2 - n1 - 1
if n2 - n1 <= 1:
    n = 0    
print(n)
for i in range(n1 + 1, n2):
    print(i, end = ' ')
