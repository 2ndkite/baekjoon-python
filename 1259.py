while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]: # indexing
        print("yes")
    else:
        print("no")
