import sys
n = int(sys.stdin.readline())

for i in range(n):
    mars = list(map(str, sys.stdin.readline().split()))
    result = 0
    for i in range(len(mars)):
        if i == 0:
            result += float(mars[i])
        else:
            if mars[i] == "#":
                result -= 7
            elif mars[i] == "%":
                result += 5
            elif mars[i] == "@":
                result *= 3
                
    print("%0.2f" %result)
