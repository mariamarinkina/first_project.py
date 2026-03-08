import sys

n=int(sys.argv[1])

if n<2:
    print([])
    sys.exit()

simple=[True]*(n+1)

simple[0]=False
simple[1]=False

p=2
while p*p<=n:
    if simple[p]:
        multiple=p*p
        while multiple<=n:
            simple[multiple]=False
            multiple+=p
    p+=1

is_simple=[]
for i in range(2,n+1):
    if simple[i]:
        is_simple.append(i)

print(is_simple)