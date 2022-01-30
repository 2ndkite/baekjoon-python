dial_list = ['','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for i in dial_list :  
    for j in i:
        for k in word :
            if j == k :
                time += dial_list.index(i) + 2
print(time)
