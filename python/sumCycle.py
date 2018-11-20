#1110
first = int(input())
count = 0
num = first

while True:
    sumN = int(num * 0.1) + (num % 10)
    newN = (num % 10) * 10 + (sumN % 10)
    count += 1
    if newN == first:
        print(count)
        break
    num = newN