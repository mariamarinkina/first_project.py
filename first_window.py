nums = [2, 1, 3, 2, 4]
target = 5

left=0
sum=0

for right in range(len(nums)):
    sum+=nums[right]

    while sum>target:
        sum-=nums[left]
        left+=1

    if sum==target:
        print(nums[left:right+1])
        break