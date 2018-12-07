#1011
import sys

endcheck = [0]

for i in range(100000):
    endcheck.append(endcheck[i]+(i+1))

def sumcheck(n):
    return path+endcheck[n]
        
n = int(sys.stdin.readline())

for j in range(n):
    raw = sys.stdin.readline().split()
    distance = int(raw[1])-int(raw[0])
    path = 0
    spd = 0
    count = 0

    while True:
        if sumcheck(spd+1) <= distance:
            spd += 1
            path += spd
            count += 1
        else:
            spd -= 1
        if path == distance:
            break

    print(count)