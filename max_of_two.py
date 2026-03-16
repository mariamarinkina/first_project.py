import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 < num2:
    print(num2)
elif num1 > num2:
    print(num1)
else:
    print("equal")