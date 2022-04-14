import sys
num1, num2 = (sys.stdin.readline().split())
num1, num2 = list(map(int, num1)), list(map(int, num2))
print(sum(num1) * sum(num2))
