n = int(input())
arr = []

for i in range(n) : 
    arr.append(int(input()))

for i in range(1, n) :
    while (i>0) & (arr[i] < arr[i-1]) :
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1
        
for n in arr : 
    print(n)
