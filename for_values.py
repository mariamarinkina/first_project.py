import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

for i in list:
    print(i)

