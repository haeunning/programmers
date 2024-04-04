from sys import stdin

n = int(stdin.readline())
time = []
for i in range(n):
    a, b = map(int, stdin.readline().split())
    time.append((a,b))

cnt = 0
end = 0

time = sorted(time, key=lambda k: k[0])
time = sorted(time, key=lambda k: k[1])

for i, j in time:
    if i >= end:
        cnt += 1
        end = j

print(cnt)