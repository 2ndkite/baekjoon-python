def prime(n): 
    array = [True] * (n) 
    for i in range(2, int(n**0.5) + 1): 
        if array[i] == True: 
            for j in range(2*i ,n, i): 
                array[j] = False 
    return [i for i in range(2, n) if array[i] == True] 

while True: 
    n = int(input()) 
    if n == 0: 
        break 
    prime_list = prime(2*n + 1) 
    answer_list = [i for i in prime_list if i > n] 
    print(len(answer_list))
