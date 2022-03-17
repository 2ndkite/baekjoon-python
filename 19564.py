import sys
n = sys.stdin.readline().rstrip()
l = [ord(i) for i in n]
cnt = 1
idx = len(n)
for i in range(idx - 1):
    if ord(n[i]) >= ord(n[i+1]):
        cnt += 1
print(cnt)
