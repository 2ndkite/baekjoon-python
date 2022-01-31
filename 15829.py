L = int(input()) 
string = input() 
sigma = 0 
for i in range(L): 
    sigma += (ord(string[i])-96) * (31 ** i) 
print(sigma % 1234567891)
