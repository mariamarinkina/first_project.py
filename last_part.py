import sys

s=sys.argv[1]
num=int(sys.argv[2])

symb=s.split(",")

print(symb[-num:])