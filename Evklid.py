import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
# Пока b не равен нулю
while b != 0:
    remainder = a % b   
    a = b               
    b = remainder       
print(a)