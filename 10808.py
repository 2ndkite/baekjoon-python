import sys
arr = [0]*26
s = sys.stdin.readline().rstrip()
for i in s:
    arr[ord(i)-97]+=1
for i in arr:
    print(i, end = " ")
