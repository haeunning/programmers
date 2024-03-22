n = int(input())
tot = 0
result = 0
for i in range(1,n+1):
    i_len = len(str(i))
    for j in range(i_len):
        tot += int(str(i)[j])
    tot += i
    if tot == n:
        result = i
        break
    else:
        tot = 0

print(result)