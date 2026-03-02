import sys

y=int(sys.argv[1])
m=int(sys.argv[2])

if y<1:
    print(False)
    sys.exit()

year=(y%4==0 and (y%100!=0 or y%400==0))

if m<1 or m>12:
    print(False)
    sys.exit()

if m==2:
    if year:
        maxDay=29
    else:
        maxDay=28
elif m==4 or m==6 or m==9 or m==11:
    maxDay=30
else:
    maxDay=31

print(maxDay)