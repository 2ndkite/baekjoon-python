x, y = map(int,input().split()) 
prime = [True] * (y + 1)
prime[0] = False
prime[1] = False 

for i in range(2, int(y ** 0.5) + 1): 
    if prime[i] == True: 
        for j in range(i * 2, len(prime), i): 
            prime[j] = False 
            
for k in range(x, y+1): 
    if prime[k] : 
        print(k)
