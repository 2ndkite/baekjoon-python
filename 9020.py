import sys

array = [False, False] + [True] * 9999
for i in range(2, 101):
    if array[i] == True:
        for j in range(2*i, 10001, i):
            array[j] = False

for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    for j in range(a//2 + 1):
        if array[a//2 - j] == True and array[a//2 + j] == True:
            print(a//2 - j, a//2 + j)
            break
