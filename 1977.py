import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
num = []
for i in range(m, n+1):
    if i == (int(i ** 0.5) ** 2):
        num.append(i)
if num == []:
    print(-1)
else:
    print(sum(num))
    print(min(num))
