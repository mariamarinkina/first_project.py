import sys

n=int(sys.argv[1])

total=0
for digit in str(n):
    total+=int(digit)
n=total
print(n)