import sys

year = int(sys.argv[1])

if year % 400 == 0:
    print("leap")
elif year % 100 == 0:
        print("common")
elif year % 4 == 0 :
        print("leap")
else:
    print("common")
