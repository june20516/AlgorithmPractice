#1065

N = int(input())

count = 0

def arith(list):
    for i in range(len(list)-2):
        if list[i] - list[i+1] != list[i+1] - list[i+2]:
            return False
    return True



for i in range(N):
    arr = [int(j) for j in str(i+1)]
    if len(arr) <= 2 or arith(arr):
        count += 1

print(count)