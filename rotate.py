import sys

s=sys.argv[1]
k=int(sys.argv[2])

symb=s.split(",")

num=[]
for x in symb: 
    num.append(int(x))

k=k%len(num)

if k==0:
    conclusion=num
else:
    conclusion=num[-k:]+num[:-k]
    
print(conclusion)