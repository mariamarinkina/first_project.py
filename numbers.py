import sys

n=(sys.argv[1])

num=n.split(",")

nums=[]
for x in num:
    nums.append(int(x))

print(nums, nums[0], nums[-1], len(nums))