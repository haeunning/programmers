nums = list(input().split('-'))

for i in range(len(nums)):
    nums[i] = sum(map(int, nums[i].split('+')))

tot = nums[0]
for i in range(1,len(nums)):
    tot -= nums[i]

print(tot)