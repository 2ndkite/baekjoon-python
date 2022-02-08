import sys
n = sys.stdin.readline().rstrip()
digit, e = 0, 0
while e < (len(n)-1):
    digit += 9*(10**e)*(e+1)
    e += 1
digit += ((int(n)-(10**(len(n)-1)))+1) * len(n)
print(digit)
