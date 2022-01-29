import sys
T = int(sys.stdin.readline()) 
for i in range(T): 
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    n = 0
    while True: 
        if d <= n*(n+1): 
            break 
        n += 1
    if d <= n**2: 
        print(n*2-1)
    else: 
        print(n*2)

"""
how i solve

1 : 1  -- 1^2
2 : 2
------ 1*2
3 : 3
4 : 3  -- 2^2
5 : 4
6 : 4
------ 2*3
7 : 5
8 : 5
9 : 5  -- 3^2
10: 6
11: 6
12: 6
------ 3*4
"""
