import sys
n = sys.stdin.readline().rstrip()
cnt = 1
for i in range(len(n) - 1):
    if ord(n[i]) >= ord(n[i+1]):
        cnt += 1
print(cnt)

    
