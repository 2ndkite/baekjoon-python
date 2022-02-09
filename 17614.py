import sys
n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n+1):
    temp = str(i)
    cnt = cnt + temp.count('3')+temp.count('6')+temp.count('9')
print(cnt)
