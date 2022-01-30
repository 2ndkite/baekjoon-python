T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    d_list = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1,n):
            d_list[j] += d_list[j-1]
    print(d_list[-1])
