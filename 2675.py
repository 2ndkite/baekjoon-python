case = int(input())
for i in range(case) :
    t, w = input().split()
    o = ""
    for j in w :
    	o += j * int(t)
    print(o)
