import sys
a, b = map(int, sys.stdin.readline().split())
people = list(map(int, sys.stdin.readline().split()))
party = a * b
for i in people:
    print(i - party, end=' ')
