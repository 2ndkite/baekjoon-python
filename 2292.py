n = int(input())
cnt = 1
edge = 1
while n > edge :
    edge += 6 * cnt
    cnt += 1
print(cnt)
