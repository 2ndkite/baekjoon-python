a = []
b = []
for i in range(3):
    aa,bb=map(int,input().split())
    a.append(aa)
    b.append(bb)
print(sorted(a,key=a.count)[0],sorted(b,key=b.count)[0])
