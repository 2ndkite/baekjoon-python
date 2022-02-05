import sys
n = int(sys.stdin.readline())
info = [0, 0, 0, 0, 0]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > 0 and b > 0:
        info[0] += 1
    if a < 0 and b > 0:
        info[1] += 1
    if a < 0 and b < 0:
        info[2] += 1
    if a > 0 and b < 0:
        info[3] += 1
    if a == 0 or b == 0:
        info[4] += 1    
        
print("Q1: %d" %(info[0]))
print("Q2: %d" %(info[1]))
print("Q3: %d" %(info[2]))
print("Q4: %d" %(info[3]))
print("AXIS: %d" %(info[4]))
