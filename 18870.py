import sys
n = sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))
a2 = list(sorted(set(a)))
dic = {a2[i]:i for i in range(len(a2))}
for i in a:
    sys.stdout.write('%d '%(dic[i]))
