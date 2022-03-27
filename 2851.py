import sys
m = []
score = 0
for i in range(10):
    m.append(int(sys.stdin.readline()))
for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)
