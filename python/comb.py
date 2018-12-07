#2292
'''
n = int(input())

cnt = 0
num = 1

while num < n:
    cnt += 1
    num = num + cnt*6
    
print(cnt+1)
'''

#1193
x = int(input())
head = []
tail = []

n = 0
while len(head) < x:
    if n % 2 == 0:
        for i in range(n):
            head.append(i+1)
    else:
        for i in range(n):
            head.append(n-i)
    n += 1
    
m = 0
while len(tail) < x:
    if m % 2 == 1:
        for j in range(m):
            tail.append(j+1)
    else:
        for j in range(m):
            tail.append(m-j)
    m += 1

print('{a}/{b}'.format(a = head[x-1], b = tail[x-1]))
