def solution(n, m):
    #최대공약수
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            a=i
            break
    #최소공배수
    for j in range(max(n,m),m*n+1):
        if j%n==0 and j%m==0:
            b=j
            break
    return [a,b]