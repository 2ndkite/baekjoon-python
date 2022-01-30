from itertools import combinations
N,M = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0

for i in combinations(num_list, 3):
    temp_sum = sum(i)
    if answer < temp_sum <= M:
        answer = temp_sum
print(answer)
