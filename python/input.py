import sys

a, b, c = sys.stdin.read().split(" ")

a = int(a)
b = int(b)
c = int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

