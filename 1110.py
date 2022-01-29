n = int(input())
num = n
t = 0
while True :
    a = num // 10  # over tens
    b = num % 10  # units
    c = (a+b) % 10
    num = (b * 10) + c
    t += 1
    
    if(num == n) :
        break
print(t)
