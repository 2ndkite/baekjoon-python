import sys
N, K = map(int, sys.stdin.readline().split()) 
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline()))
cnt = 0
coin.reverse()
for i in coin:
    cnt += K//i
    K = K%i
print(cnt)
