import sys
n = int(sys.stdin.readline())
vote = []
for i in range(n):
    vote.append(int(sys.stdin.readline()))
if sum(vote) > (n//2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
