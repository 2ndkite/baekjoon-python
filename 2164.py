n = int(input())
if n == 1 or n == 2: 
    print(n)
else:
    e = 1
    while n > 2**e:
        e += 1
    print(2**e - 2*(2**e - n))
