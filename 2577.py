a = int(input())
b = int(input())
c = int(input())
total= str(a*b*c)

for i in range(10):
    cnt = total.count(str(i))
    print(cnt)
