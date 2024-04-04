n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]

cnt = 0
for i in reversed(range(n)):
    cnt += k//coin[i]
    k %= coin[i]

print(cnt)