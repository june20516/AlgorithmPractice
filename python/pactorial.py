#8393
# n = int(input())
#재귀
def pactoPlus(n):
    if n == 0:
        return 0
    return n + pactoPlus(n - 1)
#for
def pacforPlus(n):
    sum = n
    for i in range(n):
        sum += i
    print(sum)




#11720
a = int(input())
b = input()
bArr = list(map(int,b))

ans = 0
for i in range(a):
    ans += bArr[i]

print(ans)

