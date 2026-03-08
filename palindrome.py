import sys

s=sys.argv[1]
c=(s[::-1])

if s==c:
    print(True)
else:
    print(False)