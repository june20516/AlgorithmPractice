N = int(input())

AF = int(N / 5)
R = N % 5

if R % 3 == 0:
    AT = int(R / 3)

while R % 3 != 0:
        AF -= 1
        if AF < 0:
            break
        R += 5

AT = int(R / 3)

if R % 3 == 0:
    print(AF + AT)
else:
    print(-1)
