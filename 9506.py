import sys
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    factor = []
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):
            factor.append(i)
            if ((i**2) != n) :
                factor.append(n//i)
    factor.sort()
    factor.remove(n)
    if sum(factor) == n:
        print(n, " = ", " + ".join(str(i) for i in factor), sep="")
    else:
        print(n, "is NOT perfect.")
