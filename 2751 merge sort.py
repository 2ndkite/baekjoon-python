import sys 

def merge(arr): 
    if len(arr) <= 1: 
        return arr
    
    mid = len(arr)//2 
    mrg = [] 
    
    left, right = merge(arr[:mid]), merge(arr[mid:]) 
    i, j = 0, 0 
    
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            mrg.append(left[i]) 
            i += 1 
        else: 
            mrg.append(right[j]) 
            j +=1 
            
    if i != len(left): 
        mrg += left[i:] 
    if j != len(right): 
        mrg += right[j:] 
    return mrg 

N = int(sys.stdin.readline()) 
arr = [] 
for i in range(N): 
    arr.append(int(sys.stdin.readline())) 

answer = merge(arr) 
for n in answer: 
    print(n)
