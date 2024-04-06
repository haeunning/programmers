nums = set(range(1,10001))
generate_nums = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generate_nums.add(i)

self_nums = sorted(nums-generate_nums)
for i in self_nums:
    print(i)