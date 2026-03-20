import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

for num in list:
    if num % 2 != 0:
        print(num)