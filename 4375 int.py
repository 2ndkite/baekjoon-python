import sys
while (line := sys.stdin.readline()):
    n = int(line)
    mod = 1 % n
    count = 1
    while mod != 0:
        mod =(mod * 10 + 1) % n
        count += 1
    print(count)
