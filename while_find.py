import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

i = 0 

while i < len(list):
    if list[i] > 10:
        print (list[i])
        break
    i = i + 1