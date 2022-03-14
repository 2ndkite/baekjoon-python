import sys
board = []
for i in range(8):
    board.append(list(sys.stdin.readline().rstrip()))
answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and board[i][j] == 'F':
            answer += 1
print(answer)
