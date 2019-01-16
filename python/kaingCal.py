#6064
import sys

test = open('test/kaingCal.txt', mode='rt', encoding='utf-8')

t = int(test.readline())


for i in range(t):
    m, n, x, y = list(map(int,test.readline().split()))
    count = 0
    cycle = 0
    for j in range(n+1):
        count = cycle * m + x
        b = n if count % n == 0 else count % n
        cycle += 1
        if b == y:
            print(count)
            break