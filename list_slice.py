import sys

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from_slice = int(sys.argv[1])
to_slice = int(sys.argv[2])

print(list[from_slice:to_slice])