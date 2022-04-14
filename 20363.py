import sys
h, w = map(int, input().split())
print((h+w)+w//10 if h >= w else (h+w)+h//10)
