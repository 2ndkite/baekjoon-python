n = int(input())
m = n - 9*len(str(n))
if m < 1:
    m = 1
for i in range(m, n+1):
    ans = i + sum(map(int, str(i)))
    if ans == n:
        print(i)
        break
    if i == n:
        print(0)
