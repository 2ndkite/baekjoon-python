import sys
a = sys.stdin.readline()
for i in range(0, len(a), 10):
    print(a[i:i+10])
