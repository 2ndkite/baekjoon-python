import sys
list = [int(sys.stdin.readline()) for i in range(9)]
total = sum(list)
for i in range(9):
    for j in range(i+1, 9):
        if 100 == total - (list[i] + list[j]):
            a = list[i]
            b = list[j]
            list.remove(a)
            list.remove(b)
            list.sort()
            for k in range(len(list)):
                print(list[k])
            break
    if len(list)<9:
        break
