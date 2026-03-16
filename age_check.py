import sys

age = int(sys.argv[1])

if age < 18:
    print("child")
elif age < 66:
    print("adult")
else:
    print("pensioner")