#1546

N = int(input())
scores = list(map(float,input().split()))
modScores = []
M = max(scores)

for i in range(N):
    modScores.append(scores[i]/M*100)

print(sum(modScores,0.0)/N)
