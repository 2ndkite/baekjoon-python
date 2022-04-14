import sys
money, people = map(int, sys.stdin.readline().split())
print(money//people)
print(money%people)
