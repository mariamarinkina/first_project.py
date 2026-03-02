import sys
pal = 0
dig = int(sys.argv[1])
digit =dig
while dig > 0:
    ostatok = dig % 10
    pal = 10 * pal + ostatok
    dig //= 10
if pal == digit:
    print("True")
else:
    print("False")