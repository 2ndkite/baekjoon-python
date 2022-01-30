import sys
n = int(sys.stdin.readline())
time = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time.append([start, end])
time = sorted(time, key=lambda x: [x[1], x[0]])
last = 0
conut = 0
for i in time:
  if i[0] >= last:
    conut += 1
    last = i[1]
print(conut)
