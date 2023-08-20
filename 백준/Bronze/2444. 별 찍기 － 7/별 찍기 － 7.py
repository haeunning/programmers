n = int(input())

for i in range(1,2*n):
    if i<= n:
        print(' '*(n-i)+'*'*(2*i-1))
    else:
        i = n-(i-n)
        print(' '*(n-i)+'*'*(2*i-1))