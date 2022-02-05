import sys
t = int(sys.stdin.readline())
for i in range(t):
    s = int(sys.stdin.readline())
    school = []
    for i in range(s):
        a, b = map(str, input().split())
        school.append([a,int(b)])
    school = sorted(school, key = lambda x: x[1])
    print(school[-1][0])
