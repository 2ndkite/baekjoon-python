N = int(input())
A = [0 for i in range(N+2)]
A[1] = 1
for N in range(2, N+2) :
    A[N] = A[N-1] + A[N-2]
print(A[N-1])
