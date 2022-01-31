n = int(input()) 
card = list(map(int, input().split())) 
card.sort()
dic = {}
m = int(input())
check = list(map(int, input().split()))
for i in card: 
    if i in dic: 
        dic[i] += 1 
    else: 
        dic[i] = 1

def binarySearch(card, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if card[mid] == target:
        return dic.get(target)
    elif card[mid] < target:
        return binarySearch(card, target, mid+1, end)
    else:
        return binarySearch(card, target, start, mid-1)
    
for i in check:
    print(binarySearch(card, i, 0, len(card)-1), end=" ")
