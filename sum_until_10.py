nums=[2,4,6,3]

sum=0

for n in nums:
    sum+=n
    if sum>=10:
        break

print(sum)