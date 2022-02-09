import sys
p, k = map(int, sys.stdin.readline().split())
sieve = [False, False] + [True] * (k - 1)
for i in range(2, int(k**0.5)+1):
    if sieve[i]:
        for j in range(2 * i, k + 1, i):
            sieve[j] = False
flag = True
result = 0
for i in range(2, k):
    if sieve[i]:
        if p % i == 0:
            flag = False
            result = i
            break
if flag:
    print("GOOD")
else:
    print("BAD", result)
