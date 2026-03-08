import sys
import math

dig = int(sys.argv[1])
squareRoot = int(math.sqrt(dig))

while dig % 2 == 0:
    print(2, end = " ")
    dig //= 2 
x = 3

while x <= squareRoot:
    while dig % x == 0:
        print(x, end=" ")
        dig //= x
    x += 2
    squareRoot = int(math.sqrt(dig))

if dig > 1:
    print(dig)