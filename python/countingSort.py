#108989
#countingSort
def countingSort(unsorted, maxNum):
    sorted = [-1] * len(unsorted)
    countingArray = [0] * (maxNum+1)
    #숫자 세어서 계수배열 채워넣기
    for i in unsorted:
        countingArray[i] += 1
    #계수배열 누적값으로 전환
    for i in range(maxNum):
        countingArray[i+1] += countingArray[i]
    #뒤에서부터, 정렬할 배열의 숫자를 정렬됨 배열의 알맞는 위치에 넣기
    for i in (len(unsorted),0,-1):
        sorted[countingArray[unsorted[i]]-1] = unsorted[i]
        countingArray[unsorted[i]] -= 1   
    return sorted


#raddix sort (메모리 초과로 실패)
from sys import stdin
array = [int(stdin.readline()) for i in range(int(stdin.readline()))]

def getDigit(num, d, base):  # d:자릿수, base:진법
    return (num // base ** d) % base

def countingSortByDigit(unsorted, d, base):
    k = base - 1 #base 시스템에서 최대값
    sorted = [-1] * len(unsorted)
    countingArray = [0] * (k + 1)
    #현재 자릿수 기준으로 숫자 세어서 계수배열 채우기
    for i in unsorted:
        countingArray[getDigit(i,d,base)] += 1
    #계수배열 누적값으로 전환
    for i in range(k):
        countingArray[i+1] += countingArray[i]
    #현재 자리수 기준으로 뒤에서부터 넣기
    for i in reversed(range(len(unsorted))):
        sorted[countingArray[getDigit(unsorted[i],d,base)]-1] = unsorted[i]
        countingArray[getDigit(unsorted[i],d,base)] -= 1   
    return sorted

from math import log
def radixSort(list, base=10):
    digit = int(log(max(list),base) + 1)
    for i in range(digit):
        list = countingSortByDigit(list,i,base)
    return list

sortedList = radixSort(array,base=10)
print(sortedList)

#성공!
from sys import stdin
countingArray = [0] * 10001
for i in range(int(stdin.readline())):
    countingArray[int(stdin.readline())] += 1
for j in range(10001):
    if countingArray[j] != 0:
        for k in range(countingArray[j]):
            print(j)