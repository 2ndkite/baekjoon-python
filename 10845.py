import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        queue.insert(0, a[1])
    elif a[0] == "pop":
        if len(queue) != 0: 
            print(queue.pop())
        else: 
            print(-1)
    elif a[0] == "size":
        print(len(queue))
    elif a[0] == "empty":
        if len(queue) == 0: 
            print(1)
        else : 
            print(0)
    elif a[0] == "front":
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[len(queue) -1])
    elif a[0] == "back":
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[0])
