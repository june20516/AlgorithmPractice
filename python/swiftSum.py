#15552

import sys

test = open('python/test/fastSumTest.txt', mode='rt', encoding='utf-8')

for i in range(int(test.readline())):
    case = test.readline()
    arr = list(map(int,case.split()))
    print(int(sum(arr,0)))