num = int(input())
n = 0
m = 0
while num > m :
    n += 1
    m += n
loc = m - num
if n % 2 == 0 :
    top = n - loc
    bot = loc + 1
else :
    top = loc + 1
    bot = n - loc
print(f'{top}/{bot}')
