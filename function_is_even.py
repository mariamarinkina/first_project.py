import sys 

n = int(sys.argv[1])

def even(n):
       if n % 2 == 0:
              print(True)
       else:
              print(False)

even(n)