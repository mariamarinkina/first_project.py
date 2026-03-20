import sys

list = []

for i in range(1, len(sys.argv)):
    num = int (sys.argv[i])
    list.append(num)

print(list)