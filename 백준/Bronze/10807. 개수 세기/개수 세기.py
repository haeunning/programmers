n = int(input())
m = list(map(int,input().split()))
cnt = 0
k = int(input())
for i in m: 
    if i == k:
        cnt += 1
print(cnt)