import sys

age = int(sys.argv[1])
license = sys.argv[2]
sober = sys.argv[3]

if age >= 18 and license == ("yes") and sober ==("yes"):
    print("can drive")
else:
    print("cannot drive")    