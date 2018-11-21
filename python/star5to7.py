#2448
# n = int(input())

# for i in range(n):
#     print('{}'.format(' '*(n-(i+1))), end='')
#     print('{}'.format('*'*((i+1)*2-1)))


#2443
# m = int(input())

# for i in range(m):
#     print('{}'.format(' '*i), end='')
#     print('{}'.format('*'*((m-i)*2-1)))


#2444
n = int(input())

for i in range(n):
    print('{}'.format(' '*(n-(i+1))), end='')
    print('{}'.format('*'*((i+1)*2-1)))
m = n-1
for i in range(m):
    print('{}'.format(' '*(i+1)), end='')
    print('{}'.format('*'*((m-i)*2-1)))

