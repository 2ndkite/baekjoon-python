import sys
n = int(sys.stdin.readline())
vote = list(sys.stdin.readline().rstrip())
a = vote.count("A")
b = vote.count("B")
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")
