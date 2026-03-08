import sys

y = int(sys.argv[1])
m = int(sys.argv[2])
d = int(sys.argv[3])

if y <= 0:
    print("Invalid date")
    sys.exit()

is_leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))

if m < 1 or m > 12:
    print("Invalid date")
    sys.exit()

if m == 2:
    if is_leap:
        maxDay = 29
    else:
        maxDay = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    maxDay = 30
else:
    maxDay = 31

if d < 1 or d > maxDay:
    print("Invalid date")
    sys.exit()

y1 = y - (14 - m) // 12
x = y1 + y1 // 4 - y1 // 100 + y1 // 400
m1 = m + 12 * ((14 - m) // 12) - 2
d1 = (d + x + 31 * m1 // 12) % 7

if d1 == 0:
    print("Sunday")
elif d1 == 1:
    print("Monday")
elif d1 == 2:
    print("Tuesday")
elif d1 == 3:
    print("Wednesday")
elif d1 == 4:
    print("Thursday")
elif d1 == 5:
    print("Friday")
elif d1 == 6:
    print("Saturday")