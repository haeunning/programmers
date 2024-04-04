n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

tot = 0
for i in range(n):
    max_b = max(b)
    tot += a[i]*max_b
    b.remove(max_b)
print(tot)