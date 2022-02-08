import sys
E, S, M = map(int, sys.stdin.readline().split())
temp= 1
 
while True:
    if (temp - E) % 15 == 0 and (temp - S) % 28 == 0 and (temp - M) % 19 == 0:
        print(temp)
        break
    temp += 1
