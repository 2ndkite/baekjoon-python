import sys
num = int(sys.stdin.readline())
board = [[0 for i in range(101)] for j in range(101)]
sum = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1
for i in range(1,101):
    for j in range(1,101):
        if board[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if board[nx][ny] == 1:
                    cnt += 1
            if cnt == 4:
                sum += 0
            elif cnt == 3:
                sum += 1
            elif cnt == 2:
                sum += 2
print(sum)
