import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def maximum(a,b):
       if a < b:
              return b
       else:
              return a
       
maximum = maximum (a, b)
print (maximum)