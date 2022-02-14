import sys
odd = []
for i in range(7):
    a = int(sys.stdin.readline())
    if (a % 2 == 1):
        odd.append(a)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
