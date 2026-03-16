import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 % 2 == 0 or num2 % 2 == 0:
    print("at least one even")
else:
    print("no evens")