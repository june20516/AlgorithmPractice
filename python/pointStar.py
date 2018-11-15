# N = int(input())

def pointStar(N):
    for i in range(N):
        star = ""
        for j in range(N-(i+1)):
            star += " "
        for k in range(i+1):
            star += "*"
        print(star)

def pointStarReverse(N):
    for i in range(N):
        star = ""
        for i in range(N-i):
            star += "*"
        print(star)

#2441
def pointStarInverse(N):
    for i in range(N):
        star = ""
        for j in range(i):
            star +=" "
        for j in range(N-i):
            star +="*"
        print(star)


