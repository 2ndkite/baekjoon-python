start = int(input()) 
end = int(input())
prime = []
for i in range(start, end + 1 ):
    if i > 1:
        factor = True
        for j in range(2, i):
            if i % j == 0:
                factor = False
                break
        if factor:
            prime.append(i)
if len(prime) > 0 :
    print(sum(prime))
    print(min(prime))
else:
    print(-1)           
