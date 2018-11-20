#4673

nonselfN = set()
tenThou = set()

def selfnumber(n):
    ans = n + n % 10 + int(n % 100 / 10) + int(n % 1000 / 100) + int(n % 10000 / 1000)
    if ans <= 10000:
        nonselfN.add(ans)

for i in range(10000):
    selfnumber(i+1)
    tenThou.add(i+1)

result = list(tenThou - nonselfN)
result.sort()
for i in result:
    print(i)