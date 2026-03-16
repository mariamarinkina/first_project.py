import sys

one = int(sys.argv[1])
two = int(sys.argv[2])
three = int(sys.argv[3])

if one + two > three and one + three > two and two + three > one:
    print("yes")
else:
    print("no")