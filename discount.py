import sys

sum = int(sys.argv[1])
cart = sys.argv[2]
age = int(sys.argv[3])

if sum > 1000 or cart == "yes" or age > 60:
    print("discount")
else:
    print("no discount")