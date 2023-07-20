man = int(input())
times = list(map(int, input().split()))
times.sort()

short = 0
for i in range(1,man+1):
    short += sum(times[:i])
print(short)