import sys
on = []
people = 0
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    people += b
    people -= a
    on.append(people)
print(max(on))
