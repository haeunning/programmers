import math
def solution(n):
    pizza = 0
    if n % 6 == 0:
        answer = n//6
    else:
        pizza = pizza + 6*n//math.gcd(6,n)
        answer = pizza//6
    return answer