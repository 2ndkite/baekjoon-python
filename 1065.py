def hansu(n) :
    cnt = 0
    for i in range(1, n+1):
        num_list = list(map(int,str(i))) # to use digit treat input as string
        if i < 100: # if input is double digits, anyway each digit is arithmetic sequence
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            # if input's digit is more than two, determine by definition
            cnt += 1
    return cnt

print(hansu(int(input())))
