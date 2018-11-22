import math

n = int(input())

# arr = []

# for i in range(n):
#     arr.append([])
#     for j in range(n):
#         arr[i].append(' ')
#     arr[i].append('\n')

# def starSq(n, x, y):
#     if n == 3:
#         for i in range(3):
#             for j in range(3):
#                 arr[y+i][x+j] = '*'
#         arr[y+1][x+1] = ' '
#         return
#     elif n == 1:
#         arr[0][0] = '*'
#         return
#     starSq(int(n/3),x,y)
#     starSq(int(n/3),x+int(n/3),y)
#     starSq(int(n/3),x+2*int(n/3),y)
#     starSq(int(n/3),x,y+int(n/3))
#     starSq(int(n/3),x+2*int(n/3),y+int(n/3))
#     starSq(int(n/3),x,y+2*int(n/3))
#     starSq(int(n/3),x+int(n/3),y+2*int(n/3))
#     starSq(int(n/3),x+2*int(n/3),y+2*int(n/3))

# starSq(n,0,0)

# for i in range(n):
#     for j in range(n+1):
#         print(arr[i][j],end='')


# n = 1
# a1 = ['*']

# n = 3
# a3 = [a1[0]*3, a1[0]+' '+a1[0], a1[0]*3]

# n = 9
# a9 = [a3[0]*3, a3[1]*3, a3[2]*3, a3[0]+' '*3+a3[0],a3[0]+' '*3+a3[0],a3[0]+' '*3+a3[0], a3[0]*3, a3[1]*3, a3[2]*3]

# n = 27

# a27 = [a9*3]



a = ['*']

def line(n,lst):
    end = lst * 3
    mid = []
    for i in range(int(n/3)):
        mid.append([lst[i], '{}'.format(' '*int(n/3)), lst[i]])
    return [end,mid,end]

arr = ['*']
idx = [1]
for i in range(8):
    idx.append(idx[i]*3)

for i in range(1,idx.index(n)+1,+1):
    arr = line(idx[i], arr)

print(arr)