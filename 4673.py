num = set(range(1, 10001))
del_num = set()
for i in num:
    for j in str(i):
        i += int(j)
    del_num.add(i)
self_num = sorted(num - del_num)
for a in self_num:
    print(a)
