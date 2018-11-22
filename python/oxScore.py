#8958
'''
n = int(input())

for i in range(n):
    ox = input()
    oxArr = ox.split('X')
    score = 0
    for O in oxArr:
        for i in range(len(O)):
            score += (i+1)
    print(score)
'''

#2920
'''
n = input()

if n == '1 2 3 4 5 6 7 8':
    print('ascending')
elif n == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')
'''

#10039
arr = []

for i in range(5):
    score = int(input())
    if score > 40:
        arr.append(score)
    else:
        arr.append(40)

print(int(sum(arr)/5))