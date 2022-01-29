n = int(input())
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word.find(word[j]) > word.find(word[j+1]):
            n -= 1
            break
print(n)
