#2108

T = int(input())
arr = [0] * 8001
sum = 0

for i in range(T):
    idx = int(input())
    sum += idx
    arr[idx] += 1

#평균
print(int(sum / T + 0.5))

#중간값
midIdx = 0
j = -4000
while midIdx < T // 2:
    midIdx += arr[j]
    j += 1

print(j)


#모드
mode = arr.index(max(arr))
if mode > 4001:
    print(4001-mode)
else:
    print(mode)

#범위
c = 4001
while arr[c] = 0:
    c-=1
