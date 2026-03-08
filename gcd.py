import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

while b!=0:
    divide =a%b
    a=b
    b=divide
print(a)