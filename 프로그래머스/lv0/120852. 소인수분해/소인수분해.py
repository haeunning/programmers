def solution(n):
    prime_factor = []
    answer = []
    i = 2
    while i<=n:
        if n%i == 0:
            prime_factor.append(i)
            n = n//i
        else:
            i += 1
    result = []
    for i in prime_factor:
        if i not in result:
            result.append(i)
    return  result