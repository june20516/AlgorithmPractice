#2445
# n = int(input())
# for i in range(n):
#     print('{}'.format('*'*(i+1)), end='')
#     print('{}'.format(' '*2*(n-(i+1))), end='')
#     print('{}'.format('*'*(i+1)))
# for i in range(n-1,0,-1):
#     print('{}'.format('*'*(i)), end='')
#     print('{}'.format(' '*2*(n-(i))), end='')
#     print('{}'.format('*'*(i)))

#2446
n = int(input())

for i in range(0,n,1):
    print('{}'.format(' '*(i)), end='')
    print('{}'.format('*'*((n-i)*2-1)))
for i in range(n-1,0,-1):
    print('{}'.format(' '*(i-1)), end='')
    print('{}'.format('*'*((n-i+1)*2-1)))
    