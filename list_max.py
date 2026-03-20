import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

if len(list) == 0:
    print("нет чисел")
    sys.exit(0)

max = list[0]

for num in list[1:]:
    if num > max:
        max = num

print(max)
