from collections import deque
n = int(input())
deque = deque(list(range(1, n+1)))
while(len(deque) >1): 
    deque.popleft() 
    temp = deque.popleft() 
    deque.append(temp) 
print(deque[0])
