import sys
arr = [False, False] + [True] * 999999
for i in range(2, 1001):
    if arr[i]:
        for k in range(i+i, 1000001, i):
            arr[k] = False
flag = False
while True:
    n = int(sys.stdin.readline())
    if n == 0: 
        break            
    for i in range(3, len(arr)):
        if arr[i] and arr[n-i]:
            flag = True
            print(n, "=", i, "+", n-i)
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")
