#2941

S = input()

length = len(S)
crt = ['dz=','=','lj','nj','-']

for cal in crt:
    if cal in S:
        length -= S.count(cal)

print(length)