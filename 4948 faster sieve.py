array = [False, False] + [True] * (2*123456 - 1)
for i in range(2, int((2*123456)**0.5 + 1)):
    if array[i] == True:
        for j in range(2*i, 2*123456 + 1, i):
            array[j] = False
while True:
    n = int(input())
    if n == 0: 
        break
    print(sum(array[n+1 : 2*n + 1]))
