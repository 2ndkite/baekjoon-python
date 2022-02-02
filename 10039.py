import sys
result = 0
for i in range(5):
    m = int(sys.stdin.readline())
    if m <= 40:
        m = 40
    result += m      
print(result // 5)
