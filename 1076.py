import sys
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(sys.stdin.readline().strip())
s = color.index(sys.stdin.readline().strip())
t = color.index(sys.stdin.readline().strip())
r = int(str(f) + str(s)) * (10 ** t)
print(r)
