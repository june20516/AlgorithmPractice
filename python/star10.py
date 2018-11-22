#2447
n = int(input())

'''분할정복, 시간초과됨.
arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(' ')
    arr[i].append('\n')
def starSq(n, x, y):
    if n == 3:
        for i in range(3):
            for j in range(3):
                arr[y+i][x+j] = '*'
        arr[y+1][x+1] = ' '
        return
    elif n == 1:
        arr[0][0] = '*'
        return
    starSq(int(n/3),x,y)
    starSq(int(n/3),x+int(n/3),y)
    starSq(int(n/3),x+2*int(n/3),y)
    starSq(int(n/3),x,y+int(n/3))
    starSq(int(n/3),x+2*int(n/3),y+int(n/3))
    starSq(int(n/3),x,y+2*int(n/3))
    starSq(int(n/3),x+int(n/3),y+2*int(n/3))
    starSq(int(n/3),x+2*int(n/3),y+2*int(n/3))
starSq(n,0,0)
for i in range(n):
    for j in range(n+1):
        print(arr[i][j],end='')
'''


def makeEnd(lst):
    result = []
    for i in range(len(lst)):
        result.append('{}'.format(lst[i]*3))
    return result

def makeMid(lst):
    result = []
    for i in range(len(lst)):
        result.append(lst[i] + '{}'.format(' '*len(lst)) + lst[i])
    return result

def line(lst):
    end = makeEnd(lst)
    mid = makeMid(lst)
    return end + mid + end

star = ['*']

idx = [1]
for i in range(8):
    idx.append(idx[i]*3)

for i in range(idx.index(n)):
    star = line(star)

for i in range(len(star)):
    print(star[i])