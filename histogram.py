import sys

s=sys.argv[1]
k=int(sys.argv[2])

num=[int(x) for x in s.split(",")]

minim=min(num)
maxim=max(num)

if k<=0:
    print([])
    sys.exit()

if minim==maxim:
    result=[len(num)]+[0]*(k-1) if k>0 else []
    print(result)
    sys.exit()

step=(maxim-minim)/k

conclusion=[0]*k

for n in num:
    if n==maxim:
        conclusion[-1]+=1
    else:
        idx=min(int((n-minim)/step), k-1)
        conclusion[idx]+=1

print(conclusion)