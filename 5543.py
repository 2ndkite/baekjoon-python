import sys
a = 2000
c = 2000
for i in range(3):
    b = int(sys.stdin.readline())
    a = min(a, b)
for i in range(2):
    b = int(sys.stdin.readline())
    c = min(c, b)
print(a + c - 50)
