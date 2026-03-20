import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

for num in list:
    print(num)
    if num == 7:
        print("found 7!")
        break
