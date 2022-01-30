def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix
 
 
star = ["***", "* *", "***"]

n = int(input())

exp = 0
while n != 3:
    n = int(n/3)
    exp += 1
 
for i in range(exp):
    star = stars(star)
for i in star:
    print(i)