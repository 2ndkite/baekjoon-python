import sys
n = int(sys.stdin.readline())
for i in range(n):
    stack = []
    ps = list(sys.stdin.readline().rstrip())
    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
