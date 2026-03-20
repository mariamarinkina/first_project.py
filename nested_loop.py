import sys

lines = int(sys.argv[1])
columns = int(sys.argv[2])

for i in range(1, lines + 1):
    for j in range(1, columns + 1):
        print(f"{i} x {j} = {i * j}", end = " ")
    
    print()




