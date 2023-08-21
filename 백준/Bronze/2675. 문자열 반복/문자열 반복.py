n = int(input())

for _ in range(n):
    m, word = input().split()
    for x in word:
        print(x*int(m), end='')
    print()