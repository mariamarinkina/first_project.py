import sys

grade = int(sys.argv[1])

if grade == 5:
    print("excellent")
elif grade == 4:
    print("good")
elif grade == 3:
    print("satisfactory")
elif grade == 2:
    print("bad")
elif grade == 1:
    print("very bad")
else:
    print("invalid grade")    
