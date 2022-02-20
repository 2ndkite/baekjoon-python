import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
maximum = -sys.maxsize -1
minimum = sys.maxsize

def solve(index, ans, add, sub, mul, div) :
    global maximum, minimum
    if index >= N :
        maximum = max(maximum, ans)
        minimum = min(minimum, ans)
        return
    if add > 0 :
        solve(index+1, ans+a[index], add-1, sub, mul, div)
    if sub > 0 :
        solve(index+1, ans-a[index], add, sub-1, mul, div)
    if mul > 0 :
        solve(index+1, ans*a[index], add, sub, mul-1, div)
    if div > 0 :
        solve(index+1, ans//a[index] if ans > 0 else -((-ans)//a[index]), add, sub, mul, div-1)

solve(1, a[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
