import sys
list = []
n, k= map(int, sys.stdin.readline().split())
for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
        list.append(i)
        if ((i**2) != n):
            list.append(n//i)
list.sort()
if(k > len(list)):
    print(0)
else:
    print(list[k-1])
