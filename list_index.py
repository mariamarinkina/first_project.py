import sys

list = [5, 10, 15, 20, 25, 30]

index = int(sys.argv[1])

if index <= 6:
    print(list[index])
else:
    print("index too big")