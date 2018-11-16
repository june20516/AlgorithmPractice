#4344
import sys

test = open('python/test/overage.txt', mode='rt', encoding='utf-8')

C = int(test.readline())

for i in range(C):
    case = list(map(float,test.readline().split()))
    caseN = case[0]
    del case[0]
    caseAv = sum(case,0)/caseN
    count = 0
    for i in range(len(case)):
        if case[i] > caseAv:
            count += 1
    print('%.3f'%(count/caseN*100)+'%')
