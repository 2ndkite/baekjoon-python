n = int(input())
numbers = map(int, input().split())
cnt = 0
for i in numbers:
    factor = 0
    if(i == 1):
        continue
    for j in range(2, i):
        if i % j == 0:
            factor += 1
    if factor == 0:
        cnt += 1
print(cnt)   
