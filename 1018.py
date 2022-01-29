import sys
# input part
N, M = map(int, sys.stdin.readline().split())
board = []
count = []
for i in range(N):
    board.append(sys.stdin.readline())
    
"""
selecting 8 square in a row is same as picking one starting square(0,0)
except other 7 square ar row and column. So the range below for loop is
0 to N-7, 0 to M-7
"""
for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                # checking the color by whether the sum of row and column is odd or even
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W += 1
                    if board[k][l] != 'B':
                        first_B += 1
                else:
                    if board[k][l] != 'B':
                        first_W += 1
                    if board[k][l] != 'W':
                        first_B += 1
        count.append(min(first_W, first_B))
print(min(count))
