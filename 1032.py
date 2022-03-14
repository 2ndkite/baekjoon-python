import sys
n = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
l =len(a)
for i in range(n-1):
    b = list(sys.stdin.readline().rstrip())
    for j in range(l):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
