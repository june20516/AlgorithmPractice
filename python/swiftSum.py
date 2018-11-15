import sys

def swiftSum():
    s = sys.stdin.readline()
    a = s.split()
    if len(a) != 2:
        return
    print(int(a[0]) + int(a[1]))

while True:
    swiftSum()