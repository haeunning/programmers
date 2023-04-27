def solution(n):
    a = []
    i = 1
    for i in range(1,n):
        if n%i == 1:
            a.append(i)
    return a[0]