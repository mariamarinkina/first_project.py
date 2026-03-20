import sys

N = int(sys.argv[1])

num = 1

while num <= N:
    if num % 2 == 0:
        print (num)
    num = num + 1