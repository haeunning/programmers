n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_tot = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tot = nums[i]+nums[j]+nums[k]
            if tot <= m:
                max_tot = max(tot,max_tot)
print(max_tot)