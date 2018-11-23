#1316
'''
n = int(input())
nongroup = 0

for i in range(n):
    S = input()
    char = []
    for i in range(len(S)):
        if i == 0 or S[i-1] != S[i]:
            if S[i] not in char:
                char.append(S[i])
            else:
                nongroup += 1
                break
        
print(n-nongroup)
'''

#2908
'''
n = input().split()
a = int(n[0][2])*100 + int(n[0][1])*10 + int(n[0][0])
b = int(n[1][2])*100 + int(n[1][1])*10 + int(n[1][0])

print(max(a,b))
'''

#5622
'''
S = input()
num = dict()
alp = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for al in alp:
    num[al] = alp.index(al) + 3

time = 0
for char in S:
    for key in num:
        if char in key:
            time += num[key]

print(time)
'''

