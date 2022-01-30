import sys
from collections import Counter

arr = [] 
for i in range(int(sys.stdin.readline())): 
    arr.append(int(sys.stdin.readline())) 
    
arr.sort()

cnt = Counter(arr).most_common(2)

print(round(sum(arr)/len(arr)))
print(arr[len(arr) // 2])

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(arr[-1] - arr[0])
