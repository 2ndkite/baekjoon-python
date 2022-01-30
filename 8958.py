t = int(input())
for i in range(t):
    ox_list = list(input())
    sum = 0
    c = 1
    for i in ox_list:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
