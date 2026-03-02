import sys

s=sys.argv[1]
symb=s.split(",")

mid=len(symb)//2

print(symb[:mid], symb[mid:])