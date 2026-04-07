import sys

list = []

for i in range(1, len(sys.argv)):
    list.append(int(sys.argv[i]))

def avg(list):
    add = 0
    for num in list:
       add += num
    return add / len(list)

result = avg(list)
print(result)