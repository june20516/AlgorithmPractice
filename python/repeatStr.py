#2675
'''
R = int(input())

for i in range(R):
    S = input().split()
    result = ''
    for s in S[1]:
        result += '{}'.format(s*int(S[0]))
    print(result)
'''

#10809
'''
s = input()
aph = 'abcdefghijklmnopqrstuvwxyz'
arr = []

for i in aph:
    arr.append(str(s.find(i)))

print(' '.join(arr))
'''


#1157  #길어지면 시간초과, set이용해 계산
s = input().upper()

chars = list(set(s))
fre = []

for char in chars:
    fre.append(s.count(char))

maxnum = max(fre)
if fre.count(maxnum) > 1:
    print('?')
else:
    print(chars[fre.index(maxnum)])