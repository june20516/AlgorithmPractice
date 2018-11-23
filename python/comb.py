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
step = 1
num = 1


while num < x:
    step += 1
    num += step*1

s = 1 + (x - step)
m = step - (x - step)

print('{s}/{m}'.format(s = s, m = m))