import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

num = 42
i = 0
found = False

while i < len(list):
    if list[i] == num:
        print(f"{list[i]} -> found!")
        found = True
        break
    elif list[i] < num:
        print(f"{list[i]} -> greater")
    else:
        print(f"{list[i]} -> less")

    i = i + 1

