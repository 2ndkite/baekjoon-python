import sys
S = set()
for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().rsplit()
    if order[0] == 'add':
        S.add(int(order[1]))
    elif order[0] == 'remove':
        S.discard(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in S:
             S.discard(int(order[1]))
        else:
            S.add(int(order[1]))
    elif order[0] == 'all':
        S = set(range(1, 21))
    elif order[0] == 'empty':
        S.clear()
