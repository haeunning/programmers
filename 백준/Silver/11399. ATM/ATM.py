man = int(input())
times = list(map(int, input().split()))
times.sort()

short = 0
for i in range(man):
    short += sum(times[:i+1])
print(short)
