import sys
n = int(sys.stdin.readline())
num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
if int(sys.stdin.readline()) != 0:
    num -= set(map(str, sys.stdin.readline().split()))
min_cnt = abs(100 - n)
for i in range(1000001):
        i = str(i)
        for j in range(len(i)):
            if i[j] not in num:
                break
            elif j == len(i) - 1:
                min_cnt = min(min_cnt, abs(n - int(i)) + len(str(i)))
print(min_cnt)
