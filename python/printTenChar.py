#11721
S = input()

repeat = int(len(S) / 10)
while repeat > 0:
    print(S[0:10])
    S = S[10:]
    repeat -= 1

print(S[0:])

