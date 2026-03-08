import sys

s=sys.argv[1]
k=int(sys.argv[2])

symb=s.split(",")
num=[]
for x in symb:
    num.append(int(x))

n=len(num)
a=sum(num)/n

squSum=0
for x in num:
    squSum+=(x-a)**2

sigm=(squSum/n)**0.5

low=a-k*sigm
high=a+k*sigm

result=[]
for x in num:
    if x<low or x>high:
        result.append(x)

print(result)