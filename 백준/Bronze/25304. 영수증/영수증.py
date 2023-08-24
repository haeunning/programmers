money = int(input())
n = int(input())
tot = 0
for i in range(n):
    pay, k = map(int,input().split())
    tot += pay*k
if tot==money:
    print('Yes')
else:
    print('No')