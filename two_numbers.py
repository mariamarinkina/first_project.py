import sys
n=int(sys.argv[1])
k=int(sys.argv[2])

while n >= 10:
    total = 0
    for digit in str(n):
        total += int(digit)
    n = total
print(n)

while k >= 10:
    total = 0
    for digit in str(k):
        total += int(digit)
    k = total
print(k)