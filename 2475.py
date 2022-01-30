import sys
arr = list(map(int, sys.stdin.readline().split()))
s = 0
for i in arr:
    s += (i**2)
    
    
print(s % 10)
