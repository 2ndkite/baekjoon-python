import sys
while (line := sys.stdin.readline()):
    n = int(line)
    ans = '1'
    while True:
        if int(ans) % n == 0:
            print(len(ans))
            break
        ans += '1'
