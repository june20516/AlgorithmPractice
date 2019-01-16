#2108

arr = [0] * 8001
sum = 0
T = int(input())
for i in range(T):
    idx = int(input())
    sum += idx
    arr[idx] += 1

#mean
print(int(sum / T + 0.5))

midIdx = 0
j = -4000
while midIdx < T // 2:
    midIdx += arr[j]
    j += 1

#midVal
print(j)

#mode
mode = arr.index(max(arr))
if mode > 4001:
    print(4001-mode)
else:
    print(mode)

