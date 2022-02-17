import sys
n = sys.stdin.readline().rstrip()
digit = len(n)
visited = [False] * digit
ans = "999999"
num = ""

def sol(depth):
  global num
  global ans
    
  if depth == digit:
    if int(n) < int(num) < int(ans):
        ans = num
    return

  for i in range(digit):
    if visited[i] == False:
        visited[i] = True
        num += n[i]
        sol(depth + 1)
        visited[i] = False
        num = num[:-1]
    
sol(0)

if ans == '999999':
    ans = 0
print(ans)
