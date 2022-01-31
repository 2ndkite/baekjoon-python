n = int(input()) 
card = list(map(int, input().split())) 
dic = {}
for i in card: 
    if i in dic: 
        dic[i] += 1 
    else: 
        dic[i] = 1

m = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
