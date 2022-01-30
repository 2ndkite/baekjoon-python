n = int(input())
m = 0
for i in range(n+1):
    m = i + sum(map(int, str(i)))
    if m == n:
        print(i)
        break
    if i == n:
        print(0)
