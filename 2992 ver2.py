import sys
x = sys.stdin.readline().rstrip()
arr = [0] * 10
for i in range(len(x)):
    arr[int(x[i])] += 1
for i in range(int(x) + 1, 10 ** len(x)):
    new_arr = [0] * 10
    val = str(i)
    for j in range(len(val)):
        new_arr[int(val[j])] += 1
    flag = True
    for j in range(10):
        if new_arr[j] != arr[j]: flag = False
    if flag and i > int(x):
        print(i)
        exit()
print(0)
